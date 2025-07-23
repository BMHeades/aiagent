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




def main():
    client = genai.Client(api_key=api_key)

    # Check for argument
    if len(sys.argv) == 1:
        sys.exit(1)

        

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages)
    prompt_tokens = response.usage_metadata.prompt_token_count
    usage_tokens = response.usage_metadata.candidates_token_count

    # If --verbose
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {usage_tokens}\nResponse:")


    
    print(response.text)

    


if __name__ == "__main__":
    main()
