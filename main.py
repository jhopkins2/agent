import os
import argparse
from google import genai
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Coding Support")
    parser.add_argument("user_prompt", type=str, help="Provide a question or prompt to ask the agent for help")
    args = parser.parse_args()

    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

    if response.usage_metadata != None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    else:
        raise RuntimeError("No response from Gemini model")


if __name__ == "__main__":
    main()
