import os
from openai import OpenAI

import logging

logging.basicConfig(level=logging.INFO)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logging.error("OPENAI_API_KEY environment variable is not set")
    raise EnvironmentError("Missing OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def chat_completion(prompt: str) -> str:
    """
    Sends a prompt to the new v1 Chat Completions API and returns the assistant's reply.
    """
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
        )
        status = getattr(resp, "http_response", None)
        if status:
            logging.info(f"OpenAI API response status code: {status.status_code}")
        else:
            logging.info("OpenAI API response received")
    except Exception as e:
        logging.error(f"Error calling OpenAI API: {e}")
        raise
    return resp.choices[0].message.content
