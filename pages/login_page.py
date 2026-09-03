from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object para la página de login de GeekStore"""
    
    '''USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"'''
    
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://testing.geekqa.net/public_html/public/index.php"
    
    def navigate(self):
        print("Navegando a GeekStore...")
        self.go_to(self.url)
        print("Navegación completada")
    
    def login(self, username: str, password: str):
        print(f"Haciendo login con: {username}")
        self.fill(self.USERNAME_INPUT, username)
        print("Username ingresado")
        
        self.fill(self.PASSWORD_INPUT, password)
        print("Password ingresado")
        
        self.click(self.LOGIN_BUTTON)
        print("Click en Login ejecutado")
    
    def get_error_message(self) -> str:
        """Returna el mensaje de error si el login falla"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_login_successful(self) -> bool:
        """Verifies successful login"""
        print("Verificando login exitoso...")
        result = "/index.php" in self.page.url
        print(f"URL actual: {self.page.url}")
        print(f"Login exitoso: {result}")
        return result