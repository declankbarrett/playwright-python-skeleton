from playwright.sync_api import sync_playwright
from utils.helpers import check_status_code

expected_status = 200
data = {
    "name": "morpheus",
    "job": "zion resident"
}

def test_patch (playwright: sync_playwright):
  context = playwright.request.new_context()
  response = context.patch('https://reqres.in/api/users/2', data = data)


#Documentation advise for response -> https://playwright.dev/python/docs/api/class-apiresponse
  assert response.ok
  status = response.status
  check_status_code(status, expected_status)
  assert response.json()['name'] == data["name"]
  assert response.json()['job'] == data["job"]
