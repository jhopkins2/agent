import os
import argparse
from google import genai
from dotenv import load_dotenv
from prompts.system_prompt import system_prompt

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    parser = argparse.ArgumentParser(description="Coding Support")
    parser.add_argument("user_prompt", type=str, help="Provide a question or prompt to ask the agent for help")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output of the coding agent")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)
    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=args.user_prompt)])]
        
    response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=genai.types.GenerateContentConfig(system_instruction=system_prompt))

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
