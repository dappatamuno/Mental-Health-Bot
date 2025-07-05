from prompt_templates import BASE_PROMPT
from transformers import pipeline

# Simple pipeline for generating responses
generator = pipeline("text2text-generation", model="google/flan-t5-small")

prompt_type = "default"  # or "motivational", "grounding_support", etc.
base_prompt = BASE_PROMPTS[prompt_type]

def get_bot_response(user_input):
    full_prompt = BASE_PROMPT + "\nUser: " + user_input + "\nMindEase:"
    result = generator(full_prompt, max_length=200)[0]["generated_text"]
    return result.replace(full_prompt, "").strip()
