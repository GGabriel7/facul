package _2entidadeInterface._2particularidades;

import java.util.Calendar;

public class Principal {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();
        p1.atualizarNome("Gabriel");
        p1.atualizarID("123456789");
        p1.atualizarIdade(Calendar.getInstance());
        
        System.out.println("Nome: " + p1.recuperarNome());
        System.out.println("ID: " + p1.recuperarID());
        System.out.println("Idade: " + p1.recuperarIdade());
    }
}
