renda = float(input("informe valor de renda mensal: R$"))
totais_moradia = float(input("informe valor dos seus gastos totais com moradia: R$"))
totais_educação = float(input("informe valor dos seus gastos totais com educação: R$"))
totais_transporte = float(input("informe valor dos seus gastos totais com transporte: R$"))

def funcao_diagnostico (renda, totais_moradia, totais_educação, totais_transporte):
    totais_moradia = (totais_moradia/renda)*100
    totais_educação = (totais_educação/renda)*100
    totais_transporte = (totais_transporte/renda)*100
    
    if totais_moradia <= 30:
        print(f"Seus gastos com moradia estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com moradia comprometem {round(totais_moradia)}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {renda*0.3}.")
    if totais_educação <= 20:
        print(f"Seus gastos com educação estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com educação comprometem {round(totais_educação)}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {renda*0.2}.")
    if totais_transporte <= 15:
        print(f"Seus gastos com transporte estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com transporte comprometem {round(totais_transporte)}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {renda*0.15}.")
    

funcao_diagnostico (renda, totais_moradia, totais_educação, totais_transporte)



