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

    for act in act_res_json['activities']:
        user_id = act['user_id']

        if user_id not in grp_id:
            grp_id[user_id] = [] #Creates a new entry-list for this user id
            print('New-List') #Check for sucess
        
        grp_id[user_id].append(act)

    print(grp_id) #Check for sucess

    for user_id in grp_id:
        acts_id = [] #Creates list for activities IDs
        for act in grp_id[user_id]:
            acts_id.append(act['id']) #Appends the activities to the list
        grp_id[user_id] = acts_id
    
    grpid_actsid = {} #This Dictionary will contain and group activities by their respective IDs

    for user_id in grp_id:
        grpid_actsid[user_id] = {}
        
        for act_id in grp_id[user_id]:
            grpid_actsid[user_id][act_id] = {}

            for acts in act_res_json['activities']:
                if acts['id'] == act_id:
                    grpid_actsid[user_id][act_id] = acts
                    print("Added") #Check for sucess

    for user_id in grpid_actsid:
        acts_id = [] #Creates new list for activities IDs

        for act_id in grpid_actsid[user_id]:
            acts_id.append(act_id) #Appends activities to new list

        grpid_actsid[user_id]['acts_id'] = acts_id #Inserting IDs
    
    print(grpid_actsid) #Check for sucess


