# Importar la biblioteca pywhatkit
import pywhatkit

# El número de teléfono al que deseas enviar el mensaje, con el código del país
to_number = "+573001234567"

# El contenido del mensaje
message_body = "Hola, ¿cómo estás?"

# Enviar el mensaje en una hora determinada (en este caso, a las 22:00)
pywhatkit.sendwhatmsg(to_number, 22, 0, message_body)

print(f"Mensaje enviado a {to_number}")


""" Es posible enviar mensajes de texto a través de WhatsApp utilizando Python, aunque es un proceso un poco más complejo que utilizar una biblioteca como Twilio. Para enviar mensajes de texto a través de WhatsApp desde Python, tendrás que utilizar la API de WhatsApp Business o la API de WhatsApp Messenger. Ambas APIs te permiten enviar mensajes de texto, imágenes y otros tipos de contenido a través de WhatsApp utilizando una solicitud HTTP.

Para utilizar la API de WhatsApp, necesitarás tener una cuenta de WhatsApp Business o WhatsApp Messenger y obtener un token de acceso. Además, necesitarás instalar la biblioteca pywhatkit para utilizar la API de WhatsApp desde Python.

A continuación se presenta un ejemplo de cómo enviar un mensaje de texto a través de WhatsApp utilizando la API de WhatsApp Messenger y la biblioteca pywhatkit: """