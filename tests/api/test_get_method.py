# See documentation here for further examples -> https://playwright.dev/python/docs/api/class-apirequestcontext
from playwright.sync_api import sync_playwright
from utils.helpers import check_status_code

expected_status = 200

def test_get(playwright: sync_playwright):
  context = playwright.request.new_context()
  response = context.get('https://reqres.in/api/users?page=2')

  assert response.ok
  status = response.status
  check_status_code(status, expected_status)


  
  