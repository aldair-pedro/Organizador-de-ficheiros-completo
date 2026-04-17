# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:51:57 2026

@author: AP
"""
import json




class Config_json:
    def __init__(self):
        
        with open("config.json","r",encoding="utf-8") as f:
             self.data=json.load(f)
