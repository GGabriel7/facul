package _3implementacaoDeThreads._1threadsNaPratica;

// esse programa simula uma empresa de empacotamento de produtos, onde há um número limitado de fitas para empacotar os produtos, um número limitado de empregados disponíveis para empacotar os produtos, um número máximo de equipes que podem ser formadas para empacotar os produtos e um número total de produtos a serem empacotados. Cada equipe é composta por um número específico de empregados, e cada empregado é responsável por empacotar um produto. O programa utiliza threads para simular o processo de empacotamento dos produtos pelas equipes, e semáforos e contadores sincronizados para controlar o acesso às fitas e aos produtos disponíveis. O programa também gera relatórios detalhados sobre o processo de empacotamento, incluindo o número de empacotamentos realizados por cada equipe e por cada empregado, e as threads envolvidas em cada empacotamento.

public class Principal {
    private static Empresa ACME;

    //Métodos
    public static void main ( String args [ ] ) throws InterruptedException {
        // Empresa (número de fitas, empregados disponíveis, número máximo de equipes, produtos a serem empacotados)
        ACME = new Empresa ( 8, 12, 4, 100 );
    }    
}