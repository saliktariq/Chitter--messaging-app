import pytest


@pytest.mark.parametrize("username, message_data", [
    ("olga", {
        "topic": [{"topic_name": "T"}],
        "title": "Olga's first message in Technology",
        "message": "This is Olga's first message in the Tech topic.",
        "expiry_in_seconds": 300
    }),
    ("nick", {
        "topic": [{"topic_name": "T"}],
        "title": "Nick's first message in Technology",
        "message": "This is Nick's first message in the Tech topic.",
        "expiry_in_seconds": 300
    }),
    ("mary", {
        "topic": [{"topic_name": "T"}],
        "title": "Mary's first message in Technology",
        "message": "This is Mary's first message in the Tech topic.",
        "expiry_in_seconds": 300
    }),
])
def test_post_messages(api_client, users, username, message_data):
    access_token = users[username]['access_token']
    response = api_client.post_message(access_token, message_data)
    assert response.status_code == 200
    print("The response: ", response)

    # assert the response from the api call
