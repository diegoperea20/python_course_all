from yowsup.layers.protocol_media import YowMediaProtocolLayer
from yowsup.stacks import YowStackBuilder
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.layers.auth import AuthError
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.protocol_messages import YowMessagesProtocolLayer

# Tu número de teléfono y tu contraseña de WhatsApp
phone = 'your_phone_number'
password = 'your_whatsapp_password'

# El número de teléfono al que deseas enviar el mensaje, en formato internacional con el código de país
to_number = '+571234567890'

# El cuerpo del mensaje de texto
body = 'Hola, mira esta imagen'

# La ruta al archivo de imagen que deseas adjuntar
image_path = '/path/to/image.jpg'

# Crea una pila de capas para la conexión de WhatsApp
stackBuilder = YowStackBuilder()
stack = stackBuilder \
    .pushDefaultLayers(True) \
    .push(YowMessagesProtocolLayer) \
    .push(YowMediaProtocolLayer) \
    .build()

# Inicia la pila y conecta a WhatsApp
stack.setCredentials((phone, password))
stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
try:
    stack.loop()
except AuthError as e:
    print('Error de autenticación: %s' % e)

# Envía el mensaje con la imagen adjunta
media_protocol_layer = stack.getLayerInterface(YowMediaProtocolLayer)
media_protocol_layer.send_message_with_media(to_number, image_path, body)

# Desconecta de WhatsApp y cierra la pila
stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_DISCONNECT))
stack.close()
