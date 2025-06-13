#include <stdio.h>

int main() {
    FILE *fpTexto, *fpBinario; //Declarando ponteiros para arquivos de texto e binários
    char nome[100]; // Declara um array de caracteres para armazenar o nome do participante
    int contador = 0; // Declara e inicializa uma variável inteira para o contador de participantes

    // Abertura dos arquivos
    fpTexto = fopen("participantes.txt", "a+"); // Abre (ou cria) o arquivo de texto para leitura e escrita no final
    fpBinario = fopen("contador.bin", "rb+"); // Abre (ou cria) o arquivo binário no modo de leitura e escrita

    if (fpBinario == NULL) {
        // Se o arquivo binário não existe, cria um novo modo escrita e leituuraa ("wb+")
        fpBinario = fopen("contador.bin", "wb+");
        fwrite(&contador, sizeof(int), 1, fpBinario); // Escreve o contador inicial no arquivo binário
    } else {
        // Se o arquivo binário já existe, lê o contador existente
        fread(&contador, sizeof(int), 1, fpBinario);
    }

    printf("Digite o nome do participante: ");
    scanf(" %[^\n]", nome); // Lê o nome do participante, permitindo espaços

    fprintf(fpTexto, "%s\n", nome); // Escreve o nome do participante no arquivo de texto
    contador++; // Incrementa o contador de participantes
    rewind(fpBinario); // Volta ao início do arquivo binário
    fwrite(&contador, sizeof(int), 1, fpBinario); // Atualiza o contador no arquivo binário

    fclose(fpTexto); // Fecha o arquivo de texto
    fclose(fpBinario); // Fecha o arquivo binário

    printf("Participante adicionado com sucesso!\n");
    printf("Total de participantes: %d\n", contador); // Exibe o total de participantes

    return 0; // Retorna 0 para indicar que o programa terminou com sucesso
