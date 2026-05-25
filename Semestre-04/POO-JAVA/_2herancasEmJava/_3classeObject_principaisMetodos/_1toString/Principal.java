package _3classeObject_principaisMetodos._1toString;

import java.util.Calendar;

public class Principal {
    private static Pessoa grupo []; // array de objetos do tipo Pessoa, que pode armazenar objetos do tipo Pessoa ou de suas subclasses, como Fisica e Juridica.
    
    public static void main (String args[]) {
        Calendar data_nasc = Calendar.getInstance();

        grupo = new Pessoa [2];

        grupo [0] = new Fisica("Gabriel", data_nasc, "123.456.789-00", "Brasil", "CE");
        grupo [1] = new Fisica("Escola Novo Mundo Ltda", data_nasc, "43.186.666/0026-32", "Brasil", "CE");

        for ( int i = 0 ; i <= 1 ; i++ ) {
            System.out.println( "grupo[" + i + "]: " + grupo[i].toString() );
        }
    }
}
