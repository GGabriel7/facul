#include <stdio.h>

int totalEstoque = 100; // Variável global para armazenar o total de itens no estoque

// Procedimento (função sem retorno - void)) para adicionar itens ao estoque
void adicionarEstoque(int quantidade) { // quantidade é um parametro formal
    if (quantidade < 0) {
        printf("Erro: A quantidade a adicionar não pode ser negativa.\n");
        return;
    }
    if (quantidade == 0) {
        printf("Erro: A quantidade a adicionar não pode ser zero.\n");
        return;
    }
    totalEstoque += quantidade;
    printf("Adicionado %d itens ao estoque. Total no estoque: %d\n", quantidade, totalEstoque);
}

// Procedimento (função sem retorno - void) para remover itens do estoque
void removerEstoque(int quantidade) { // quantidade é um parametro formal    
    if (quantidade < 0) {
        printf("Erro: A quantidade a remover não pode ser negativa.\n");
    } else if (quantidade == 0) {
        printf("Erro: A quantidade a remover não pode ser zero.\n");
    } else if (quantidade <= totalEstoque) {
        totalEstoque -= quantidade;
        printf("Removido %d itens do estoque. Total no estoque: %d\n", quantidade, totalEstoque);
    } else {
        printf("Erro: Não há itens suficientes no estoque para remover %d itens.\n", quantidade);
    }
}

int main() {
    int opcao, quantidade;

    do {
        printf("Escolha uma opção:\n");
        printf("1. Adicionar itens ao estoque.\n");
        printf("2. Remover itens do estoque.\n");
        printf("3. Ver total de itens no estoque.\n");
        printf("4. Sair.\n");
        printf("Opção: ");

        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite a quantidade a adicionar: ");
                scanf("%d", &quantidade);
                adicionarEstoque(quantidade);
                break;

            case 2:
                printf("Digite a quantidade a remover: ");
                scanf("%d", &quantidade);
                removerEstoque(quantidade);
                break;

            case 3:
                printf("Total de itens no estoque: %d\n", totalEstoque);
                break;
            
            case 4:
                printf("Saindo do programa...\n");
                break;

            default:
                printf("Opção inválida. Tente novamente.\n");
                break;
        }
    } while (opcao != 4); // O loop continua até que o usuário escolha a opção 4 (sair)

    printf("Pressione Enter para sair...");
    getchar(); // consome o '\n' restante
    getchar(); // espera o Enter final

    return 0;
}