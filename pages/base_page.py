from playwright.sync_api import Page


class BasePage:
    """Pagina base para todos los objetos de página."""
    
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 5000
    
    def go_to(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")
    
    def get_title(self) -> str:
        return self.page.title()
    
    def click(self, selector: str):
        self.page.click(selector, timeout=self.timeout)
    
    def fill(self, selector: str, text: str):
        self.page.fill(selector, text, timeout=self.timeout)
    
    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)
    
    def is_visible(self, selector: str) -> bool:
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=self.timeout)
            return True
        except:
            return False