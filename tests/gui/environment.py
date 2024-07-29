from playwright.sync_api import sync_playwright
import os
from allure_commons.types import AttachmentType
import allure

def before_all(context):
    context.playwright = sync_playwright().start()

def before_feature(context, feature):
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.context.clear_cookies()

def after_feature(context, feature):
    context.page.close()
    context.browser.close()
    
def after_step(context, step):
    if step.status == "failed":
        screenshot_dir = "reports/allure-results/screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{step.name}.png")
        context.page.screenshot(path=screenshot_path)
        # Attach screenshot to Allure report
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=AttachmentType.PNG)

def after_all(context):
    context.playwright.stop()