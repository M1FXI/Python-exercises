import matplotlib.pyplot as plt


montante = float(input("Valor inicial: "))
rendimento = float(input("valor de rendimento (%): "))
aporte = float(input("valor de aporte por período: "))
ciclos = int(input("Total de períodos: "))


def ciclos_de_rendimento(montante, rendimento, aporte, ciclos):
    valores=[None]*ciclos
    for i in range(ciclos):
        montante=montante+(rendimento*(montante/100))+aporte
        print(f"Após {i+1} período(s), o montante será de R${round(montante, 2)}")
        valores[i]=montante
    return(valores)

        
        
        
def mostra_grafico(valores, ciclos):
    vetor_de_ciclos = []
    for i in range(1, ciclos+1):
        vetor_de_ciclos.append(i)
    plt.plot(vetor_de_ciclos ,valores)
    plt.show()
        
        
    
        
    
    
valores = ciclos_de_rendimento (montante, rendimento, aporte, ciclos)

mostra_grafico(valores, ciclos)