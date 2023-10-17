def deletar_arquivo(produtos,nome):
    nome=input("digite o nome do produto:  ")
    for linha in leitor_csv:
        if linha['Nome'] == nome:
            produto_registrado = linha
    if produto_registrado:
        linha.delete(produto_registrado)
        print("produto apagado")
        produtos=leitor_csv
        criar_arquivo_csv()

while True:
    
    
    print("1 -  Cadastrar Produto")
    print("2 -  Imprimir Produtos")
    print("3 -  Atualizar Produto")
    print("4 -  Deletar Produto")
    print("5 -  Fechar Programa")
    print("===============================")
    escolha=(input("Escolha uma das opçoes acima:  "))
    
    if escolha=="1":
        
        nome=(input("Nome do produto:  "))
        qnt=float(input("Quantidade a ser vendida:  "))
        valor=float(input("Valor do produto unitario:  "))
        lucro=float(input("Lucro do produto:  "))
        imp1=float(input("Valor do Imposto1:  "))
        imp2=float(input("Valor do Imposto2:  "))
        imp3=float(input("Valor do Imposto3:  "))
        frete=float(input("Valor de Frete:  "))
   
    elif escolha=="2":
        imprimir_csv(arquivo_csv)
        
    elif escolha=="3":
        
        atualizar_produtos(leitor_csv)
    
    elif escolha == "4":
        
        deletar_arquivo(produtos,nome)
        
    elif escolha=="5":
        print("fechando programa")
        
        break

    
        
        
            
            
    
    
