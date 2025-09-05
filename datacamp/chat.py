client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]
user_msgs = ["Explain what pi is", "Summarize this in two bullet points"]

for q in user_msgs:
    print("User: ", q)

    # create a user dict from the q and append it to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict) 

# Send the chat messages to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_completion_tokens=100
)

# Extract the assistant message from the response
assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}

# Add assistant_dict to the messages dictionary
messages.append(assistant_dict)
print(messages)



