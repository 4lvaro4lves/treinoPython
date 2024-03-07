import datetime
import time

def diferenca():
        s = int(input("Digite quantos segundos deseja esperar :  "))

        antes = datetime.datetime.now()

        print("Aguardando")
        time.sleep(s/4)
        for i in range(1,4):
            print (".")
            time.sleep(s/4)

        depois = datetime.datetime.now()

        
        print ("Antes")
        print (antes)
        print ("\nDepois")
        print (depois)
        erro =  (depois.microsecond - antes.microsecond)/1000000
        print ("\nErro na contagem em segundos")
        print (erro)
