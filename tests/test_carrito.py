from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constantes del proyecto
LOGIN_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
# ID del primer producto que vamos a agregar (Sauce Labs Backpack)
PRODUCTO_A_AGREGAR_ID = "add-to-cart-sauce-labs-backpack"
# Nombre esperado del producto en el carrito
NOMBRE_PRODUCTO_ESPERADO = "Sauce Labs Backpack"
# Selector para el ícono del carrito
CART_LINK_CLASS = "shopping_cart_link" 
# Selector para el nombre de un producto dentro del carrito
CART_ITEM_NAME_CLASS = "inventory_item_name" 

def test_verificacion_producto_en_carrito(driver):
    """
    Simula el login, agrega un producto, navega al carrito y verifica 
    la presencia y el contador del producto añadido.
    """
    print("\nIniciando prueba de Verificación del Producto en el Carrito...")

    # 1. LOGIN (Necesario para empezar cualquier prueba de flujo)
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # Espera a que cargue el inventario
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    # 2. AGREGA PRIMER PRODUCTO AL CARRITO
    
    add_button = driver.find_element(By.ID, PRODUCTO_A_AGREGAR_ID)
    add_button.click()
    print(f"✅ Se agregó el producto '{NOMBRE_PRODUCTO_ESPERADO}' al carrito.")


    # 3. VERIFICA CONTADOR DEL CARRITO 
    
    # El contador debe ser visible y tener el valor '1'
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.is_displayed(), "❌ El contador del carrito no es visible."
    assert cart_badge.text == "1", f"❌ El contador esperado era '1', se obtuvo '{cart_badge.text}'."
    print("✅ Contador de carrito validado correctamente (valor: 1).")


    # 4. NAVEGAR AL CARRITO DE COMPRAS
    
    cart_icon = driver.find_element(By.CLASS_NAME, CART_LINK_CLASS)
    cart_icon.click()
    
    # Espera a que la URL cambie a la página del carrito
    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )
    print("✅ Navegación a la página del carrito (cart.html) exitosa.")


    # 5. VERIFICA ÍTEM EN CARRITO 
    # Buscamos todos los nombres de productos listados en la página del carrito
    cart_item_names = driver.find_elements(By.CLASS_NAME, CART_ITEM_NAME_CLASS)
    
    # Aserción A: Verificar que haya al menos un ítem
    assert len(cart_item_names) == 1, f"❌ Se esperaba 1 producto en el carrito, se encontraron {len(cart_item_names)}."

    # Aserción B: Verificar que el nombre del producto sea el correcto
    producto_encontrado = cart_item_names[0].text
    assert producto_encontrado == NOMBRE_PRODUCTO_ESPERADO, \
        f"❌ El producto en el carrito no coincide. Se esperaba '{NOMBRE_PRODUCTO_ESPERADO}', se encontró '{producto_encontrado}'."
    
    print(f"✅ Validación de ítem en carrito exitosa. Producto encontrado: {producto_encontrado}")

    print("\n--- PRUEBA DE FLUJO DE CARRITO FINALIZADA CON ÉXITO ---")