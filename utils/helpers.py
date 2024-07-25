
   
def check_status_code(actual_status, expected_status):
  assert actual_status == expected_status, (
              f"Expected status code to be '{expected_status}' but got '{actual_status}'"
          )
