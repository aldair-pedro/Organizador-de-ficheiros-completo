# -*- coding: utf-8 -*-
from config import Config_loader
from config_json import Config_json

import os
import shutil
import hashlib
import csv
#import json
"""
Created on Sun Apr  5 16:11:15 2026

@author: AP
"""


class Organizador(Config_loader):
    def __init__(self,caminho):
        self.config=Config_loader()
        self.config_json=Config_json()
        self.caminho=caminho
        self.pasta=0
        self.duplicados=0
        self.relatorio=[]
        
    def criar_pasta(self,nome):
        pasta=os.path.join(self.caminho,nome)
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        return pasta
    def categoria(self,ficheiro):
        _,extensao=os.path.splitext(ficheiro)
        for categoria,lista_ext in self.config.Extensoes.items():
            if extensao.lower() in lista_ext:
                return categoria
        return "Outros"
    
    def Organizar(self):
        try:
            
            for ficheiro in os.listdir(self.caminho):
                caminho_completo=os.path.join(self.caminho,ficheiro)
                
                if os.path.isdir(caminho_completo):
                    self.pasta+=1
                    continue
                
                categoria=self.categoria(ficheiro)
                pasta=self.criar_pasta(categoria)
                pasta_destino=os.path.join(pasta,ficheiro)
                shutil.move(caminho_completo,pasta_destino)
                self.relatorio.append(f"Ficheiro movido -> {ficheiro}")
            print("Organização Feita com Sucesso...")
        except Exception as e:
            print(f"Erro ao Organizar:{e}")
    def calcular_hash(self,caminho):
        hash_obj=hashlib.sha256()
        with open(caminho,"rb") as f:
            for chunk in iter(lambda: f.read(4096),b""):
                hash_obj.update(chunk)
                return hash_obj.hexdigest()  
    def encontrar_duplicados(self,acao):
        hashes={}
        duplicados=[]
        pasta_dup=self.config_json.data["duplicados"]["nome_pasta"]
        
        for root,_,files in os.walk(self.caminho):
            for file in files:
                caminho_completo2=os.path.join(root,file)
                try:
                   h=self.calcular_hash(caminho_completo2)
                   if h in hashes:
                       
                       duplicados.append([caminho_completo2,hashes[h]])
                       self.duplicados+=1
                       self.relatorio.append([file,"Duplicado",caminho_completo2,hashes[h]])
                       
                      
                       if acao=="mover":
                           pasta_duplicados=os.path.join(self.caminho,pasta_dup)
                           if not os.path.exists(pasta_duplicados):
                               os.makedirs(pasta_duplicados)
                           destino=os.path.join(pasta_duplicados,file)
                           if os.path.exists(destino):
                                 nome,ext=os.path.splitext(file)       
                                 destino=os.path.join(pasta_duplicados,f"{nome}_dup{ext}")  
                           shutil.move(caminho_completo2,destino)
                           
                       elif acao=="apagar":
                           os.remove(caminho_completo2)
                           continue
                       
                   else:
                       hashes[h]=caminho_completo2
                       self.relatorio.append([file,"Único",caminho_completo2])
                       
                except Exception as e:
                    self.relatorio.append([file,caminho_completo2,e])
                    print(e)
                   
        return duplicados
    
    def criar_backup(self):
        nome_backup=self.config_json.data["backup"]["nome_pasta"]
        backup=os.path.join(self.caminho,nome_backup)
        if not os.path.exists(backup):
            os.makedirs(backup)

        for ficheiro in os.listdir(self.caminho):
            origem=os.path.join(self.caminho,ficheiro)
            
            if ficheiro == nome_backup:
                self.relatorio.append([ficheiro,"Pasta","Ignorado",origem])
                continue
            if  ficheiro.startswith("."):
                self.relatorio.append([ficheiro,"Sistema","Ignorado",origem])
                continue
            try:
                if os.path.isfile(origem):
                    destino_file=os.path.join(backup,ficheiro)
                    shutil.copy(origem,destino_file)
                    self.relatorio.append([ficheiro,"Ficheiro","Copiado",origem,destino_file])
                elif os.path.isdir(origem):
                    destino_pasta=os.path.join(backup,ficheiro)
                    shutil.copytree(origem,destino_pasta)
                    self.relatorio.append([ficheiro,"Pasta","Copiado",origem,destino_pasta])
            except Exception as e :
                print(f"ERRO em {ficheiro}:{e}")
                self.relatorio.append([ficheiro,"Erro: "+str(e),origem])
        print("BackUp Feito....")
    
    def Gerar_Relatorio_Completo(self):
        try:
            nome_relatorio=self.config_json.data["relatorio"]["arquivo"]
            caminho_csv=os.path.join(self.caminho,nome_relatorio)
            with open(caminho_csv,"a",newline="",encoding="utf-8") as arquivo:
                writer=csv.writer(arquivo)
                writer.writerow(["Nome","Tipo","Origem","Destino"])
                writer.writerows(self.relatorio)
                print("Relatório Completo Feito...")
        except Exception as e:
            print(f"Erro Detectado: {e}")
            
    def Renomear(self):
        try: 
            s=1
            ficheiro=self.config_json.data["renomear"]["ficheiros"]
            for file in os.listdir(self.caminho):
                _,ext=os.path.splitext(file)
                origem=os.path.join(self.caminho, file)
                nome=f"{ficheiro}_"+str(s)+ext
                novo_caminho=os.path.join(self.caminho, nome)
                s+=1
                os.rename(origem, novo_caminho)
                self.relatorio.append([file ,origem,novo_caminho])
        except Exception as e:
            self.relatorio.append([ficheiro,"Erro: "+str(e),origem])
            print(f"Erro ao Renomear: {e}")
            
            
    
            
            
        
    
              
        
        
        
        
        
        
            
                
           
                
            