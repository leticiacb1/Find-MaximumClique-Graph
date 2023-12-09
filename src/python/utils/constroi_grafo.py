import networkx as nx
import matplotlib.pyplot as plt
import random

def constroi_grafo(nome_arquivo, num_vertices, show = False, save_fig_graph = None):
    '''
        Constroi um grafo com {num_vertices} e salva seu resultado em um arquivo {nome_arquivo}
    '''

    probabilidade_conexao = 0.7
    grafo = nx.fast_gnp_random_graph(num_vertices, probabilidade_conexao)

    with open(nome_arquivo , 'w') as arquivo:
        arquivo.write(f"{num_vertices} {grafo.number_of_edges()}\n")

        for aresta in grafo.edges():
            arquivo.write(f"{aresta[0]+1} {aresta[1]+1}\n")

    print(f" [INFO] Grafo densamente conectado gerado e salvo em '{nome_arquivo}'.\n")

    # Desenha Grafo
    if (show):
        pos = nx.spring_layout(grafo)
        nx.draw(grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color='red',
                font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.8)

        plt.title("Grafo com " + str(num_vertices) + " vertices")
        plt.savefig(save_fig_graph)
        plt.show()

if __name__ == "__main__":
    
    num_vertices = 4
    filename = "../../../data/graphs/grafo.txt"

    constroi_grafo(nome_arquivo = filename, num_vertices = num_vertices)