import csv
def cadastrar_produtos(produtos,nome,valor,qnt,lucro,valordecusto,valordevenda,frete,imp1,imp2,imp3):
    produto ={
        'Nome' : nome,
        'Valor' : valor,
        'Qnt' : qnt,
        'Lucro' : lucro,
        'Valorcusto' : valordecusto,
        'Valorvenda': valordevenda,
        'Frete' : frete,
        'Imp1' : imp1,
        'Imp2' : imp2,
        'Imp3' : imp3
    }
    
    produtos.append(produto)
    criar_arquivo_csv()
    print("Produto cadastrado com sucesso!")
    
produtos = []

def criar_arquivo_csv():
    with open ('arquivo.csv', mode='w', newline="") as arquivo_csv:
        writer= csv.writer(arquivo_csv)
        writer.witerow(["Nome", "Valor", "Valor de custo", "lucro", "Valor de venda", "Quantidade", "Imposto 1", "Imposto 2", "Imposto 3", "Frete"])

        for produto in produtos:
            writer.witerow([produto['Nome'], produto['Valor'], produto['Valordecusto'], produto['Lucro'], produto['Valordevenda'], produto['Qnt'], produto['Imp1'], produto['Imp2'], produto['Imp3'], produto['Frete']])

def ler_arquivo_csv():
    try:
        with open('arquivo.csv' ,mode= 'r') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            return list(leitor_csv)
    except FileNotFoundError:
        print(f"O arquivo não foi encontrado.")

def imprimir_csv():
    for linha in produtos:
        imp1 = (float(linha['Valor']) * float(linha['Imp1'])) / 100
        imp2 = (float(linha['Valor']) * float(linha['Imp2'])) / 100
        imp3 = (float(linha['Valor']) * float(linha['Imp3'])) / 100
        frete = (float(linha['Frete']) / float(linha['Qnt']))
        valordecusto = float(linha['Valor']) + imp1 + imp2 + imp3 + frete
        lucro = float(linha['Lucro'])
        valordevenda = valordecusto+ (valordecusto * (lucro/ 100))
        print(linha)

def atualizar_produtos(leitor_csv):
    ler_arquivo_csv()
    nome =  input("Digite o nome do produto que deseja apagar: ")
    for linha in leitor_csv:
        if linha['Nome'] == nome:
            
            print(f"****************************")
            print("")
            linha['Nome'] = input("Nome do produto:  ")
            linha['Valor'] = float(input("Valor do produto: "))
            linha['Qnt'] = float(input("Quantidade do produto: "))
            linha['Frete'] = float(input("Valor do frete: "))
            linha['Imp1'] = float(input("Valor do primeiro imposto: "))
            linha['Imp2'] = float(input("valor do segungo imposto: "))
            linha['Imp3'] = float(input("Valor do terceiro imposto: "))
            linha['Lucro'] = float(input("Valor da margem de lucro desejada: "))
        
        produtos = leitor_csv

        criar_arquivo_csv()

        print(f"")
        print("Produto atualizado!")
        print(f"****************************")
        print(f"")
    else:
        print("ID não encontrada!")

def deletar_arquivo(produtos,nome):
    ler_arquivo_csv()
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
        imprimir_csv()
        
    elif escolha=="3":
        
        atualizar_produtos()
    
    elif escolha == "4":
        
        deletar_arquivo(produtos,nome)
        
    elif escolha=="5":
        print("fechando programa")
        
        break
