#include<iostream>
#include<vector>
#include <fstream>
#include<algorithm>

#include "../utils/display-result.h"
#include "../utils/ler-grafo.h"

using namespace std;

// ---------------------------------------------------------------------------
// -------------------------- CLIQUE MÁXIMA ----------------------------------
// ---------------------------------------------------------------------------

int calculaGrau(vector<vector<int>>& grafo, int vertice) {
    /*
    *   Calcula grau de adjacência de um vertice.
    */

    int grau = 0;
    for (int vizinho : grafo[vertice]) {
        if (grafo[vertice][vizinho] == 1) {
            grau++;
        }
    }

    return grau;
}

bool OrdenarPorGrau(int vertice1, int vertice2, vector<vector<int>>& grafo) {
    /*
    *    Função para ordenação de acordo com o grau de adjacẽncia.
    */
    return calculaGrau(grafo, vertice2) - calculaGrau(grafo, vertice1) > 0;
}


vector<int> EncontrarCliqueMaximaHeuristica(vector<vector<int>>& grafo, int numVertices) {
    vector<int> cliqueMaxima;
    vector<int> candidatos;

    for (int i = 0; i < numVertices; i++) {
        candidatos.push_back(i);
    }

    sort(candidatos.begin(), candidatos.end(), [&](int v1, int v2) {
        return OrdenarPorGrau(v1, v2, grafo);
    });

    while (!candidatos.empty()) {
        int v = candidatos.back();
        candidatos.pop_back();

        bool podeAdicionar = true;

        for (int u : cliqueMaxima) {
            if (grafo[u][v] == 0) {
                podeAdicionar = false;
                break;
            }
        }

        if (podeAdicionar) {
            cliqueMaxima.push_back(v);
            vector<int> novosCandidatos;

            for (int u : candidatos) {
                bool adjacenteATodos = true;

                for (int c : cliqueMaxima) {
                    if (grafo[u][c] == 0) {
                        adjacenteATodos = false;
                        break;
                    }
                }

                if (adjacenteATodos) {
                    novosCandidatos.push_back(u);
                }
            }

            sort(novosCandidatos.begin(), novosCandidatos.end(), [&](int u1, int u2) {
                return OrdenarPorGrau(u1, u2, grafo);
            });

            candidatos = novosCandidatos;
        }
    }

    return cliqueMaxima;
}

// ---------------------------------------------------------------------------
// ------------------------------- MAIN --------------------------------------
// ---------------------------------------------------------------------------

int main(int argc, char* argv[]) {

    if(argc != 3 ){
      cout << " [ERROR] Qunatidade errada de argumentos. Esperado = 3 argumentos | Recebeu = " << argc << " argumentos \n";
      return 1;
    }

    string nomeArquivo = argv[1];
    int numVertices = stoi(argv[2]);

    vector<vector<int>> grafo = LerGrafo(nomeArquivo, numVertices);
    vector<int> cliqueMaximo =  EncontrarCliqueMaximaHeuristica(grafo,numVertices);

    displayResult("Busca Exaustiva Local com Heuristica", cliqueMaximo);

    return 0;
}
