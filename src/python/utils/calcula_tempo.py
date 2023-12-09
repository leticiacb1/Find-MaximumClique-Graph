import subprocess
import time
import os

def calcula_tempo(algoritimo, filename_grafo ,debug = False):
    '''
        Roda algorítimo com arquivo de grafo específico comoo entrada e calcula o tempo de execução.
    '''
    
    command = ["./" + algoritimo + " " + filename_grafo]
    
    start = time.perf_counter()
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    end = time.perf_counter()

    delta = end - start

    if(debug):
        print(f"\n [INFO] Calculando {algoritimo} | filename = {filename_grafo} \n")
        print("\n [TIMER] " + str(delta) + " segundos\n\n")

    return delta


if __name__ == "__main__":

    algoritimo = "../../implementations/algorithm/busca_exaustiva_global"
    filename = "../../../data/graphs/grafo.txt"

    if not os.path.exists(algoritimo):
        print(f"\n [ERROR] Arquivo {algoritimo} não existe! \n")  
    elif not os.path.exists(filename):
        print(f"\n [ERROR] Arquivo {filename} não existe! \n")  
    else:
        calcula_tempo(algoritimo, filename_grafo ,debug = False)
    

