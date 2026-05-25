package _2entidadeInterface._2particularidades;

import java.util.Calendar;

public interface iPessoa {
    void atualizarNome(String nome);
    String recuperarNome();
    String recuperarNacionalidade();
    void atualizarIdade(Calendar data_inicio_existencia);
    int recuperarIdade();
    int calcularIdade(Calendar data_inicio_existencia);
}
