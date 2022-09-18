def extrair_dados(caminho_arquivo):
  with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: 
    conteudo = arquivo.read()
  
  conteudo = conteudo.splitlines() 
  rotulos = conteudo[0] 
  rotulos = rotulos.split(',')
  conteudo = conteudo[1:] 
  valores_listados = []
  for lista_anos in conteudo:
    lista_anos = lista_anos.split(',') 
    valores_listados.append(lista_anos) 
  
  return rotulos, valores_listados


nome_pais=(input("Digite o nome do país: "))
ano=(input("Digite ano do pib: "))

def diz_pib(nome_pais, anos):
    rotulos, lista_anos = extrair_dados('Assessment_PIBs1.csv')
    achou_pais=False
    achou_ano=False
    for i in range(15):
        if lista_anos[i][0] == nome_pais:
            achou_pais=True
            for y in range(8):
                if rotulos[y] == anos:
                    achou_ano=True               
    if achou_ano==False:
        print("ano inválido")
    if achou_pais==False:
        print("nome de país inválido")
    if achou_pais==True and achou_ano==True:
        print(f"PIB {nome_pais} em {anos}: US${lista_anos[i][y]} trilhões.") 
#     return(pib)
                  


    

diz_pib(nome_pais, ano)
