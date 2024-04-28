import os
from langchain_aws import ChatBedrock
import requests


MODEL_ID_LLAMA =  'meta.llama2-70b-chat-v1'
MODEL_ID_CLAUDE = 'anthropic.claude-3-sonnet-20240229-v1:0'
MODEL_ID_CLAUDE_V2 = 'anthropic.claude-v2'

AWS_PROFILE = 'default'

MODEL_ID = MODEL_ID_CLAUDE_V2

API_ENDPOINT = "https://46m6oqzgq0.execute-api.us-east-1.amazonaws.com/dev"
USER_INPUT = "please explain the effect of patent law in Italy?"

# Function to interact with the API
def call_api(user_prompt):
   
    data = {"prompt": user_prompt}
    print (data)
    response = requests.get(API_ENDPOINT, params=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Return message is> ")
        print(response.status_code)


# Function to integrate API response with LLM
def process_prompt_through_llm(user_prompt):
   
    api_response = call_api(user_prompt)  
    
    # Call the API with the user prompt
    # if 'text' in api_response:  # Check if the response contains text data
 
    print("API Response:", api_response)
    return api_response
    

llm_output = process_prompt_through_llm(USER_INPUT)
print(llm_output)
