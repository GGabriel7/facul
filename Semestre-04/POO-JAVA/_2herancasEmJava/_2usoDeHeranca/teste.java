package _2usoDeHeranca;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class teste implements Comparator<String> {
    public static void main ( String args [ ] ) {
    List<String> lista_cores = new ArrayList<>();
        lista_cores.add ( "Branco" );
        lista_cores.add ( "azul" );
        lista_cores.add ( "vermelho" );
        lista_cores.add ( "Laranja" );
        lista_cores.add ( "Verde" );
        lista_cores.add ( "branco" );
        lista_cores.add ( "Amarelo" );
        lista_cores.add ( "Preto" );
        System.out.println ( lista_cores );
    }

    @Override
    public int compare ( String obj1 , String obj2 ){
        int cmp;
        if ( ( cmp = obj1.compareTo ( obj2 ) ) < 0 )
            return 1;
        else if ( cmp > 0 )
            return -1;
        else
            return 0;
    }
}
