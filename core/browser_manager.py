import os
from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self):
        self.headless = os.getenv("HEADLESS", "true").lower() == "true"
        self.playwright = None
        self.browser = None

    def start(self):
        if not self.playwright:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(
                headless=self.headless,
                args=["--no-sandbox", "--disable-dev-shm-usage"]
            )

        context = self.browser.new_context()
        page = context.new_page()
        page._context = context   # guardar referencia
        return page

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()