import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.regression
class TestLogin:
    """Tests para la funcionalidad de login"""
    
    def test_open_browser(self, page):
        """TC001: Navegar hacia pagina Geek Store"""
        login_page = LoginPage(page)
        login_page.navigate()
        
        # Validate we're on products page
        assert "/index.php" in page.url
        print("TC001: Navegación completada")