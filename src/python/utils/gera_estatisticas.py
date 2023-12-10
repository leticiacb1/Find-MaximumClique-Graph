
from .clique_maximo_resposta import clique_maximo_resposta
from .processa_stdout import pega_tamanho, pega_vertices_max_clique
import subprocess
import pandas as pd

def gera_estatisticas(algoritimo, lista_de_vertices, lista_commandos, arquivo_csv, debug = False):
    '''
        Compara resultado obtido pelo algorítimo com a resposta esperada.
        Salva essas informações em um .csv 
    '''
    
    # Variaveis Auxiliares
    lista_nome_algoritimo = len(lista_de_vertices)*[algoritimo]

    lista_valores_calculados= []
    lista_valores_esperados = []

    lista_tamanho_calculado = []
    lista_tamanho_esperado  = []

    lista_qtd_vertices = []

    lista_mesmo_tamanho = []

    for command in lista_commandos:
        
        if(debug):
            print(f" [COMANDO] {command} | [VERTICES] {command[2]}\n")
        
        executavel = command[0]
        filename_grafo = command[1]
        num_vertice = command[2]
        
        # ---- Resultado Esperado ----
        esperado = clique_maximo_resposta(filename_grafo)
        size_esperado = len(esperado)

        # ---- Resultado Obtido ----
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout_result = result.stdout

        calculado = pega_vertices_max_clique(stdout_result)
        size_obtido = pega_tamanho(stdout_result)

        # ---- Adiciona nas listas auxiliares ----
        lista_valores_calculados.append(calculado)
        lista_valores_esperados.append(esperado)

        lista_tamanho_calculado.append(len(calculado))
        lista_tamanho_esperado.append(len(esperado))

        lista_mesmo_tamanho.append("Sim" if (len(calculado) == len(esperado)) else "Não")

    # ---- Monta dataframe ----
    dados = {
        'Algoritimo': lista_nome_algoritimo ,
        'Vertices' : lista_de_vertices,
        'Clique Esperado': lista_valores_esperados,
        'Clique Calculado': lista_valores_calculados,
        'Tamanho Esperado':  lista_tamanho_esperado,
        'Tamanho Calculado': lista_tamanho_calculado,
        'Mesmo Tamanho ?': lista_mesmo_tamanho
    }

    df = pd.DataFrame(dados)
    df.to_csv(arquivo_csv)

    return df