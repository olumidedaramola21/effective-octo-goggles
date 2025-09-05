response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,

    # Enter your prompt
    messages=[{
        "role":"user",
        "content": "hi, how are you doing"
    }]
)

print(response.choices[0].message.content)


# making a request
from openai import OpenAI
client = OpenAI(api_key="api_key")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,

    # Enter your prompt
    messages=[{
        "role":"user",
        "content": "hi, how are you doing"
    }]
)

print(response)


# Text editing
prompt = """ 
Update names to Maarten, pronous to he/him, and job title to Senior Content Developer in the following text:

Joanne is a Content Developer at Datacamp. Her favorite programming language is R, which she uses for statistical analyses.

"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
    message=[{
        "role": "user",
        "content": prompt
    }]
)

print(response.choices[0].message.content)


# Calculating the cost

# Define price per token
input_token_price = 0.15/1_000_000
output_token_price = 0.6/1_000_000
# Extract token usage
input_token = response.usage.prompt_tokens
output_token = max_completion_tokens
# Calculate cost
cost = (input_token * input_token_price + output_token * output_token_price)
