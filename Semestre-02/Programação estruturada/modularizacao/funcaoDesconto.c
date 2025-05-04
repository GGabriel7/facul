#include <stdio.h>

float calcularDesconto(float preco, float percentual) {
    return preco * (percentual / 100);
}

void exibirTotal(float preco, float desconto) {
    float total = preco - desconto;
    printf("Preço: %.2f\n", preco);
    printf("Desconto: %.2f\n", desconto);
    printf("Valor final com desconto: %.2f\n", total);
}

int main() {
    float preco, percentualDesconto, desconto;

    printf("Digite o valor do produto: R$ ");
    scanf("%f", &preco);

    printf("Digite o percentual do desconto: ");
    scanf("%f", &percentualDesconto);

    desconto = calcularDesconto(preco, percentualDesconto);
    exibirTotal(preco, desconto);

    return 0;
}