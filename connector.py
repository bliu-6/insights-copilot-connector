from flask import request, Flask, jsonify
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

load_dotenv()

app = Flask(__name__)

@app.route('/AIDaxExpression', methods=['POST'])
def getAIDaxExpression():
    endpoint = os.getenv("ENDPOINT_URL")
    deployment = os.getenv("DEPLOYMENT_NAME")
    subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

    # Parse JSON request body
    data = request.get_json()

    body = data.get("body")

    # Initialize Azure OpenAI client with key-based authentication
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version="2025-01-01-preview",
    )

    # Prepare the chat prompt
    with open('AIDaxExpressionPrompt.txt', 'r') as file:
        template = file.read()

    # Replace placeholders with actual values
    chat_content = template.format(body=body)
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": chat_content
                }
            ]
        }
    ]

    # Include speech result if speech is enabled
    messages = chat_prompt

    # Generate the completion
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=800,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})

@app.route('/validateDaxExpression', methods=['POST'])
def validateDaxExpression():
    endpoint = os.getenv("ENDPOINT_URL")
    deployment = os.getenv("DEPLOYMENT_NAME")
    subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

    # Parse JSON request body
    data = request.get_json()

    body = data.get("body")

    # Initialize Azure OpenAI client with key-based authentication
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version="2025-01-01-preview",
    )

    # Prepare the chat prompt
    with open('validateDaxExpressionPrompt.txt', 'r') as file:
        template = file.read()

    # Replace placeholders with actual values
    chat_content = template.format(body=body)
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": chat_content
                }
            ]
        }
    ]

    # Include speech result if speech is enabled
    messages = chat_prompt

    # Generate the completion
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=800,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )

    response = completion.choices[0].message.content

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8090)

    