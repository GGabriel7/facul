package _2entidadeInterface._2particularidades;

import java.util.Calendar;

public class Pessoa implements iPessoa, Identrificador{
    int idade;
    String nome = "", nacionalidade ="", id="";

    public void atualizarNome(String nome) {
        if (!nome.isBlank()) // isBlank é um método da classe String que verifica se a string está em branco (vazia ou composta apenas por espaços em branco)
            this.nome = nome;
        else
            System.out.println("ERRO: nome em branco!");
    }

    public String recuperarNome() {
        return this.nome;
    }

    public void atualizarID(String id) {
        this.id = id;
    }

    public String recuperarID() {
        return this.id;
    }

    public void formatarID(int id){
        this.id = String.valueOf(id); // valueOf é um método da classe String que converte um valor em String
    }

    public boolean validarID(String id) {
        if (id.isBlank() || id.isEmpty())
            return false;
        else
            return true;
    }

    public String recuperarNacionalidade() {
        return this.nacionalidade;
    }

    public void atualizarIdade(Calendar data_inicio_existencia) {
        this.idade = calcularIdade(data_inicio_existencia);
    }
    public int recuperarIdade() {
        return this.idade;
    }

    public int calcularIdade(Calendar data_inicio_existencia) {
        // criando uma data de inicio e subtraindo a data atual para obter a idade
        Calendar data_atual = Calendar.getInstance();
        int idade = data_atual.get(Calendar.YEAR) - data_inicio_existencia.get(Calendar.YEAR);
        if (data_atual.get(Calendar.MONTH) < data_inicio_existencia.get(Calendar.MONTH) || (data_atual.get(Calendar.MONTH) == data_inicio_existencia.get(Calendar.MONTH) && data_atual.get(Calendar.DAY_OF_MONTH) < data_inicio_existencia.get(Calendar.DAY_OF_MONTH))) {
            idade--;
        }
        return idade;
    }
}
