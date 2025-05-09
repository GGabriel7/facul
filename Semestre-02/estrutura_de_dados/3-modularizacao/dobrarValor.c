#include <stdio.h>
#include <stdlib.h>

void dobrarValorVal(int valor) {
    valor *= 2;
    printf("Valor dobrado (dentro da função por valor): %d\n", valor);
}

void dobrarValorRef(int *valor) {
    *valor *= 2;
    printf("Valor dobrado (dentro da função por referência): %d\n", *valor);
}

int main() {
    int  valor = 10;

    //Passagem por valor
    printf("Valor original: %d\n", valor);
    dobrarValorVal(valor); // Passagem por valor
    printf("Valor após dobrar por valor: %d\n", valor); // Valor não alterado

    // Passagem por referência
    printf("Valor original: %d\n", valor);
    dobrarValorRef(&valor); // Passagem por referência no endereço, necessário o utilizar &
    printf("Valor após dobrar por referência: %d\n", valor); // Valor alterado
    
    system("pause");
    return 0;
}