import os
import argparse
from google.genai import Client, types
from dotenv import load_dotenv
from prompts.system_prompt import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERATIONS

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    parser = argparse.ArgumentParser(description="Coding Support")
    parser.add_argument("user_prompt", type=str, help="Provide a question or prompt to ask the agent for help")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output of the coding agent")
    args = parser.parse_args()

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    client = Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    for i in range(MAX_ITERATIONS):
        try: 
            final_response_text = generate_content(client, messages, args.verbose)
            if final_response_text:
                print(final_response_text)
                return 0
        except Exception as e:
            print(f"Error in generate_content: {e}")

    print(f"Maximum Iterations {MAX_ITERATIONS} reached")


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(
                tools = [available_functions],
                system_instruction=system_prompt)
            )

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)
    
    function_result_response_list = []

    if not response.function_calls and response.text:
        return f"Response: {response.text}"

    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)

        if not function_call_result.parts:
            raise RuntimeError(f"Error: Malform function response")

        if not function_call_result.parts[0].function_response:
            raise RuntimeError(f"Error: No FunctionReponse object was returned")

        if not function_call_result.parts[0].function_response.response:
            raise RuntimeError(f"Error: No response was return in the FunctionResponse object")

        function_result_response_list.append(function_call_result.parts[0])
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

    messages.append(types.Content(role="user", parts=function_result_response_list))

if __name__ == "__main__":
    main()
