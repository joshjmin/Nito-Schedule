#HTSL Project

import json       
import urllib.parse
import boto3 #issue here
boto3.__version__
from botocore.client import Config

print(boto3.__version__)

# # Initialize AWS Bedrock client

session = boto3.session.Session()
region = session.region_name
bedrock_config = Config(connect_timeout=120, read_timeout=120, retries={'max_attempts': 0})
model_id = "anthropic.calude-3-sonnet-20240229-v2:0"
s3 = boto3.client('s3')
document_uri_1 = "s3://uofteventcreater1234/course.exam/"
document_uri_2 = "s3://uofteventcreater1234/rooms/"
kbId= '6KQKS5KQXG'

client = boto3.client(service_name = 'bedrock-agent-runtime', region_name=region, config=bedrock_config)  # Replace with your region
#region = "us-west2???"

def retrieveAndGenerate(input_text, sourceType, model_id, sourceChunk, region, document_s3_uri=None, data=None, identifier=None):
    model_arn = f'arn:aws:bedrock:{region}::foundation-model/{model_id}'

    return client.retrieve_and_generate(
        input={'text': input_text},
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId' : kbId,
                'modelArn': model_arn,
                
                'retrievalConfiguration': [
                    
                    {
                        "sourceChunk" : sourceChunk,
                        "sourceType": sourceType,
                        "s3Location": {
                            "uri": document_uri_1,
                            "uri": document_uri_2
                        }
                    }
                ]    
            }
            
        }
    )

response = retrieveAndGenerate(input_text="You are a uoft exam coordination bot. You are to look at all the rooms and courses and compare the avalibility and capacity. Generate a overall time table that list when all courses should happen and which room they are in. All course should last 2 hours consecutively and there should be an one hour break after that. Courses can happen at the same time as long as they are in different rooms. Look at all rooms and all courses. Rooms can be use multiple time throughout the day as long as there is no time conflict. All courses should only appear once in the timetable. ", sourceType="S3", model_id=model_id,  sourceChunk = "15" ,region=region)
generated_text = response['output']['text']
print(generated_text)
# # Input text for summarization
# input_text = """
# summary
# """

# # Invoke the foundation model for text summarization
# response = client.invoke_model( #ISSUE with invoke_model
#     modelId='anthropic-claude-v2',  # Replace with the appropriate foundation model ID
#     inputText=input_text,
# )

# # Print the summarized output
# print("Summarized Text:", response['outputText'])

# SHRUTI TESTING HERE - GPT prompt for "How do I access the buckets from AWS S3 into the VS code?"
# NOTES: all the code shows 
# Initialize the S3 client
#s3 = boto3.client('s3')

    # List all buckets
   # response = s3.list_buckets()
   # print("S3 Buckets:")
   # for bucket in response['Buckets']:
   #     print(f"  - {bucket['Name']}")

    # Access a specific bucket and list its contents
   # bucket_name = 'uofteventcreater1234'  # Replace with your bucket name
   # print(f"\nContents of bucket '{bucket_name}':")
#    # response = s3.list_objects_v2(Bucket=bucket_name)

#     if 'Contents' in response:
#         for obj in response['Contents']:
#             print(f"  - {obj['Key']} (Size: {obj['Size']} bytes) {obj['Key'].ext('name')}")
#             #print("Professor:", data['prof'])
#     else:
#         print("  The bucket is empty.")


# model: Claude 3 Sonnet v1
# # source chunks = 15
# prompt = "You are a uoft exam coordination bot. You are to look at all the rooms and courses and compare the avalibility and capacity. Generate a overall time table that list when all courses should happen and which room they are in. All course should last 2 hours consecutively and there should be an one hour break after that. Courses can happen at the same time as long as they are in different rooms. Look at all rooms and all courses. Rooms can be use multiple time throughout the day as long as there is no time conflict. All courses should only appear once in the timetable. "
