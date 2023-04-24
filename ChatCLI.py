import openai
import prompt_toolkit
import time
from collections import deque

# Set up OpenAI API credentials
openai.api_key = "OPENAI_API_KEY_HERE"
openai.api_base = "https://api.openai.com/v1/chat"

# Define function to generate response from OpenAI API
def generate_response(prompt):
    # Convert conversation history to a list of message dictionaries
    message_list = [{'role': 'system', 'content': 'ChatGPT: How can I help?'}]
    for i, message in enumerate(prompt.split('\n')):
        role = 'user' if i % 2 == 1 else 'assistant'
        message_list.append({'role': role, 'content': message})

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=message_list,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
        stream=False,
    )

    message = response.choices[0].message['content'].strip()
    return message




# Define initial prompt
initial_prompt = "ChatGPT: How can I help?\n\nUser: "
followup_prompt = "ChatGPT: Is there anything else I can help with?\n\nUser: "

# Define exit command
exit_command = "exit"

# Define maximum conversation history length
max_history_length = 10

# Initialize deque for conversation history
conversation_history = deque(maxlen=max_history_length)

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
