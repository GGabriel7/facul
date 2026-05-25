package _1polimorfismoEmJava._4polimorfismo;

import java.util.Calendar; //importação da classe Calendar para trabalhar com datas

public abstract class Pessoa {
    protected String nome;
    protected Calendar dataInicio;
    protected String id;

    public Pessoa(String nome, Calendar dataInicio, String id) {
        this.nome = nome;
        this.dataInicio = dataInicio;
        this.id = id;
    }

    public String recuperarNome ( ) {
        return this.nome;
    }

    protected abstract boolean atualizarID(String id);
    protected abstract String recuperarID();
    // por serem metodos abstratos, não possuem implementação na classe Pessoa, e devem ser implementados nas classes filhas (Fisica e Juridica) obrigatoriamente (em caso de não implementação, as classes filhas devem ser abstratas também)
}