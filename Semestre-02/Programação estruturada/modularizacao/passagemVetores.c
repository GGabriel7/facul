#include <stdio.h>
#include <stdlib.h>

int calcularSoma(int vetor[], int tamanho) {
    int soma = 0;

    for (int i = 0; i < tamanho; i++) {
        soma += vetor[i];
    }

    return soma;
}

int main() {
    int lista[5] = {4, 5, 6, 7, 8};
    int tamanho = sizeof(lista) / sizeof(lista[0]);

    int resultado = calcularSoma(lista, tamanho);

    printf("A soma dos elementos do vetor é: %d\n", resultado);

    system("pause");
    return 0;
}