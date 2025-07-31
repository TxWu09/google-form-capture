from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import requests
import os

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")


def generate_summary(form_data):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Please extract information from the form \n{text}"
    )
    llm = OpenAI(temperature=0.3, api_key=OPENAI_KEY)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(form_data)


def post_to_slack(text):
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {SLACK_TOKEN}"}
    data = {
        "channel": "form-submissions",
        "text": f" :\n{text}"
    }
    requests.post(url, headers=headers, json=data)

def process_form_submission(form_data):
    summary = generate_summary(str(form_data))
    post_to_slack(summary)