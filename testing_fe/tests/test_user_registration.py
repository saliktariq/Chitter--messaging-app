import pytest
import requests


@pytest.mark.parametrize("username, password, first_name, last_name", [
    ("olga", "olga123", "Olga", "Kiev"),
    ("nick", "nick123", "Nick", "English"),
    ("mary", "mary123", "Mary", "Johns"),
    ("nester", "nester123", "Nester", "Smith"),
])
def test_user_registration(users, username, password, first_name, last_name):
    user_data = users[username]
    assert user_data["password"] == password
    assert user_data["first_name"] == first_name
    assert user_data["last_name"] == last_name
    assert "access_token" in user_data
    assert "refresh_token" in user_data


@pytest.mark.parametrize("username, password", [
    ("olga", "olga123"),
    ("nick", "nick123"),
    ("mary", "mary123"),
    ("nester", "nester123"),
])
def test_request_new_token(api_client, username, password):
    response = api_client.request_token(username, password)
    print("test_request_new_token : ", response)
    assert "access_token" in response
    assert "refresh_token" in response


def test_unauthorized_request(api_client, users):
    message_URL = f"{api_client.base_url}/v1/message/"
    response = requests.get(message_URL)
    assert response.status_code == 401  # Unauthorized
