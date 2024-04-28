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
def call_api(user_prompt,apiEndpoint):
   
    data = {"prompt": user_prompt}
    #print (data)

    response = requests.get(apiEndpoint, params=data)
    if response.status_code == 200:
        #print(response.json())
        return response.json()
    else:
        print(response.status_code)


def getBedrockReponseThroughAPI(user_prompt):
   
    api_response = call_api(user_prompt,API_ENDPOINT) 

    try:
        api_response = call_api(user_prompt,API_ENDPOINT) 
        # Extract text, handle case where 'text' key might not exist
        return api_response.get('body', 'Nothing was found')
    except requests.RequestException as e:
        return f"An error occurred: {str(e)}"
    

# llm_output = getBedrockReponseThroughAPI(USER_INPUT)
# print(llm_output)
