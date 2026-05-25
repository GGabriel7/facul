package _2usoDeHeranca;

import java.util.Comparator; // Compara objetos de uma classe, implementando a interface Comparator<T>

public class _3ComparaPessoa implements Comparator<_3PessoaFisica> {
    // implements serve para implementar uma interface, ou seja, o classe _3ComparePessoa deve implementar os métodos definidos na interface Comparator<T>. A diferença para o extends é que extends é usado para herdar de uma classe, enquanto implements é usado para implementar uma interface. 

    @Override // Sobrescreve o método compare da interface Comparator<T>
    public int compare(_3PessoaFisica p1, _3PessoaFisica p2) {
        return p1.getNome().compareTo(p2.getNome()); // Compara os nomes das pessoas
    } 
}