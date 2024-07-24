from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()

def before_feature(context, feature):
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.context.clear_cookies()

def after_feature(context, feature):
    context.page.close()
    context.browser.close()

def after_all(context):
    context.playwright.stop()