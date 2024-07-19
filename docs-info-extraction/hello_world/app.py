import json
import re
import boto3
from botocore.exceptions import ClientError
from utils import extract_snippet_from_tags
from prompt import get_system_prompt, get_user_prompt


bedrock_client = boto3.client(service_name="bedrock-runtime")
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

inferenceConfig = {
    'maxTokens': 500,
    'temperature': 0.1,
    'topP': 0.8
}


system_message = [{
    'text': get_system_prompt()
}]


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    with open("Proforma. Personal Office six months.pdf", "rb") as file:
        pdf_bytes = file.read()
            
        message = {
            "role": "user",
            "content": [
                {
                    "text": get_user_prompt()
                },
                {

                    "document": {
                        "format": "pdf",
                        "name": "example",
                        "source": {
                            "bytes": pdf_bytes
                        } 
                    }
                }
            ]
        }
    messages = [message]

    try: 
        
        response = bedrock_client.converse(
            modelId = model_id,
            system = system_message,
            messages = messages
        )
        output_message = response.get('output', 
                                      None).get('message',
                                                None).get('content',
                                                                    None)[0].get('text',
                                                                              None)
        print(f"RAW MODEL OUTPUT: \n\n {output_message} \n\n")
        json_response = extract_snippet_from_tags(output_message)
        print(json_response)

        # return {
        #     "statusCode": 200,
        #     "body": json.dumps({
        #         "message": json_response,
        #     }, ensure_ascii=False),
        # }
    except ClientError as err:
        print(f"Error: {err}")




