from prompt_templates import RESPONSE_POOL
from transformers import pipeline
import random

generator = pipeline("text2text-generation", model="google/flan-t5-small")

def get_bot_response(user_input):
    tone = random.choice(RESPONSE_POOL)
    prompt = f"{tone}\nUser: {user_input}\nResponse:"
    result = generator(prompt, max_length=200)[0]["generated_text"]
    return result.replace(prompt, "").strip()