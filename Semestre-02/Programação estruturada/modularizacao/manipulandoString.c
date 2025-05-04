#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char nome1[50] = "Joao";
    char nome2[] = "Gabriel";

    //Concatenando String
    strcat(nome1, nome2);
    printf("Nome completo: %s\n", nome1);

    //medindo tamanhho
    int comprimento = strlen(nome1);
    printf("Comprimento do nome completo: %d\n", comprimento);

    // comparando
    if (strcmp(nome1, "Joao Gabriel") == 0) {
        printf("As strings são iguais.\n");
    } else {
        printf("As strings são diferentes.\n");
    }

    //copiando
    char copia[50];
    strcpy(copia, nome1);
    printf("Cópia do nome: %s\n", copia);

    system("pause");
    return 0;
}