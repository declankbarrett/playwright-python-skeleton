from playwright.sync_api import sync_playwright
from utils.helpers import check_status_code

expected_status = 201
data = {
    "name": "morpheus",
    "job": "leader"
}

def test_post(playwright: sync_playwright):
  context = playwright.request.new_context()
  response = context.post('https://reqres.in/api/users', data = data)


# Documentation advise for response -> https://playwright.dev/python/docs/api/class-apiresponse
  assert response.ok
  status = response.status
  check_status_code(status, expected_status)
  assert response.json()['name'] == data["name"]
  assert response.json()['job'] == data["job"]
