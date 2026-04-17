# -*- coding: utf-8 -*-
from models import Organizador
import time
"""
Created on Sun Apr  5 17:11:05 2026

@author: AP
"""

caminho=input("Qual Pasta Vamos Organizar? ")
org=Organizador(caminho)
def menu_dup():
    print("""
          ---- Como tratar os duplicados? ----
          
              [1]-Mover
              [2]-Apagar
          """)  
def menu():
    print(
        """
          ---- BEM-VINDO AO ORGANIZADOR DE FICHEIROS ----
          
              [1]- Organizar Ficheiros
              [2]-Fazer Backup dos Ficheiros
              [3]-Relatório Completo
              [4]-Ficheiros Duplicados
              [5]-Renomear Ficheiros
              [6]-Encerrar Programa
          """)
    
while True:
    menu()
    try:
            
        op=int(input("Escolha uma opção: "))
        
        if op==1:
            org.Organizar()
            print("Ficheiros Organizados")
            
        elif op==2:
            org.criar_backup()
            print("BackUp Feito...")
            
        elif op==3:
            org.Gerar_Relatorio_Completo()
            print("Relatório Feito...")
            
        elif op==4:
            menu_dup()
            acao=input("Escolha: ").lower()
            if acao=="1":
                acao="mover"
            elif acao=="2":
                acao="apagar"
            else:
                print("Opção Invalida")
                continue     
            org.encontrar_duplicados(acao)
            print("Tratamento de duplicados feito...")
        
        elif op==5:
            org.Renomear()
            print("Ficheiros Renomeados...")
            
        elif op==6:
            print("Encerrando o Programa.")
            time.sleep(0.5)
            print("Volte Sempre...")
            break
        
        else:
            print(f"Opção Inválida: {op}")
            
    except Exception as e:
        print(f"Erro: {e}")
       
    
    try:
        
        opp=input("Deseja continuar?[S/N]").lower()
        if opp=="s":
            continue
        
        elif opp=="n":
            print("Escolha a opção [6].\nPara encerrar o Programa. ")
            time.sleep(2)
            
        else:
            print("Opção Inválida")
            
    except Exception as e :
        print(f"Erro: {e}")
   
        
        
    
        

#org.Organizar()
#org.criar_backup()
#org.Gerar_Relatorio_Completo()
#org.encontrar_duplicados(caminho)
