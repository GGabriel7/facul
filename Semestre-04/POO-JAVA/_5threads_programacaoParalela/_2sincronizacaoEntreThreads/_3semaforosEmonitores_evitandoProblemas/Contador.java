package _3semaforosEmonitores_evitandoProblemas;

import java.util.concurrent.Semaphore;

public class Contador {
    private volatile int contador = 0; //volatile funciona como uma barreira de memória, garantindo que as alterações sejam visíveis para todas as threads
    private final Semaphore semaforo = new Semaphore(1); // Inicializa o semáforo com 1 permissão

    public synchronized void incrementar() {
        //synchronized é usado para garantir que apenas uma thread possa acessar o método incrementar() por vez, evitando condições de corrida

        try {
            semaforo.acquire(); //adquire a permissão do semáforo, bloqueando se já estiver em uso por outra thread
            contador++;
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // Restaura o status de interrupção da thread
            throw new RuntimeException("Thread interrompida", e); // Lança uma exceção para indicar que a thread foi interrompida
        } finally {
            semaforo.release(); // Libera a permissão do semáforo, permitindo que outras threads acessem o contador
        }
    }

    public int getContador() {
        return contador; // Retorna o valor atual do contador
    }
}
