package _1semaforoEmonitores;

import java.util.concurrent.Semaphore;

// as técnicas de semaforo e monitores são usadas para controlar o acesso a recursos compartilhados entre threads, evitando condições de corrida e garantindo a sincronização adequada.

// processo do semaforo: é feito a solicitação de acesso a um recurso compartilhado, o semáforo verifica se o recurso está disponível. Se estiver disponível, o semáforo concede acesso à thread solicitante e decrementa seu contador interno. Se o recurso não estiver disponível, a thread solicitante é bloqueada até que o recurso seja liberado por outra thread.

// Acquire() é o método que uma thread chama para solicitar acesso a um recurso protegido por um semáforo. Se o recurso estiver disponível, o método decrementa o contador do semáforo e permite que a thread continue sua execução. Se o recurso não estiver disponível, a thread é bloqueada até que o recurso seja liberado por outra thread.

// Realease() é o método que uma thread chama para liberar um recurso protegido por um semáforo. Quando uma thread chama release(), o contador do semáforo é incrementado, indicando que o recurso está disponível novamente. Se houver threads bloqueadas esperando por esse recurso, uma delas será desbloqueada e poderá adquirir o recurso.

public class PingPong {
    private Semaphore s1, s2; // semáforos para controlar o acesso às threads
    private Ping ping; // Usar a classe Ping para criar a thread de ping
    private Pong pong; // Usar a classe Pong para criar a thread de pong
    private Controle contador;
    private int tamanhoPartida;

    public PingPong(int tamanhoPartida) throws InterruptedException {
        s1 = new Semaphore(0);
        s2 = new Semaphore(0);
        contador = new Controle(tamanhoPartida);
        ping = new Ping(s1, s2, contador);
        pong = new Pong(s1, s2, contador);

        new Thread(ping).start(); // Inicia a thread de ping
        new Thread(pong).start(); // Inicia a thread de pong
        s1.release(); // Libera o semáforo para iniciar a partida
    }
}