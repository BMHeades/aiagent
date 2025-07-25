# for env
import os
from dotenv import load_dotenv

# arguments
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Google
from google import genai
from google.genai import types # types like messages

# config / settings
from config import *

# function schemas
from function_schemas import schema_get_files_info


def main():
    client = genai.Client(api_key=api_key)

    # Check for argument
    if len(sys.argv) == 1:
        sys.exit(1)

        

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # tools for ai
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=SYSTEM_PROMPT)
        )
    prompt_tokens = response.usage_metadata.prompt_token_count
    usage_tokens = response.usage_metadata.candidates_token_count

    # If --verbose
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {usage_tokens}\nResponse:")


    
    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    


if __name__ == "__main__":
    main()
