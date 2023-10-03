import requests as re
import json

username = "samriddha.biswas@wonderbotz.com"
password = "SaminClan112@"

def func(user1: str, password1: str):
    url1 = "https://community.cloud.automationanywhere.digital/v1/authentication"
    params1 = {'username':f'{user1}' , 'password':f'{password1}'}
    response = re.post(url1, json=params1)
    dict_var = json.loads(response.text)
    if (response.status_code == 204) or (response.status_code == 201) or (response.status_code == 200) :
        return dict_var['token']
    else:
        return None
    
