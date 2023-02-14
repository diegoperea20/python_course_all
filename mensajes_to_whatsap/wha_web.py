from selenium import webdriver

# El número de teléfono al que deseas enviar el mensaje, en formato internacional con el código de país
to_number = '+571234567890'

# El cuerpo del mensaje de texto
body = 'Hola, ¿cómo estás?'

# Inicializa el navegador y abre la página web de WhatsApp
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# Espera a que se cargue la página y se escanee el código QR
input('Por favor, escanea el código QR y presiona Enter una vez que hayas iniciado sesión en WhatsApp:')

# Encuentra el elemento de entrada de búsqueda y haz clic en él
search_box = driver.find_element_by_css_selector('#side > div.search-container > div > label > input')
search_box.click()

# Ingresa el número de teléfono en el cuadro de búsqueda y presiona Enter
search_box.send_keys(to_number)
search_box.send_keys(u'\ue007')

# Espera a que se cargue la conversación y encuentra el elemento de entrada de mensaje
message_box = driver.find_element_by_css_selector('#main > footer > div._3ee1T._1LkpH.copyable-text.selectable-text')

# Ingresa el cuerpo del mensaje en el cuadro de entrada y presiona Enter para enviar
message_box.send_keys(body)
message_box.send_keys(u'\ue007')

# Cierra el navegador
driver.quit()
