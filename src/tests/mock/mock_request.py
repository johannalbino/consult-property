import json


def get_mock():
    with open('src/tests/mock/resp.json', 'rb') as file:
        MOCK_REQUEST_API_EXTERNAL = json.loads(file.read())

    return MOCK_REQUEST_API_EXTERNAL


MOCK_REQUEST_API_EXTERNAL = get_mock()
