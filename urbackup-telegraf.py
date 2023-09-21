import urbackup_api
from telegraf.client import TelegrafClient
import time
import datetime
import keyring
urbackusername = keyring.get_password("urbackup", "username")
urbackpassword = keyring.get_password("urbackup", "password")
server = urbackup_api.urbackup_server("http://[YOUR_IP]:55414/x", urbackusername, urbackpassword)
tgClient = TelegrafClient(host='localhost', port=8092)
clients = server.get_status()
for client in clients:
    tgClient.metric('Urbackup Status', client['image_ok'], tags={'Endpoint': client['name']})
    tgClient.metric('Urbackup Last', client['lastbackup_image'], tags={'Endpoint': client['name']})
    tgClient.metric('Urbackup Seen', client['lastseen'], tags={'Endpoint': client['name']})
