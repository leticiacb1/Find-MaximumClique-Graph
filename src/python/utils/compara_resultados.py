def calcula_esperado_e_calculado(command):
  # ---- Resultado Esperado ----
  cliqueMaximo_esperado = cliqueMaximo_Resposta()

  # ---- Resultado Obtido ----
  result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  clique_calculado = result.returncode

  return cliqueMaximo_esperado, clique_calculado


def compara_resultados(lista_vertices, lista_commandos, algoritimos, arquivo_csv):
  '''
    Monta uma tabela com a comparação dos resultados obtidos.
    Salva os dados em um excel.
  '''

  lista_valores_calculados = []
  lista_valores_esperados = []

  lista_tamanho_calculado = []
  lista_tamanho_esperado = []
  lista_mesmo_tamanho = []

  lista_algoritimos = []
  lista_vertices_df = []

  for command , algoritimo in zip(lista_commandos, algoritimos):
    for vertices in lista_vertices:
        calculado, esperado = calcula_esperado_e_calculado(command)

        lista_valores_calculados.append(calculado)
        lista_valores_esperados.append(esperado)

        lista_algoritimos.append(algoritimo)

        lista_tamanho_calculado.append(len(calculado))
        lista_tamanho_esperado.append(len(esperado))

        lista_vertices_df.append(vertices)

        lista_mesmo_tamanho.append("Sim" if (len(calculado) == len(esperado)) else "Não")

  dados = {
      'Algoritimo': lista_algoritimos ,
      'Vertices' : lista_vertices_df,
      'Clique Esperado': lista_valores_esperados,
      'Clique Calculado': lista_valores_calculados,
      'Tamanho Clique Esperado':  lista_tamanho_esperado,
      'Tamanho Clique Calculado': lista_tamanho_calculado,
      'Mesmo Tamanho ?': lista_mesmo_tamanho
  }

  df = pd.DataFrame(dados)
  df.to_csv(arquivo_csv)

  return df


  if __name__ == "__main__":
    
    lista_vertices = [i for i in range(5)]
    
    lista_commandos = ['./algorithm/0-busca-exaustiva-local grafo.txt']
    algoritimos = 'busca-exaustiva-local'

    arquivo_csv = "../../../data/analysis/teste.csv"

    #compara_resultados(lista_vertices = lista_vertices , lista_commandos = lista_commandos , algoritimos = algoritimos , arquivo_csv = arquivo_csv)