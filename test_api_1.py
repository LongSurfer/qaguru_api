import requests
from requests import Response

from pprint import pprint

def test_get_users():
    result: Response = requests.get('https://reqres.in/api/users', params={'page': 2})
    # print(response.status_code)
    # pprint(response.json())
    assert result.status_code == 200
    assert result.json()['page'] == 2

def test_create_user():
    name = "morpheus_007"
    job = "leader"

    result = requests.post(
        url='https://reqres.in/api/users',
        json={"name": name, "job": job}
    )
    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job

