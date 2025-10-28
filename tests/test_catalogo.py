from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constantes de la Página de Inventario
LOGIN_URL = "https://www.saucedemo.com/"
INVENTORY_URL_PART = "/inventory.html"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
INVENTORY_URL_PART = "/inventory.html"
EXPECTED_TITLE_TEXT = "Products"
PRODUCT_ITEM_CLASS = "inventory_item"
PRODUCT_NAME_CLASS = "inventory_item_name"
PRODUCT_PRICE_CLASS = "inventory_item_price"
MENU_BUTTON_ID = "react-burger-menu-btn"
CART_ICON_CLASS = "shopping_cart_link"


def test_verificacion_catalogo(driver):

    """
    Verifica que la página de inventario se haya cargado correctamente
    """

    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    print("\nIniciando prueba de Verificación del Catálogo...")
    # 1. NAVEGAR A LA PÁGINA DE INVENTARIO DESPUÉS DEL LOGIN

    if INVENTORY_URL_PART not in driver.current_url:
        print("⚠️ Advertencia: Asumiendo que el driver está en la página de inventario tras un login previo.")
    # 2. VALIDA  TÍTULO DE LA PÁGINA
    # Usamos una espera explícita para asegurarnos de que el título esté visible
    wait = WebDriverWait(driver, 10)
    
    # El título del catálogo es el elemento con la clase 'title'
    products_title_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    
    # Aserción A: Verificar el texto del título
    assert products_title_element.text == EXPECTED_TITLE_TEXT, \
        f"❌ Título de página incorrecto. Se esperaba '{EXPECTED_TITLE_TEXT}', se obtuvo '{products_title_element.text}'."
    
    print(f"✅ Validación de Título exitosa: {products_title_element.text}")


    # 3. VALIDA PRESENCIA DE PRODUCTOS Y LISTA INFO DEL PRIMERO
    
    # Encontrar todos los contenedores de productos
    product_list = driver.find_elements(By.CLASS_NAME, PRODUCT_ITEM_CLASS)
    
    # Aserción B: Comprobar que haya al menos un producto visible
    assert len(product_list) > 0, "❌ No se encontraron productos en la página."
    print(f"✅ Validación de Presencia de Productos exitosa. Se encontraron {len(product_list)} productos.")
    
    # Extraer y listar nombre/precio del primer producto
    first_product = product_list[0]
    
    # Nombre del primer producto
    name = first_product.find_element(By.CLASS_NAME, PRODUCT_NAME_CLASS).text
    
    # Precio del primer producto
    price = first_product.find_element(By.CLASS_NAME, PRODUCT_PRICE_CLASS).text
    
    print(f"\n Primer Producto Listado:")
    print(f"   Nombre: {name}")
    print(f"   Precio: {price}")
    
    
    # 4. VALIDAR ELEMENTOS IMPORTANTES DE LA INTERFAZ
    
    # Aserción C: Verificar la presencia del botón de menú (hamburguesa)
    menu_button = driver.find_element(By.ID, MENU_BUTTON_ID)
    assert menu_button.is_displayed(), "❌ El botón de Menú (hamburguesa) no está visible."
    
    # Aserción D: Verificar la presencia del icono del carrito de compras
    cart_icon = driver.find_element(By.CLASS_NAME, CART_ICON_CLASS)
    assert cart_icon.is_displayed(), "❌ El ícono del carrito de compras no está visible."

    print("✅ Validación de Elementos de Interfaz (Menú y Carrito) exitosa.")
    print("\n--- PRUEBA DE CATÁLOGO FINALIZADA CON ÉXITO ---")