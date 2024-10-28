import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test the API by making a simple request using the free model gpt-3.5-turbo
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use the free model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello!"}
    ]
)

# Print the response
print(response['choices'][0]['message']['content'])
