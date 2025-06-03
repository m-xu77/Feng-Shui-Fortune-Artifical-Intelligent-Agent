
from langchain.prompts import AIMessagePromptTemplate
from langchain.prompts import SystemMessagePromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatMessagePromptTemplate # customize the role and template

prompt = "May {subject} be with you!"

chat_message_prompt = ChatMessagePromptTemplate.from_template(role="Skywalker",template=prompt)
chat_message_prompt.format(subject="the Force")

