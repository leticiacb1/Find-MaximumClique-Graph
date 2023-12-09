import matplotlib.pyplot as plt
import numpy as np

def desenha_grafico_comparacao(filename, title, list_x,list_y, list_labels):
    '''
        Desenha e salva um grafico de comparação entre algorítimos
    '''

    print(len(list_x))
    print(list_y)
    for i in range(len(list_x)):
        plt.plot(list_x, list_y[i], label = list_labels[i])

    plt.xlabel(' N° Vertices ')
    plt.ylabel(' Time (s) ')

    plt.title(title)

    plt.grid(True)
    plt.legend()
    plt.show()

    plt.savefig(filename)

if __name__ == "__main__":

    filename = "../../../img/graphs/grafo.png"

    title = "Grafico Teste"
    
    list_labels = ["1", "2", "3", "4", "5"]

    lista_x = [i for i in range(5)]
    
    lista_y = []
    for j in range(5):
        aux =  [5*j for i in range(5)]
        lista_y.append(aux)


    desenha_grafico_comparacao(filename = filename, title = title , list_x = lista_x , list_y = lista_y, list_labels= list_labels)
