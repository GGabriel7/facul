package _3semaforosEmonitores_evitandoProblemas;

import java.util.concurrent.ExecutorService; // Importa a classe ExecutorService para gerenciar um pool de threads, ou seja, uma coleção de threads que podem ser reutilizadas para executar tarefas assíncronas, melhorando a eficiência e o desempenho do programa.
import java.util.concurrent.Executors; // Importa a classe Executors, que fornece métodos estáticos para criar diferentes tipos de pools de threads, como thread pools fixos, thread pools cacheados e thread pools agendados, facilitando a criação e o gerenciamento de threads em aplicações Java.

public class TesteContador {
    public static void main(String[] args) {
        Contador contador = new Contador(); // Cria uma instância da classe Contador, que é responsável por manter um contador e fornecer um método para incrementá-lo de forma segura em um ambiente multithread.

        int numThreads = 10; // Define o número de threads que serão usadas para incrementar o contador, permitindo que várias threads concorram para atualizar o valor do contador simultaneamente.
        int numIncrements = 1000; // Define o número de incrementos que cada thread realizará no contador, garantindo que o contador seja incrementado um total de 10.000 vezes (10 threads x 1.000 incrementos por thread), o que é útil para testar a eficácia da sincronização e a integridade dos dados em um ambiente multithread.

        ExecutorService executor = Executors.newFixedThreadPool(numThreads); // Cria um pool de threads fixo com um número específico de threads, permitindo que as tarefas sejam executadas de forma concorrente e eficiente.

        for (int i = 0; i < numThreads; i++) {
            executor.submit(() -> { // Submete uma tarefa para execução no pool de threads, onde cada tarefa é definida como uma expressão lambda que incrementa o contador um número específico de vezes.
                for (int j = 0; j < numIncrements; j++) {
                    contador.incrementar(); // Chama o método incrementar() do contador para aumentar o valor do contador de forma segura, garantindo que as operações sejam sincronizadas e evitando condições de corrida.
                }
            });
        }
        executor.shutdown(); // Encerra o pool de threads após a conclusão das tarefas

        while (!executor.isTerminated()) {
            // Aguarda até que todas as tarefas sejam concluídas antes de prosseguir
        }
        System.out.println("Valor final do contador: " + contador.getContador()); // Imprime o valor final do contador após todas as threads terem incrementado o contador, demonstrando que a sincronização foi eficaz e o valor é consistente.
    }
}
