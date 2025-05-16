#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>

#define TAMANHO 10000

int vetor[TAMANHO];
int vetorBolha[TAMANHO];
int vetorSelecao[TAMANHO];
int vetorInsercao[TAMANHO];

int menu();
void imprimir(int *vetor);
void carregarExemplo();
void carregarExemplos();
void bolha(int *vetor);
void selecao(int *vetor);
void insercao(int *vetor);

int main ()
{
    while(menu());
}

int menu()
{
    int opcao;
    clock_t Ticks[2];
    int fImprimir = 0;
    
    system("cls");
    printf("\n Digite: ");
    printf("\n 0. Sair");
    printf("\n 1. Bolha");
    printf("\n 2. Selecao");
    printf("\n 3. Insercao");
    printf("\n 4. Executar os 4 algoritmos");
    printf("\n");
    scanf("%d", &opcao);

    switch (opcao)
    {
        case 0:return 0;

        case 1:
        {
            carregarExemplo();

            if (fImprimir)
            {
                printf("\n Antes da ordenação: ");
                imprimir(vetor);
            }

            Ticks[0] = clock();
            bolha(vetor);
            Ticks[1] = clock();
            double Tempo = (Ticks[1] - Ticks[0]) * 1000.0 / CLOCKS_PER_SEC;
            printf("\n Tempo de execucao: %fms", Tempo);

            if (fImprimir)
            {
                printf("\n Depois da ordenação: ");
                imprimir(vetor);
            }

            printf("\n\n Pressione qualquer tecla para continuar...");
            system("pause");
            return 1;
        }

        case 2:
        {
            carregarExemplo();

            if (fImprimir)
            {
                printf("\n Antes da ordenação: ");
                imprimir(vetor);
            }

            Ticks[0] = clock();
            selecao(vetor);
            Ticks[1] = clock();
            double Tempo = (Ticks[1] - Ticks[0]) * 1000.0 / CLOCKS_PER_SEC;
            printf("\n Tempo de execucao: %fms", Tempo);

            if (fImprimir)
            {
                printf("\n Depois da ordenação: ");
                imprimir(vetor);
            }

            printf("\n\n Pressione qualquer tecla para continuar...");
            system("pause");
            return 1;
        }

        case 3:
        {
            carregarExemplo();

            if (fImprimir)
            {
                printf("\n Antes da ordenação: ");
                imprimir(vetor);
            }

            Ticks[0] = clock();
            insercao(vetor);
            Ticks[1] = clock();
            double Tempo = (Ticks[1] - Ticks[0]) * 1000.0 / CLOCKS_PER_SEC;
            printf("\n Tempo de execucao: %fms", Tempo);

            if (fImprimir)
            {
                printf("\n Depois da ordenação: ");
                imprimir(vetor);
            }

            printf("\n\n Pressione qualquer tecla para continuar...");
            system("pause");
            return 1;
        }

        case 4:
        {
            carregarExemplos();

            if (fImprimir)
            {
                printf("\n Antes da ordenação: ");
                printf("[BOLHA]\n");
                imprimir(vetorBolha);
                printf("[SELECAO]\n");
                imprimir(vetorSelecao);
                printf("[INSERCAO]\n");
                imprimir(vetorInsercao);
            }

            Ticks[0] = clock();
            bolha(vetorBolha);
            Ticks[1] = clock();
            double TempoBolha = (Ticks[1] - Ticks[0]) * 1000.0 / CLOCKS_PER_SEC;
            printf("\n Tempo de execucao BOLHA: %fms", TempoBolha);

            Ticks[0] = clock();
            selecao(vetorSelecao);
            Ticks[1] = clock();
            double TempoSelecao = (Ticks[1] - Ticks[0]) * 1000.0 / CLOCKS_PER_SEC;
            printf("\n Tempo de execucao SELECAO: %fms", TempoSelecao);

            Ticks[0] = clock();
            insercao(vetorInsercao);
            Ticks[1] = clock();
            double TempoInsercao = (Ticks[1] - Ticks[0]) * 1000.0 / CLOCKS_PER_SEC;
            printf("\n Tempo de execucao INSERCAO: %fms", TempoInsercao);

            if(fImprimir)
            {
                printf("\n Depois da ordenação: ");
                printf("[BOLHA]\n");
                imprimir(vetorBolha);
                printf("[SELECAO]\n");
                imprimir(vetorSelecao);
                printf("[INSERCAO]\n");
                imprimir(vetorInsercao);
            }

            printf("\n\n Pressione qualquer tecla para continuar...");
            system("pause");
            return 1;
        }

        default:
            printf("\n Opcao invalida");
            printf("\n\n Pressione qualquer tecla para continuar...");
            system("pause");
            return 1;
    }
}

void imprimir(int *vetor)
{
    int i;
    for (i = 0; i < TAMANHO; i++)
    {
        printf("%d ", vetor[i]);
    }
}

void carregarExemplo()
{
    int i;
    for (i = 0; i < TAMANHO; i++)
    {
        vetor[i] = rand() % 1000;
    }
}

void carregarExemplos()
{
    int i;
    for (i = 0; i < TAMANHO; i++)
    {
        int a = rand() % 100;
        vetorBolha[i] = a;
        vetorSelecao[i] = a;
        vetorInsercao[i] = a;
    }
}

void bolha(int *vetor)
{
    int i, j, aux;
    int troca = 1;

    for (i = 0; i < TAMANHO - 1 && troca; i++)
    {
        troca = 0;
        for (j = 0; j < TAMANHO - 1 - i; j++)
        {
            if (vetor[j] > vetor[j + 1])
            {
                aux = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = aux;
                troca = 1;
            }
        }
    }
}

void selecao(int *vetor)
{
    int i, j, aux, posMinimo;
    for (i = 0; i < TAMANHO - 1; i++)
    {
        posMinimo = i;
        for (j = i + 1; j < TAMANHO; j++)
        {
            if (vetor[j] < vetor[posMinimo])
            {
                posMinimo = j;
            }
        }
        aux = vetor[i];
        vetor[i] = vetor[posMinimo];
        vetor[posMinimo] = aux;
    }
}

void insercao(int *vetor)
{
    int i, j, aux;
    for (i=1; i < TAMANHO-1; i++)
    {
        aux = vetor[i];
        j=i+1;

        while (j > 0 && vetor[j] > aux)
        {
            vetor[j + 1] = vetor[j];
            j--;
        }
        vetor[j + 1] = aux;
    }
}