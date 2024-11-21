import copy
import requests
from prompt_data import generate_ins_prompt, generate_env_prompt, generate_clarify_prompt, generate_miss_ins_prompt
import sys
import os



def init_action_chat():
    operation_history = []
    system_prompt = "You are a helpful office assistant."
    operation_history.append(["system", [{"type": "text", "text": system_prompt}]])
    return operation_history
def init_clarify_chat():
    operation_history = []
    system_prompt = "You are an intelligent agent designed to interact with users to clarify and specify their requests. When given a user’s initial query and a specific detail that is missing, your task is to generate a natural, conversational question to obtain that specific missing information from the user. Your response should use coreference or omission to refer back to the initial query, minimizing direct repetition of its details."
    operation_history.append(["system", [{"type": "text", "text": system_prompt}]])
    return operation_history

def add_response(role, prompt, chat_history):
    new_chat_history = copy.deepcopy(chat_history)
    content = [
        {
            "type": "text",
            "text": prompt
        },
    ]
    new_chat_history.append([role, content])
    return new_chat_history

def inference_chat(chat, model, api_url, token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    data = {
        "model": model,
        "messages": [],
        "max_tokens": 2048,
        'temperature': 0.0,
        "seed": 1234
    }

    for role, content in chat:
        data["messages"].append({"role": role, "content": content})

    while True:
        try:
            res = requests.post(api_url, headers=headers, json=data)
            res_json = res.json()
            res_content = res_json['choices'][0]['message']['content']
        except:
            print("Network Error:")
            try:
                print(res.json())
            except:
                print("Request Failed")
        else:
            break

    return res_content




API_url = "https://api.openai-hk.com/v1/chat/completions"
token = "hk-x7r3vc100003489791121e73861680c3d17f2a2e074c5ae5"
output_data=''
prompt = generate_env_prompt()
chat_action = init_action_chat()
chat_action = add_response("user", prompt, chat_action)
output_env = inference_chat(chat_action, 'gpt-4o', API_url, token)
print(output_env)
output_data += output_env
prompt = generate_ins_prompt(output_env)
chat_action = init_action_chat()
chat_action = add_response("user", prompt, chat_action)
output_ins = inference_chat(chat_action, 'gpt-4o', API_url, token)
print(output_ins)
output_data += output_ins
prompt = generate_miss_ins_prompt(output_env,output_ins)
chat_action = init_action_chat()
chat_action = add_response("user", prompt, chat_action)
output_miss_ins = inference_chat(chat_action, 'gpt-4o', API_url, token)
print(output_miss_ins)
output_data += output_miss_ins
prompt = generate_clarify_prompt(output_env,output_miss_ins)
chat_action = init_clarify_chat()
chat_action = add_response("user", prompt, chat_action)
output_clar = inference_chat(chat_action, 'gpt-4o', API_url, token)
print(output_clar)
output_data += output_clar
fw = open("test.txt", 'w')
fw.write(output_data)



