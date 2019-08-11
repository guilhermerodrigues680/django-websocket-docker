""" Esta classe envia a cada intervalo de tempo
uma mensagem para todos os clientes WebSockets ativos 
"""

import threading
import time
import json

class MsgAutomatica(object):

    # Atributos da classe
    t = None # Variavel que irá armazenar a Thread
    clientesSocket = [] # Variavel que armazenará os sockets do consumers.py

    @classmethod
    def rotinaThread(cls, messagem):
        cont = 0
        while True:
            for client in cls.clientesSocket:
                client.send(text_data=json.dumps({
                    'message': messagem + str(cont)
                }))

            cont += 1

            print(len(cls.clientesSocket))
            time.sleep(2)

    @classmethod
    def iniciarThread(cls):
        if cls.t == None:    
            print('Iniciando Thread...')
            msg = "thread sendo executada"
            cls.t = threading.Thread(target=cls.rotinaThread,args=(msg,))
            cls.t.start()
            
        else:
            print('Thread já iniciada!')