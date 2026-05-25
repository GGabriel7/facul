package _1polimorfismoEmJava._4polimorfismo;

import java.util.Calendar;

public class Fisica extends Pessoa {
    String nacionalidade;

    public Fisica(String nome, Calendar dataNasc, String CPF, String nacionalidade) {
        super(nome, dataNasc, ""); // nome, data e id de Pessoa
        atualizarID(CPF);
        this.nacionalidade = nacionalidade;
    }

    public String recuperarNacionalidade ( ) {
        return nacionalidade;
    }

    @Override
    public boolean atualizarID ( String CPF ) {
        if ( validarID ( CPF ) ) {
               this.id = CPF;
               return true;
        }
        else {
               System.out.println ( "CPF invalido!" );
               return false;
        }
    }

    @Override
    public String recuperarNome ( ) {
        return "<NOME> " + this.nome;
    }

    protected String recuperarID ( ) {
        return String.format ( "%s.%s.%s-%s" , id.substring ( 0 , 3 ) , id.substring ( 3 , 6 ) , id.substring ( 6 , 9 ) , id.substring ( 9 ) );
    }

    @Override
    public String toString (){
        return "Objeto:" + "\n\t- Classe: " + getClass().getName() + "\n\t- Hash: " + Integer.toHexString(hashCode()) + "\n\t- Nome: " + nome + "\n\t- Identificador: " + id;
    }

    private boolean validarID ( String CPF ) {
        //verifica sequência de dígitos iguais e tamanho (11 dígitos)
        if ( ! ( CPF.chars ( ).allMatch ( Character::isDigit ) ) ) {
            System.out.println ( "CPF possui caracteres não numéricos!" );
            return false;
        }
        else if ( ( CPF.length() != 11 ) || CPF.matches( "[0]{11}|[1]{11}|[2]{11}|[3]{11}|[4]{11}|[5]{11}|[6]{11}|[7]{11}|[8]{11}|[9]{11}" ) )
        return false;
    return true;
    }
}