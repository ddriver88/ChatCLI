import openai
import prompt_toolkit
import time

conversation_history = []

# Set up OpenAI API credentials
openai.api_key = "OPENAI_API_KEY_HERE"

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
initial_prompt = "ChatGPT: How can I help?\n\nUser: "
followup_prompt = "ChatGPT: Is there anything else I can help with?\n\nUser: "

# Define exit command
exit_command = "exit"

# Start the REPL loop
while True:
    # Get input from user
    user_input = prompt_toolkit.prompt(initial_prompt)

    # Check if user wants to exit
    if user_input.lower() == exit_command:
        print("\n\nSee you soon!")
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        break

    # Add user input to conversation history
    conversation_history.append(user_input)

    # Generate response from OpenAI API using conversation history
    prompt = "\n".join(conversation_history)
    response = generate_response(prompt)

    # Add response to conversation history
    conversation_history.append(response)

    # Print response
    print("ChatGPT: "+response+"\n\n")
    initial_prompt = followup_prompt
