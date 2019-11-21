# https://mydevices.com/cayenne/docs_stage/cayenne-mqtt-api/#cayenne-mqtt-api-manually-publishing-subscribing
# Manually Publishing / Subscribing

# Biblioteca para o protocolo MQTT
import paho.mqtt.client as mqtt
import time

# Variáveis para acesso ao servidor
import credenciais as c

# Cria o objeto para acessar o servidor (Client ID)
client = mqtt.Client(c.client_id)

# Informa ao objeto o usuário e senha para acesso ao servidor (MQTT username, MQTT password)
client.username_pw_set(c.user, c.password)

# Estabelece a conexão com o servidor (MQTT Server, MQTT Port)
client.connect(c.server, c.port)

# MQTT Server, MQTT Port,
client.connect(c.server, c.port)

# Envia a informação 123.4 para o canal 0
client.publish('v1/'+c.user+'/things/'+c.client_id+'/data/0', 123.4) # posta no canal 0
time.sleep(5)

from random import randrange
def umidade():
    return randrange(20, 60)

def mensagem(client, userdata, msg): # callback
    t = msg.topic.split('/')
    v = msg.payload.decode().split(',')
    print(t)
    print(v)
    client.publish('v1/'+c.user+'/things/'+c.client_id+'/response', 'ok,'+v[0]) # posta no canal 0

client.on_message = mensagem #callback
client.subscribe('v1/'+ c.user +'/things/'+c.client_id+'/cmd/2')
client.loop_start()   # tread de monitorar

# MQTT Server, MQTT Port,
client.connect(c.server, c.port)


client.on_message = mensagem #callback
client.loop_start()   # tread de monitorar


if __name__ == '__main__':
    while True:
        umid = umidade()
        client.publish('v1/' + c.user + '/things/' + c.client_id + '/data/1', umid)  # posta no canal 0

        time.sleep(10)
