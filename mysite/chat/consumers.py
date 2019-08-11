# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json

from chat.classes.msgautomatica import MsgAutomatica

class ChatConsumer(WebsocketConsumer):

    # Atributo da classe
    conexoesAtivas = []
    
    def connect(self):
        self.accept()
        self.__class__.conexoesAtivas.append(self)
        self.atualizarClienteMsgAutomatica()

        self.printConexoes() #self.__class__.printConexoes()

    def disconnect(self, close_code):
        if self in self.__class__.conexoesAtivas:
            self.__class__.conexoesAtivas.remove(self)
            self.atualizarClienteMsgAutomatica()
        
        self.printConexoes()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        messagemRecebida = text_data_json['messagem']

        if messagemRecebida == 'iniciarthread':
            MsgAutomatica.iniciarThread()

        # Envia a mensagem para todos os clientes ativos e para quem redigiu a mensagem
        for client in self.__class__.conexoesAtivas:
            client.send(text_data=json.dumps({
                'message': messagemRecebida
            }))

    @classmethod
    def printConexoes(cls):
        print('\tConexoes Ativas: ' + str(len(cls.conexoesAtivas)))

    @classmethod
    def atualizarClienteMsgAutomatica(cls):
        # Sicroniza os clientes com a classe msgAutomatica
        MsgAutomatica.clientesSocket = cls.conexoesAtivas