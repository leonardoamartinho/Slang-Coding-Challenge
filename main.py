import requests
import json

url_get = "https://api.slangapp.com/challenges/v1/activities"
header = {'Content-Type': 'application/json', 'Authorization': 'Basic MTQxOjVGZHZTamV1V01MQ0tZcFRySk9TemQ1ZHVKbjdhVm9salNTZmlGUXp6Qk09'}

activities_response = requests.get(url_get, headers = header)
print(activities_response.url) #confirms url get

if(activities_response.status_code == 200):
    print('Yes!') #Check for sucess in retrieving the endpoint
    act_res_json = json.loads(activities_response.text) #This will contain the list of "activities"
    print(act_res_json) #Check for sucess

    grp_id = {} #This will contain and group users by their respective IDs

    for act in act_res_json:
        user_id = act_res_json[act]

        if user_id not in grp_id:
            grp_id[user_id] = [] #Creates a new entry-list for this user id
            print('New-List') #Check for sucess
        
        grp_id[user_id].append(act)

    print(grp_id) #Check for sucess


