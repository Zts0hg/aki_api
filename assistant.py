import openai
import os
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain import PromptTemplate, OpenAI, LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import SequentialChain
from langchain.chat_models import AzureChatOpenAI

deployment = "text_model"
model = "gpt-35-turbo"

openai_config = {
    "openai_api_type": "azure",
    # "openai_api_base": "https://ai-test-for-aki.openai.azure.com/",
    "openai_api_base": "https://shibainu.openai.azure.com/",
    "openai_api_version": "2023-07-01-preview",
    "openai_api_key": os.environ.get("OPENAI_API_KEY"),
}
openai.api_type = openai_config["openai_api_type"]
openai.api_base = openai_config["openai_api_base"]
openai.api_version = openai_config["openai_api_version"]
openai.api_key = openai_config["openai_api_key"]


class Assistant:
    llm = AzureChatOpenAI(deployment_name=deployment, model_name=model, temperature=0, max_tokens=200, **openai_config)
    translating_prompt_template = """translate "{content}" into {target_language}:"""
    translating_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(translating_prompt_template), output_key="translated")

    # classifying_prompt_template = """
    # Determine if the following content is related to {topic}. If it is related, return "Y"; otherwise, return "N":
    # ---
    # {content}
    # """
    classifying_prompt_template = """
    judge the following content is weather relative with {topic} or not. return "Y" if it is relative, or return "N":
    ---
    {content}
    """
    classifying_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(classifying_prompt_template), output_key="relevance")

    sentence_analyzing_prompt_template = """
    analyze the following Japanese sentence and explain the used grammar and words using Chinese:
    ---
    {content}
    """
    sentence_analyzing_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(sentence_analyzing_prompt_template), output_key="analysis")

    question_answering_prompt_template = """
    analyze the following Japanese question and tell me which option is best for chosen answer and explain the reason using Chinese:
    ---
    {content}
    """
    question_answering_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(question_answering_prompt_template), output_key="answer")

    @classmethod
    def translate(cls, content: str, target_language: str):
        result: str = cls.translating_chain.run({
            "content": content,
            "target_language": target_language.capitalize(),
        })

        return result

    @classmethod
    def analyze_sentence(cls, content: str):
        result: str = cls.sentence_analyzing_chain.run({
            "content": content,
        })

        return result

    @classmethod
    def answer_question(cls, content: str):
        result: str = cls.question_answering_chain.run({
            "content": content,
        })

    @classmethod
    def judge_relevance(cls, content, topic="japanese learning"):
        result: str = cls.classifying_prompt_template.run({
            "content": content,
            "topic": topic,
        })

        return result == "Y"
