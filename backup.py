
import requests
import mysql.connector

def registerNewUser(username, password, firstname, lastname):
    import requests
    url = "http://13.40.180.161:8000/authentication/register/"
    userObject = {
        'username': username,
        'password': password,
        'first_name': firstname,
        'last_name': lastname
    }
    userRegistrationResponse = requests.post(url, data=userObject)
    serverResponse = userRegistrationResponse.json()
    if (serverResponse is not None):
        print(serverResponse)
        return serverResponse
    else:
        print("Error! Unable to register user")
backup_user = registerNewUser("backup", "backup123", "Back", "Up")

# Entering dummy data to database
message_URL = 'http://13.40.180.161:8000/v1/message/'
access_token = backup_user['access_token']
headers = {'Authorization': 'Bearer ' + str(access_token)}
dataset = {

    "topic": [
        {

            "topic_name": "T"
        }
    ],
    "title": "First message",
    "message": "This is first message in the Tech topic.",
    'expiry_in_seconds': 300

}

dummy_request_to_post = requests.post(message_URL, headers=headers, json=dataset)

dataset = {

    "topic": [
        {

            "topic_name": "T"
        }
    ],
    "title": "Second message",
    "message": "This is second message in the Tech topic.",
    'expiry_in_seconds': 300

}
dummy_request_to_post = requests.post(message_URL, headers=headers, json=dataset)

dataset = {

    "topic": [
        {

            "topic_name": "T"
        }
    ],
    "title": "Third message",
    "message": "This is third message in the Tech topic.",
    'expiry_in_seconds': 300

}
dummy_request_to_post = requests.post(message_URL, headers=headers, json=dataset)

dataset = {

    "topic": [
        {

            "topic_name": "T"
        }
    ],
    "title": "Fourth message",
    "message": "This is fourth message in the Tech topic.",
    'expiry_in_seconds': 300

}
dummy_request_to_post = requests.post(message_URL, headers=headers, json=dataset)

dataset = {

    "topic": [
        {

            "topic_name": "T"
        }
    ],
    "title": "Fifth message",
    "message": "This is fifth message in the Tech topic.",
    'expiry_in_seconds': 300

}
dummy_request_to_post = requests.post(message_URL, headers=headers, json=dataset)

# Fetching the data back from server

import requests

tech_posts_URL = 'http://13.40.180.161:8000/v1/messagebytopic/T/'
access_token = backup_user['access_token']
headers = {'Authorization': 'Bearer ' + str(access_token)}

_request = requests.get(tech_posts_URL, headers=headers)

print('----------FULL DATASET RECEIVED--------------------')
print(_request.json())
print('---------------------------------------------------')
post_number = 0
for request in _request.json():
    post_number = post_number + 1
    print('Post number : ' + str(post_number))
    print('Post by : ' + str(request['username']))
    print('Topic : ' + str(request['topic'][0]['topic_name']))
    print('Title : ' + str(request['title']))
    print('Message : ' + str(request['message']))



# establish connection to MySQL database
cnx = mysql.connector.connect(host='localhost', database='chitter', user='root', password='password123')

# create a cursor object
cursor = cnx.cursor()

# iterate over each request in the JSON data
for request in _request.json():
    post_number += 1
    username = request['username']
    topic = request['topic'][0]['topic_name']
    title = request['title']
    message = request['message']

    # insert the data into the "tweet" table
    query = "INSERT INTO tweet (post_number, username, topic, title, message) VALUES (%s, %s, %s, %s, %s)"
    values = (post_number, username, topic, title, message)
    cursor.execute(query, values)
    cnx.commit()

    print('Post number : ' + str(post_number))
    print('Post by : ' + str(username))
    print('Topic : ' + str(topic))
    print('Title : ' + str(title))
    print('Message : ' + str(message))

# close the cursor and connection
cursor.close()
cnx.close()

