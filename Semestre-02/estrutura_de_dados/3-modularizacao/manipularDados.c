#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main() {
    char texto[] = "Programacao123";
    int i = 0;

    // Vamos percorrer cada caractere da string
    while (texto[i]) {
        // É letra?
        if (isalpha(texto[i])) {
            printf("%c = uma letra.\n", texto[i]);

            // passando para maiúsculo
            if (islower(texto[i])) {
                texto[i] = toupper(texto[i]);
                printf("Convertido para maiuculo: %c\n", texto[i]);
            }
        }

        // É número?
        else if (isdigit(texto[i])) {
            printf("%c = um número.\n", texto[i]);
        }

        i++;
    }

    printf("Texto tranformado: %s\n", texto);

    system("pause");
    return 0;
}