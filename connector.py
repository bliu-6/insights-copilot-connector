from flask import Flask, jsonify
import os
import base64
from openai import AzureOpenAI

app = Flask(__name__)

@app.route('/AIDaxExpression', methods=['GET'])
def getAIDaxExpression():
    endpoint = os.getenv("ENDPOINT_URL")
    deployment = os.getenv("DEPLOYMENT_NAME")
    subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

    # Initialize Azure OpenAI client with key-based authentication
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version="2025-01-01-preview",
    )

    # Prepare the chat prompt
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are an AI assistant that helps people find information."
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

    return completion.to_json()

@app.route('/validateDaxExpression', methods=['GET'])
def validateDaxExpression():
    return jsonify({'status': 'Server is running smoothly'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8090)

    