# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from models import Organizador
import os
"""
Created on Sat Apr 18 15:28:22 2026

@author: AP

"""

app= Flask(__name__) #app objecto criado pela class flask/__name__ faz ref ao nome do arquivo.

@app.route("/",methods=["GET","POST"]) #rota para chaar a funcao abaixo
def home():
    #Funcao executada assim que route for acessada
    if request.method=="POST":
        caminho=request.form.get("caminho")
        acao=request.form.get("acao")
        
        if not os.path.exists(caminho):
            print("Caminho Inválido.")
        if caminho.strip=="":
            print("Erro:Não foi informado nenhum caminho")
            
        org=Organizador(caminho)
        if acao=="mover":
            resultado=org.encontrar_duplicados(acao)
        elif acao=="apagar":
            resultado=org.encontrar_duplicados(acao)
        elif acao=="backup":
            resultado=org.criar_backup()
        elif acao=="organizar":
            resultado=org.Organizar()
        elif acao=="renomear":
            resultado=org.Renomear()
        elif acao=="relatorio":
            resultado=org.Gerar_Relatorio_Completo()
        return str(resultado)
    return render_template("index.html")
        
if __name__=="__main__":
    app.run()#inicia o server,par debug-recarrega auto alteracoes feitas e mostra erros no browser 
    