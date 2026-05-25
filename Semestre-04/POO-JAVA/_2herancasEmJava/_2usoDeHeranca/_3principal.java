package _2usoDeHeranca;

import java.util.SortedSet;
import java.util.TreeSet;

public class _3principal {
    private static SortedSet<_3Aluno> cj_ordenado; // SortedSet é uma interface que define um conjunto ordenado de elementos, ou seja, os elementos são armazenados em uma ordem específica, geralmente definido por um comparador ou pela ordem natural dos elementos. 

    public static void main(String[] args) {
        cj_ordenado = new TreeSet<_3Aluno>(new _3ComparaPessoa()); // TreeSet é uma implementação concreta da interface SortedSet que utiliza uma árvore de busca binária para armazenar os elementos em ordem crescente.
        cj_ordenado.add(new _3Aluno("Martins" , "12345678912" , "M1"));
        cj_ordenado.add(new _3Aluno("Paula" , "12345678912" , "M2"));
        cj_ordenado.add(new _3Aluno("Carla" , "36925814774" , "M3"));
        cj_ordenado.add(new _3Aluno("Martins" , "45678912336" , "M4"));
        System.out.println(cj_ordenado);
    }
}