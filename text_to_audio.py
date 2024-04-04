"""
云服务器上需如果出现报错 Exception with an error code: 0x38 (SPXERR_AUDIO_SYS_LIBRARY_NOT_FOUND), 需要运行以下命令
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
sudo dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb
"""

import os
import time
import sys
import re
from tqdm import tqdm
import os
import azure.cognitiveservices.speech as speechsdk

voice_names = (
    ("zh-CN-XiaoxiaoNeural", "Female"),
    ("zh-CN-XiaoyiNeural", "Female"),
    ("zh-CN-XiaochenNeural", "Female"),
    ("zh-CN-XiaohanNeural", "Female"),
    ("zh-CN-XiaomengNeural", "Female"),
    ("zh-CN-XiaomoNeural", "Female"),
    ("zh-CN-XiaoqiuNeural", "Female"),
    ("zh-CN-XiaoruiNeural", "Female"),
    ("zh-CN-XiaoshuangNeural", "Female, Child"),
    ("zh-CN-XiaoyanNeural", "Female"),
    ("zh-CN-XiaoyouNeural", "Female, Child"),
    ("zh-CN-XiaozhenNeural", "Female"),
    ("zh-CN-XiaochenMultilingualNeural", "Female"),
    ("zh-CN-XiaorouNeural", "Female"),
    ("zh-CN-XiaoxiaoDialectsNeural", "Female"),
    ("zh-CN-XiaoxiaoMultilingualNeural", "Female"),
    ("zh-CN-XiaoyuMultilingualNeural", "Female"),
    ("zh-CN-YunxiNeural", "Male"),
    ("zh-CN-YunjianNeural", "Male"),
    ("zh-CN-YunyangNeural", "Male"),
    ("zh-CN-YunfengNeural", "Male"),
    ("zh-CN-YunhaoNeural", "Male"),
    ("zh-CN-YunxiaNeural", "Male"),
    ("zh-CN-YunyeNeural", "Male"),
    ("zh-CN-YunzeNeural", "Male"),
    ("zh-CN-YunjieNeural", "Male"),
    ("zh-CN-YunyiMultilingualNeural", "Male"),
)
SPEECH_KEY = "db9a08a574d344b58e1d7177d865e1d1"
SPEECH_REGION = "eastasia"

name_to_voice_name = {
    "旁白": "zh-CN-XiaoyiNeural",
    "叶凌飞": "zh-CN-YunhaoNeural",
    "白晴婷": "zh-CN-XiaoxiaoNeural",
    "周欣茗": "zh-CN-XiaochenNeural",
    "唐晓婉": "zh-CN-XiaomoNeural",
    "李可欣": "zh-CN-XiaozhenNeural",
    "秦瑶": "zh-CN-XiaochenMultilingualNeural",
    "于婷婷": "zh-CN-XiaoyiNeural",
    "陈玉婷": "zh-CN-XiaochenNeural",
    "张璐雪": "zh-CN-XiaomoNeural",
    "于筱笑": "zh-CN-XiaozhenNeural",
    "张雪寒": "zh-CN-XiaochenMultilingualNeural",
    "萧雨雯": "zh-CN-XiaoyiNeural",
    "彭晓露": "zh-CN-XiaomengNeural",
    "Xiaoxiao": "zh-CN-XiaoxiaoNeural",
    "Xiaoyi": "zh-CN-XiaoyiNeural",
    "Xiaochen": "zh-CN-XiaochenNeural",
    "Xiaohan": "zh-CN-XiaohanNeural",
    "Xiaomeng": "zh-CN-XiaomengNeural",
    "Xiaomo": "zh-CN-XiaomoNeural",
    "Xiaoqiu": "zh-CN-XiaoqiuNeural",
    "Xiaorui": "zh-CN-XiaoruiNeural",
    "Yunxi": "zh-CN-YunxiNeural",
    "Yunhao": "zh-CN-YunhaoNeural",
    "Yunjian": "zh-CN-YunjianNeural",
    "Yunze": "zh-CN-YunzeNeural"
}

name_pattern = re.compile(fr"{'|'.join(sorted(name_to_voice_name.keys(), key=len, reverse=True))}")
sentence_pattern = re.compile(r"^(?P<before>.*?)(?P<dialog>“[^”]{4,}”)(?P<after>.*?)$")


def file_alreay_works(file_path):
    if not os.path.exists(file_path):
        return False

    if os.path.getsize(file_path) == 0:
        return False

    return True


def get_role_and_dialog(line):
    dialog = []
    if not line.startswith("　　"):
        dialog.append(("旁白", line))

    elif not sentence_pattern.search(line):
        dialog.append(("旁白", line))

    else:
        matched_result = sentence_pattern.search(line).groupdict()
        matched_role_names = name_pattern.findall(matched_result["before"] + matched_result["after"])

        role_name = matched_role_names[0] if matched_role_names else "旁白"

        if matched_result["before"].strip():
            dialog.append(("旁白", matched_result["before"]))

        dialog.append((role_name, matched_result["dialog"]))

        if matched_result["after"].strip():
            dialog.append(("旁白", matched_result["after"]))

    return dialog


def generate_voice(content, voice_name, rate=None, duration=None, style="Gentle", styledegree=5):
    voice_content = content

    if rate:
        voice_content = f"""
            <prosody rate="{rate}">
                {voice_content}
            </prosody>
            """

    if duration:
        voice_content = f"""
        <mstts:audioduration value="{duration}s"/>
        {voice_content}
        """

    voice_content = f"""
                <voice name="{voice_name}">
                    <mstts:express-as style="{style}" styledegree="{styledegree}" > 
                        {voice_content}
                    </mstts:express-as>
                </voice>"""

    return voice_content


def generate_audio(
    dialog,
    audio_file_path,
    debug=False,
    overwrite=False,
    rate=None,
    duration=None,
    style="Gentle",
    xml_lang="zh-CN",
    styledegree=5,
    log=print,
):
    if not overwrite and audio_file_path is not None and file_alreay_works(audio_file_path):
        if not debug:
            log(f"[ Skip ] {audio_file_path} already exists and works.")
        return True

    if [1 for line in dialog if line[1].strip("　……")]:
        log(f"[ Generate ] {audio_file_path} for text: {dialog}")

    content = "\n".join([
        generate_voice(
            content=line[1],
            voice_name=name_to_voice_name.get(line[0], "zh-CN-XiaochenMultilingualNeural"),
            rate=rate,
            duration=duration,
            style=style,
            styledegree=styledegree,
        ) for line in dialog if line[1].strip("　…")
    ])

    if not content:
        return True

    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    if audio_file_path is None:
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    else:
        audio_config = speechsdk.audio.AudioOutputConfig(filename=audio_file_path)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    text = f"""
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="{xml_lang}">
                {content}
            </speak>
            """

    speech_synthesis_result = speech_synthesizer.speak_ssml_async(text).get()

    for retry_count in range(3):
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            if debug:
                log(f"[ Completed ] {audio_file_path} generated for text: {dialog}")

            break

        cancellation_details = speech_synthesis_result.cancellation_details
        if cancellation_details.reason == speechsdk.CancellationReason.Error and cancellation_details.error_details:
            log(cancellation_details.error_details)
        if debug:
            log(f"Error Occurred. text: {text}")
            log("=" * 32)
        time.sleep(1)
        log(f"Retrying #{retry_count}")
