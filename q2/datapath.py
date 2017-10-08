import json
from mongokit import *

'''
    General:
    --------
    use mongokit for input validation
    use pyton-firebase
    
    
    flow:
        - convert each input to converted_input
        - store converted_input to mongoDB (don't forget to use mongokit for validating input)
            * if input.uuid already exist in database, update incident and replace flow_type with 'update_incident'
        - store converted_input to firebase using firebase convention (incident-firebase) - no input validation needed    


    msg -> sys_msg rules:
    ---------------------
    1. all messages city origin is Las Vegas
    2. type: 
        ACCIDENT -> crash
        ALL_OTHER -> incident
    3. subtype:
        if type == crash:
            ACCIDENT_MAJOR -> major
            ACCIDENT_MINOR -> minor
        else:
            * -> minor
    4. location: use lat, lng instead of x, y
    5. if reliability bigger than 6 (exclusive) -> accurate is true
    6. if confidence * reliability > 20 -> accurate is true
    8. id is uuid
    9. timestamp is seconds


    store to firebase:
    ------------------
    1. color: 'red' for major incidents otherwise 'orange'
    2. title: "what happened"
    3. subtitle: street
    4. time: timestamp in milis

    * use firebase-python


'''



def sys_convert(msg):
    pass




with open('./input.json') as json_data:
    msg = json.load(json_data)
    print(msg)

    sys_msg = sys_convert(msg)










