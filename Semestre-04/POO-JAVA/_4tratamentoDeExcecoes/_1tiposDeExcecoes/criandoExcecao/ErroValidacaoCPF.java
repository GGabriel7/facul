package criandoExcecao;

public class ErroValidacaoCPF extends Throwable {
    // extende a classe Throwable, que é a classe base para todas as exceções e erros em Java. Como qualquer classe derivada de Throwable, um objeto dessa subclasse conterá um instantâneo da pilha de execução de sua thread no momento em que foi criado.
    
    private String msgErro;

    ErroValidacaoCPF(String msgErro) {
        this.msgErro = msgErro;
    }

    @Override
    public String toString() {
        return "ErroValidacaoCPF: " + msgErro;
    }
}
