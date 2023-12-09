import networkx as nx
import os

def clique_maximo_resposta(nome_arquivo, debug = False):
    '''
        Utiliza uma biblioteca do python especializada para descobrir qual o clique máximo de um grafo.
    '''

    if not os.path.exists(filename):
        print(f"\n [ERROR] Arquivo {nome_arquivo} não existe! \n")  
        return      

    with open(nome_arquivo, 'r') as arquivo:
        next(arquivo)  

        G = nx.parse_adjlist(arquivo)

    cliques_maximais = list(nx.find_cliques(G))
    clique_maxima = max(cliques_maximais, key=len)

    if(debug):
        print(" ===== [ RESPOSTAS ] ===== ")
        print("\n > Cliques maximais encontradas:")
        for clique in cliques_maximais:
            print(clique)

        print("\n > Clique máxima encontrada:", clique_maxima)
        print("\n > Clique máxima tamanho:", len(clique_maxima))



if __name__ == "__main__":
    
    filename = "../../../data/graphs/grafo.txt"
    clique_maximo_resposta(nome_arquivo = filename, debug = True)