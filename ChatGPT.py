from openai import OpenAI #for chatGPT
import os #To get enviroment elements
import requests
import time
import openai
from openai import OpenAIError, APIConnectionError
from proxy import *


secret_key = openai.api_key = str(os.getenv("OPENAI_SECRET_KEY"))


chat_completion = openai.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)