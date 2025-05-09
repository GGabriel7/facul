#include <stdio.h>
#include <stdlib.h>

// Prototipo das funções. A função em si será definida depois de main.
float calcularAreaCirculo(float raio);
int calcularAreaRetangulo(float largura, float altura);

int main() {
    float raio = 5.0;
    int largura = 4;
    int altura = 6;

    //Chamando as funções antes de defini-las completamente
    printf("Área do círculo: %.2f\n", calcularAreaCirculo(raio));
    printf("Área do retângulo: %.2f\n", calcularAreaRetangulo(largura, altura));

    system("pause");
    return 0;
}

// Definição das funções
float calcularAreaCirculo(float raio) {
    return 3.14159 * raio * raio; // Fórmula da área do círculo
}

int calcularAreaRetangulo(float largura, float altura) {
    return largura * altura; // Fórmula da área do retângulo
}
// O código acima mostra como usar protótipos de funções para declarar funções antes de defini-las completamente.