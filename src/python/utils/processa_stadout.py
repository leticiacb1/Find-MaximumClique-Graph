#   -------------------------------------------
#   ---- Funções de extração de informação ----  
#   -------------------------------------------

def pega_tamanho(stdout_result):
  '''
    Processa a string de retorno {stdout_result} e busca a informação relacionada
    ao tamanho do clique máximo encontrado.
  '''
  result = stdout_result.split("\n")

  max_clique_tamanho = result[-1]
  max_clique_tamanho = max_clique_tamanho.split(":")[1]

  return max_clique_tamanho

def pega_vertices_max_clique(stdout_result):
  '''
    Processa a string de retorno {stdout_result} e busca a informação relacionada 
    a combinação dos vertices pertencentes ao clique máximo calculado.
  '''
  result = stdout_result.split("\n")

  proc_max_clique = [p for p in result if len(p) > 0]
  proc_max_clique = proc_max_clique[1].split(":")[1]
  proc_max_clique = proc_max_clique.split(",")

  return proc_max_clique