from channels.consumer import SyncConsumer
from time import sleep
import names
from .models import Name

class GenerateName(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        a=event['text']

        for i in range(int(a)): 
            name=names.get_first_name()
            Name.objects.create(name=name)   
            self.send({
            "type": "websocket.send",
            "text": str(name),
            })
            sleep(10)

    def  websocket_disconnect(self, event):
        print("websoket disconnect",event)