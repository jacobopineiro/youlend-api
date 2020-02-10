import unittest
import requests
import json
import jsonpath


class TestAPI(unittest.TestCase):
    def test_post_user(self):
        # (CREATE) creates user with name and job and asserts response code and name:
        url = 'https://reqres.in/api/users'
        file = open('json_resources/post_example_json.json', 'r')
        json_input = file.read()

        request_json = json.loads(json_input)
        response = requests.post(url, request_json)

        # Assert response code
        assert response.status_code == 201
        response_json = json.loads(response.text)

        name = jsonpath.jsonpath(response_json, 'name')
        # Assert name from the user we created:
        assert name[0] == 'Jacobo'

    def test_get_user(self):
        # (READ) gets user by id and asserts response code and id:
        url = 'https://reqres.in/api/users/2'
        response = requests.get(url)
        # Assert response code = 200
        assert response.status_code == 200
        json_response = json.loads(response.text)
        data = jsonpath.jsonpath(json_response, 'data')
        # Assert user id = 2
        assert data[0]['id'] == 2

    def test_put_user(self):
        # (UPDATE) updates user with name and job and asserts response code and name:
        url = 'https://reqres.in/api/users/2'
        file = open('json_resources/put_example_json.json', 'r')
        json_input = file.read()

        request_json = json.loads(json_input)
        response = requests.put(url, request_json)

        # Assert response code
        assert response.status_code == 200
        response_json = json.loads(response.text)

        name = jsonpath.jsonpath(response_json, 'name')
        # Assert name from the user we created:
        assert name[0] == 'Jacobo P'

    def test_delete_user(self):
        # (DELETE) deletes user by id and asserts response code:
        url = 'https://reqres.in/api/users/2'
        response = requests.delete(url)
        assert response.status_code == 204


if __name__ == '__main__':
    unittest.main()
