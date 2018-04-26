#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:28:02 2018

@author: allansinger99
"""
import json

with open('ep1.json','r') as arquivo:
    conteudo = arquivo.read().strip()
    if len(conteudo)==0:
        estoque={}
    else:
        estoque=json.loads(conteudo)
        
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
            j=float(input('Preco unitario: '))
            while j<0:
                print('O preco unitario nao pode ser negativo')
                j=float(input('Preco unitario: '))
            if produto not in estoque and quantidade>0 and j>0:
                estoque[produto]={'quantidade': quantidade, 'preco': j}
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
#******************************************************************************         
        esc = input('1- Ver lista de produtos com quantidade de estoque negativa; 2- Ver o valor total do estoque: ')
        if esc=='1':
            
            estoque_negativo=[]
            for k in estoque:
                if estoque[k]['quantidade']<0:
                    print('{0}:{1}'.format(k,estoque[k]['quantidade']))
                
                
        elif esc=='2':
            total=0
            for i in estoque:
               total += estoque[i]["quantidade"]*estoque[i]["preco"]
            print('R${0}'.format(total))
#******************************************************************************    
with open('ep1.json','w') as arquivo2:
    arquivo2.write(json.dumps(estoque))
