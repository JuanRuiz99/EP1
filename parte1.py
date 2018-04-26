#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:20:11 2018

@author: Juan
"""

estoque={}

while True:
    print("Controle de Estoque")
    print("0 - sair")
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - alterar item")
    print("4 - imprimir estoque")
    escolha=input("Faca sua escolha: ")
    
#******************************************************  CODIGO ESCOLHA 0 *****        
    
    if escolha=='0':
        print("Ate mais!")
        break
    
#*******************************************************   CODIGO ESCOLHA 1 ***
    
    elif escolha=='1':
        produto=input("Nome do produto: ")
        if produto in estoque:
            print("Produto ja cadastrado")
        else:
            quantidade=int(input("Quantidade inicial: "))
            while quantidade<0:
                print("A quantidade inicial nao pode ser negativa")
                quantidade=int(input("Quantidade inicial: "))
          
            if produto not in estoque:
                estoque[produto]={'quantidade':quantidade}
#*******************************************************   CODIGO ESCOLHA 2 ***            
    elif escolha=='2':
        produto=input("Nome do produto: ")
        if produto in estoque:
            del estoque[produto]
        else:
            print("Produto nao cadastrado")
            
 #*******************************************************  CODIGO ESCOLHA 3 ***           
    elif escolha=='3':
        produto=input("Nome do produto: ")
        if produto in estoque:
            quantidade3=int(input("Quantidade: "))
            soma=(quantidade + quantidade3)
            estoque[produto]['quantidade']=soma
        else:
            print("Produto nao cadastrado")
            
            
#*********************************************************  CODIGO ESCOLHA 4***    
        
    elif escolha=='4':
        print(estoque)    