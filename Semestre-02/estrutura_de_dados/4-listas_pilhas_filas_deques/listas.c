1. Alocação sequencial:
    Alocação sequencial, como o nome já diz, é uma alocação sequencial na memória. Inicia-se com um ponteiro para o primeiro elemento (0) e, a partir dele, os outros elementos são alocados sequencialmente na memória. Isso significa que todos os elementos estão contidos em um único bloco de memória. 

    int vetor[10]; // vetor de 10 inteiros
    vetor[4] = 50; // alocando o valor 50 na posição 4 (5°) do vetor.

    Compreender o que é alocação sequencial vai lhe ajudar não apenas no entendimento de como estruturas tais quais listas, filas e pilhas funcionam, mas também na compreensão do mecanismo da alocação dinâmica.


2. Listas lineares genericas:
    Listas lineares genéricas são listas que podem armazenar qualquer tipo de dado, até os complexos. Elas são implementadas usando ponteiros, o que permite que os elementos sejam alocados em qualquer lugar da memória. Isso significa que os elementos não precisam estar contidos em um único bloco de memória, como nas listas sequenciais. 

    typedef struct {
        void *dados; // ponteiro para os dados
        int tamanho; // tamanho dos dados
    } ListaGenerica;