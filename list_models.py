import boto3 
bedrock = boto3.client(service_name='bedrock')

result = bedrock.list_foundation_models()
print(result)
