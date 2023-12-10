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
    cout << "\n > Clique Máxima encontrada : ";

    for (size_t i = 0; i < cliqueMaximo.size(); ++i) {
        std::cout << cliqueMaximo[i] + 1;

        if (i < cliqueMaximo.size() - 1) {
            std::cout << ", ";
        }
    }

    cout << "\n > Tamanho : " << cliqueMaximo.size();
}