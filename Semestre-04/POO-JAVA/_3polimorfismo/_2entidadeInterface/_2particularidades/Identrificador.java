package _2entidadeInterface._2particularidades;

public interface Identrificador {
    //interface é um contrato que define um conjunto de métodos que uma classe deve implementar sem fornecer uma implementação concreta. Ela é usada para definir um comportamento comum que pode ser compartilhado por várias classes, independentemente de sua hierarquia de herança.
    
    final int tamanhoMax = 21; //final significa que o valor não pode ser alterado.
    boolean validarID(String id); // void significa que o método não retorna nenhum valor.
    void formatarID(int tipo);
    void atualizarID(String id);
    String recuperarID();
}
