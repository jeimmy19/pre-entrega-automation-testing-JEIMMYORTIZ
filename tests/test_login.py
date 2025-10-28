from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL y Credenciales Fijas
LOGIN_URL = "https://www.saucedemo.com/"
INVENTORY_URL_PART = "/inventory.html"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_login_exitoso(driver):
    """
    Caso de prueba para automatizar un login exitoso en la página de Sauce Demo.
    """    
    print("Iniciando prueba de Login Exitoso...")

    # 1. NAVEGAR A LA PÁGINA DE LOGIN
    driver.get(LOGIN_URL)
    print(f"Navegando a: {LOGIN_URL}")

    # 2. ENCONTRAR E INGRESAR CREDENCIALES

    # Usuario (Por ID)
    user_field = driver.find_element(By.ID, "user-name")
    user_field.send_keys(USERNAME)
    
    # Contraseña (Por ID)
    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys(PASSWORD)
    
    # Botón de Login (Por ID)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # 3. CRITERIO DE VALIDACIÓN CLAVE: ESPERA EXPLÍCITA
    
    # La espera explícita asegura que el script PARE y ESPERE hasta que
    # se cumpla una condición específica, en este caso, la visibilidad
    # del encabezado "Products" en la nueva página.
    try:
        # Definimos una espera de máximo 10 segundos
        wait = WebDriverWait(driver, 10)
        
        # Esperamos a que el título "Products" (etiqueta con clase .title) esté visible
        products_title = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        
        # 4. ASERSIONES (Validaciones)
        
        # A. Validar el texto del encabezado ("Products" o "Swag Labs")
        assert products_title.text == "Products", "El título de la página no es 'Products'."
        
        # B. Validar la URL: Verificar que la URL contenga '/inventory.html'
        current_url = driver.current_url
        assert INVENTORY_URL_PART in current_url, f"No se redirigió a {INVENTORY_URL_PART}. URL actual: {current_url}"

        print("✅ Login Exitoso Validado.")
        
    except Exception as e:
        print(f"❌ La prueba falló. No se pudo verificar la página de inventario en el tiempo esperado: {e}")
        # Asegúrate de que la prueba falle si la excepción se captura aquí
        assert False, f"Fallo en la aserción de la prueba: {e}"