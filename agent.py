import os
from dotenv import load_dotenv
from openai import OpenAI
from task import PROMPT

# Load API Key
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL = "openai/gpt-4o-mini"


def explain_code(code):
    """Send code to OpenRouter AI and get explanation."""

    prompt = PROMPT.format(code)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful Python programming tutor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content