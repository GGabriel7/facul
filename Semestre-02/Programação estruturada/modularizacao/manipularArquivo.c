#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *arquivo; //ponteiro para o arquivo
    char nome[50];
    int idade;

    arquivo = fopen("dados.txt", "w"); //abrir para escrita
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    printf("Digite seu nome: ");
    scanf("%s", nome);
    printf("Digite sua idade: ");
    scanf("%d", &idade);

    //gravando os dados no arquivo
    fprintf(arquivo, "Nome: %s\nIdade: %d\n", nome, idade);

    fclose(arquivo);

    arquivo = fopen("dados.txt", "r"); //abrindo como leitura para ver os dados
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    fscanf(arquivo, "Nome: %s\nIdade: %d\n", nome, &idade);//leio os dados do arquivo

    printf("Dados lidos do arquivo:\n");
    printf("Nome:%s\nIdade: %d\n", nome, idade); //exibo os dados

    fclose(arquivo);

    system("pause");//função para não fazer o arquivo fechar no windows
    return 0;
}