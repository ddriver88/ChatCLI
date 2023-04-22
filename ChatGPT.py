import openai
import prompt_toolkit
import time

# Set up OpenAI API credentials
openai.api_key = "KEY_HERE"

# Define function to generate response from OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Define initial prompt
initial_prompt = "How can I help?\n"
followup_prompt = "Is there anything else I can help with? "

# Define exit command
exit_command = "exit"

# Start the REPL loop
while True:
    # Get input from user
    user_input = prompt_toolkit.prompt(initial_prompt)

    # Check if user wants to exit
    if user_input.lower() == exit_command:
        print("See you soon!")
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        break

    # Generate response from OpenAI API
    prompt = f"{user_input.strip()}\n"
    response = generate_response(prompt)

    # Print response
    print(response)
    initial_prompt = followup_prompt
