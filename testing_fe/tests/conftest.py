import json

import pytest
import requests

BASE_URL = "http://localhost:8000"


@pytest.fixture(scope='session')
def api_client():
    class APIClient:
        def __init__(self):
            self.base_url = BASE_URL

        def register_user(self, username, password, first_name, last_name):
            url = f"{self.base_url}/authentication/register/"
            user_object = {
                "username": username,
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
            }
            user_registration_response = requests.post(url, data=user_object)
            return user_registration_response.json()

        def request_token(self, username, password):
            url = f"{self.base_url}/authentication/token/"
            request_object = {
                "username": username,
                "password": password,
            }
            requested_token = requests.post(url, data=request_object)
            return requested_token.json()

        def post_message(self, access_token, message_data):
            url = f"{self.base_url}/v1/message/"
            headers = {'Authorization': f"Bearer {str(access_token)}"}
            message_post_response = requests.post(url, json=message_data, headers=headers)
            print("\nTEST FOR POSTING A MESSAGE :")
            print(json.dumps(message_post_response.json(), indent=4))
            return message_post_response

    return APIClient()


@pytest.fixture(scope='session')
def users(api_client):
    users_data = {
        "olga": {"username": "olga", "password": "olga123", "first_name": "Olga", "last_name": "Kiev"},
        "nick": {"username": "nick", "password": "nick123", "first_name": "Nick", "last_name": "English"},
        "mary": {"username": "mary", "password": "mary123", "first_name": "Mary", "last_name": "Johns"},
        "nester": {"username": "nester", "password": "nester123", "first_name": "Nester", "last_name": "Smith"},
    }

    for user_data in users_data.values():
        username = user_data["username"]
        password = user_data["password"]
        first_name = user_data["first_name"]
        last_name = user_data["last_name"]

        user_data.update(api_client.register_user(username, password, first_name, last_name))
        if "a user with that username already exists." in str(user_data.get("username", "")).lower():
            user_data.update(api_client.request_token(username, password))

    return users_data


@pytest.fixture(scope="session", autouse=True)
def setup_topics(api_client, users):
    access_token = users["olga"]["access_token"]
    topic_url = f"{BASE_URL}/v1/topic/"
    headers = {"Authorization": f"Bearer {access_token}"}

    topics_data = [{"topic_name": "P"}, {"topic_name": "H"}, {"topic_name": "S"}, {"topic_name": "T"}]
    topic_names = [topic["topic_name"] for topic in topics_data]

    for topic in topics_data:
        response = requests.post(topic_url, headers=headers, data=topic)
        print("TOPIC POST RESPONSE : ", response)
        if response.status_code == 500:
            # If 500 error occurs, retrieve all topics and check if they match the expected topics
            get_response = requests.get(topic_url, headers=headers)
            assert get_response.status_code == 200
            retrieved_topics = get_response.json()
            retrieved_topic_names = [topic["topic_name"] for topic in retrieved_topics]
            assert set(topic_names) == set(retrieved_topic_names)
            break
