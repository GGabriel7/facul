package _3classeObject_principaisMetodos._1toString;

import java.util.Calendar;

public class Pessoa {
    protected String nome, naturalidade, nacionaldiade, id;
    private Calendar dataInicioExistencia;
    private int idade;

    public Pessoa(String nome, Calendar dataInicioExistencia, String id, String nacionaldiade, String naturaldiade) {
        this.nome = nome;
        this.dataInicioExistencia = dataInicioExistencia;
        this.id = id;
        this.nacionaldiade = nacionaldiade;
        this.naturalidade = naturaldiade;
    }

    @Override // @override serve para indicar que o metodo abaixo é uma sobrescrita de um metodo da classe  pai
    public String toString() {
        // toString permite pegar o objeto e retornar uma represeção em string dele.
        return getClass().getName() + "@" + Integer.toHexString(hashCode()) + "\n\t- Nome: " + nome + "\n\t- Id: " + id; // pegamos métodos da classe Object, como “getClass” e “hashCode”, seguido por símbolo de “@” e, após este, do código hash do objeto
    }
}
