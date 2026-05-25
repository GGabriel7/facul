package _1polimorfismoEmJava._4polimorfismo;

import java.util.Calendar;

public class Juridica extends Pessoa {
    String cidadeSede;

    public Juridica(String razaoSocial, Calendar dataCriacao, String CNPJ, String cidadeSede) {
        super(razaoSocial, dataCriacao, ""); //nome, data e id de Pessoa
        atualizarID(CNPJ);
        this.cidadeSede = cidadeSede;
    }

    public String recuperarSede ( ) {
        return cidadeSede;
    }

    @Override
    public String recuperarNome ( ) {
        return "<RAZAO SOCIAL> " + this.nome;
    }

    @Override
    public boolean atualizarID(String CNPJ) {
        if (validarID(CNPJ)) {
            this.id = CNPJ;
            return true;
        }
        else {
            System.out.println("CNPJ invalido!");
            return false;
        }
    }

    @Override
    protected String recuperarID ( ) {
        return String.format ( "%s.%s.%s/%s-%s" , id.substring ( 0 , 2 ) , id.substring ( 2 , 5 ) , id.substring ( 5 , 8 ) , id.substring ( 8 , 12 ) , id.substring ( 12 ) );
    }

    @Override
    public String toString (){
        return "Objeto:" + "\n\t- Classe: " + getClass().getName() + "\n\t- Hash: " + Integer.toHexString(hashCode()) + "\n\t- Nome: " + nome + "\n\t- Identificador: " + id;
    }

    private boolean validarID ( String CNPJ ) {
        //verifica sequência de dígitos iguais e tamanho (11 dígitos)
        if ( ! ( CNPJ.chars ( ).allMatch ( Character::isDigit ) ) ) {
            System.out.println ( "CNPJ possui caracteres não numéricos!" );
            return false;
        }
        else if ( ( CNPJ.length() != 14 ) || CNPJ.matches( "[0]{14}|[1]{14}|[2]{14}|[3]{14}|[4]{14}|[5]{14}|[6]{14}|[7]{14}|[8]{14}|[9]{14}" ) )
            return false;
        return true;
    }
}
