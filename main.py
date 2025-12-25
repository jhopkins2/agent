import os
import argparse
from google.genai import Client, types
from dotenv import load_dotenv
from prompts.system_prompt import system_prompt
from call_function import available_functions

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    parser = argparse.ArgumentParser(description="Coding Support")
    parser.add_argument("user_prompt", type=str, help="Provide a question or prompt to ask the agent for help")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output of the coding agent")
    args = parser.parse_args()

    client = Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
        
    response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(
                tools = [available_functions],
                system_instruction=system_prompt)
            )

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        if response.text:
            print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
