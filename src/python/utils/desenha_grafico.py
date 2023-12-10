import matplotlib.pyplot as plt
import numpy as np

def desenha_grafico(filename, title, x_label, y_label, list_x,list_y, list_labels):
    '''
        Desenha e salva um grafico de comparação entre algorítimos
    '''

    for i in range(len(list_y)):
        plt.plot(list_x, list_y[i], marker='o', linestyle='-' , alpha=0.7,  markeredgecolor='black', size = 4, label = list_labels[i])

    plt.xlabel(x_label)
    plt.ylabel(y_label)

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
