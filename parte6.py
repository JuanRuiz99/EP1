#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:56:35 2018

@author: Juan
"""

#import json
from firebase import firebase

firebase=firebase.FirebaseApplication('https://ep01-434d3.firebaseio.com/ep01-434d3', None)
#result=firebase.get('https://ep01-434d3.firebaseio.com/ep01-434d3', None)
result=firebase.get('https://ep01-434d3.firebaseio.com/ep01-434d3', None)

estoque_total=result

#with open('ep1.json','r') as arquivo:
#    conteudo = arquivo.read().strip()
#    if len(conteudo)==0:
#        estoque_total={}
#    else:
#        estoque_total=json.loads(conteudo)
#*******************************************************  CODIGO LOJA *********
while True:
    print("Controle de Loja")
    print('0- sair')
    print("1- Adicionar loja")
    print('2- imprimir loja(s)')
    print('3- Selecionar loja')
    escolha_1 =int(input('Faca sua escolha: '))
    if escolha_1 == 0:
        print('Ate mais!')
        break
    
    if escolha_1 == 1:
        loja=input('Nome da loja: ')
        if loja in estoque_total:
            print('Loja ja cadastrada')
        else:
            estoque_total[loja]={}
            estoque = estoque_total[loja]
            break
                    
    if escolha_1 == 2:
        for i in estoque_total:
            print(i)
        
    if escolha_1 == 3:
        loja_selecionada = input('Selecione sua loja: ')
        if loja_selecionada not in estoque_total:
            print('Loja nao encontrada')
        else:
            estoque = estoque_total[loja_selecionada]
        break
#*******************************************************  CODIGO ESTOQUE ******
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
#with open('ep1.json','w') as arquivo2:
#    arquivo2.write(json.dumps(estoque_total))
    

#firebase.put('https://ep01-434d3.firebaseio.com/','ep01-434d3', estoque_total) 
#    else:
#        print('Escolha invalida, escolha novamente')
if escolha_1 == 1:
    firebase.patch(loja, estoque_total[loja])
if escolha_1 == 3:
    firebase.patch(loja_selecionada, estoque_total[loja_selecionada])