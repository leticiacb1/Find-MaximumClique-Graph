#include "display-result.h"

#include<iostream>
#include<vector>
#include <fstream>
#include<algorithm>

using namespace std;

void displayResult(string choose_algorithm, vector<int> cliqueMaximo){
    /*
    * Mostra resultado do algorítimo na tela
    */

    cout << " ===== [" + choose_algorithm + "] ===== \n";
    cout << "\n > Clique Máxima encontrada : [";
    for (auto &el : cliqueMaximo) {
      cout << el+1 << " ";
    }
    cout << "] \n";
    cout << "\n > Tamanho : " << cliqueMaximo.size();
}