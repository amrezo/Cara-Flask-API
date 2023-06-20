from flask import Flask, request
import json
import boto3


app = Flask(__name__)

@app.route('/api/v1/generate_reply', methods=['POST'])
def generate_reply():
    endpoint_name = 'jumpstart-dft-hf-llm-falcon-40b-instruct-bf16'

    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=json.dumps(request.data).encode('utf-8'))

    return response
