package _1polimorfismoEmJava._4polimorfismo;

import java.util.Calendar;

public class Principal {
    private static Pessoa [] vetor;
    private static Calendar data_inicial = Calendar.getInstance ( );

    public static void main(String [] args) {
        vetor = new Pessoa[6];
        String data[];
        
        // criando pessoas fisicas
        data_inicial.set(2000,01,01);
        vetor[0] = new Fisica("Carlos", data_inicial, "12345678900", "Brasileira");

        data_inicial.set(1990, 02,10);
        vetor[1] = new Fisica("Maria", data_inicial, "00987654321", "Portugeusa");

        data_inicial.set(1998,12, 12);
        vetor[2] = new Fisica("Gabriel", data_inicial, "18274622789", "Brasileira");

        // criando pessoas Juridicas
        data_inicial.set(2001, 02,11);
        vetor[3] = new Juridica("Java", data_inicial, "25967538000120", "Bogotá");

        data_inicial.set(1975, 07, 10);
        vetor[4] = new Juridica("Carls Bergs", data_inicial, "12595436000132", "São Paulo");

        data_inicial.set(2013, 05,05);
        vetor[5] = new Juridica("Web Cursos", data_inicial, "62526486000132", "Fortaleza");

        for(int i=0; i<vetor.length; i++) {
            System.out.println(String.format("DENOMINACAO: %s - ID: %s", vetor[i].recuperarNome(), vetor[i].recuperarID()));
        }
    }
}