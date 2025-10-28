import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# CAMBIO CLAVE: Cambiar el scope de "module" a "function"
@pytest.fixture(scope="function") 
def driver():
    """Configura y cierra el WebDriver para CADA PRUEBA."""
    # (Usaremos la ruta relativa con la extensión .exe que funcionó antes)
    service = Service('./driver/chromedriver.exe') 
    
    # INICIA EL DRIVER (SETUP)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10) 
    driver.maximize_window()
    
    # 'yield' ES DONDE SE EJECUTA LA PRUEBA
    yield driver
    
    # CIERRA EL DRIVER (TEARDOWN) - Se ejecuta después de CADA PRUEBA
    driver.quit()