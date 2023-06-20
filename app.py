from flask import Flask, request
import json
import boto3


app = Flask(__name__)

@app.route('/api/v1/generate_reply', methods=['POST'])
def generate_reply():
    endpoint_name = 'jumpstart-dft-hf-llm-falcon-40b-instruct-bf16'

    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=request.data)

    model_predictions = json.loads(response['Body'].read())
    generated_text = model_predictions[0]['generated_text']

    return generated_text
