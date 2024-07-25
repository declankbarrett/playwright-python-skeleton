from playwright.sync_api import sync_playwright
from utils.helpers import check_status_code

expected_status = 204

def test_get(playwright: sync_playwright):
  context = playwright.request.new_context()
  response = context.delete('https://reqres.in/api/users/2')


#Documentation advise for response -> https://playwright.dev/python/docs/api/class-apiresponse
  assert response.ok
  status = response.status
  check_status_code(status, expected_status)
 