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

    grp_id = {} #This dictionary will contain and group users by their respective IDs

    for activities in act_res_json['activities']:
        user_id = activities['user_id']

        if user_id not in grp_id:
            grp_id[user_id] = [] #Creates a new entry-list for this user id
            print('New-List') #Check for sucess
        
        grp_id[user_id].append(activities)

    print(grp_id) #Check for sucess

    for user_id in grp_id:
        act_id = [] #Creates list for activities IDs
        for activities in grp_id[user_id]:
            act_id.append(activities['id']) #Appends the activities to the list
        grp_id[user_id] = act_id


