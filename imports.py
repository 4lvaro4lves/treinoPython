from defs.sair import * #importa todas as funçoes e deixa como nativas
from defs.mat import soma, potencia, fibonacci #importa as funçoes (soma, potencia e fibonacci) e deixa como nativas
import defs.calTempo #importa tudo mas não deixa nativa
from defs.limpar import limpaTela as limpar #importa somente a funcão limpaTela e chama de limpar deixando nativa
from defs.continuar import repetir as continuar #importa somente a funcão prosseguir e chama de continuar deixando nativa


def menu():
    menu = ('ativo')
    while (menu == 'ativo'):
        menu = ('inativo')
        print ("\nIniciando Importação das Funções")
        print ("\nQual função deseja usar?")
        print ("1 - Calulo do tempo")
        print ("2 - Matemática")
        print ("3 - Calulo do tempo")
        escolha = input("                       = ")

        while(escolha == '1'):
            limpar()
            print("Iniciando def/caltempo.py")
            defs.calTempo.diferenca()
            print("\n\nFinalizando def/caltempo.py\n\n")

            escolha = continuar()
            if (escolha == 'menu'):
                menu = ('ativo')
            elif(escolha == ''):
                escolha = ('1')
            else:
                exit()

            
        
        while(escolha == '2'):
            limpar()
            print("Iniciando def/mat.py")
            print ("SOMA")
            print (soma())
            print ("\nPOTÊNCIA")
            print (potencia())
            print ("\nFIBONACCI")
            print (fibonacci())
            print(".\n.\nFinalizando def/mat.py\n\n")

            escolha = continuar()
            if (escolha == 'menu'):
                menu = ('ativo')
            elif(escolha == ''):
                escolha = ('2')
            else:
                exit()


#
menu()
limpar()
sair()
