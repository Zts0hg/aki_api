import os

from langchain import LLMChain, PromptTemplate
from langchain_openai import AzureChatOpenAI

# deployment = "text_model"
# model = "gpt-35-turbo"

# openai_config = {
#     "openai_api_type": "azure",
#     # "openai_api_base": "https://ai-test-for-aki.openai.azure.com/",
#     "openai_api_base": "https://shibainu.openai.azure.com/",
#     "openai_api_version": "2023-07-01-preview",
#     "openai_api_key": "f7d7d95881d440dda5f275c5574f04d0",
#     # "openai_api_key": os.environ.get("AKI_API_OPENAI_API_KEY"),
# }
# openai.api_type = openai_config["openai_api_type"]
# openai.api_base = openai_config["openai_api_base"]
# openai.api_version = openai_config["openai_api_version"]
# openai.api_key = openai_config["openai_api_key"]
# print(openai_config)
class Assistant:
    llm = AzureChatOpenAI(
        azure_endpoint="https://shibainu.openai.azure.com/",
        api_key=os.environ.get("AKI_API_OPENAI_API_KEY"),
        azure_deployment="gpt-4o",
        api_version="2024-02-15-preview",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    translating_prompt_template = """translate "{content}" into {target_language}:"""
    translating_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(translating_prompt_template),
        output_key="translated",
    )

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
    classifying_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(classifying_prompt_template),
        output_key="relevance",
    )

    sentence_analyzing_prompt_template = """
    analyze the following Japanese sentence and using Chinese to explain the used grammar and words:
    requirement 1: you should use Chinese to reply.
    requirement 2: the reply should be Markdown content but not a code snippet.
    ---
    {content}
    """
    sentence_analyzing_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(sentence_analyzing_prompt_template),
        output_key="analysis",
    )

    question_answering_prompt_template = """
    analyze the following Japanese question and tell me which option is best for chosen answer and explain the reason using Chinese:
    (notice: the lowercase alphabet, such as a, b, c, or digit in the brackets is just a sequence mark of options, not a part of option)
    requirement 1: you should use Chinese to reply.
    requirement 2: you can explain why the option is best or other option is not best from grammar correctness, meaning, context or other aspects.
    requirement 3: the reply should be Markdown content but not a code snippet.
    ---
    {content}
    """
    question_answering_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(question_answering_prompt_template),
        output_key="answer",
    )

    @classmethod
    def translate(cls, content: str, target_language: str):
        result: str = cls.translating_chain.run(
            {
                "content": content,
                "target_language": target_language.capitalize(),
            }
        )

        return result

    @classmethod
    def analyze_sentence(cls, content: str):
        result: str = cls.sentence_analyzing_chain.run(
            {
                "content": content,
            }
        )

        return result

    @classmethod
    def answer_question(cls, content: str):
        result: str = cls.question_answering_chain.run(
            {
                "content": content,
            }
        )
        return result

    @classmethod
    def judge_relevance(cls, content, topic="japanese learning"):
        result: str = cls.classifying_prompt_template.run(
            {
                "content": content,
                "topic": topic,
            }
        )

        return result == "Y"


if __name__ == "__main__":
    content = "ここに車を止められるのは、許可をもらっている人（a だけ b に限り）です。"
    print(Assistant.answer_question(content=content))
