package _2usoDeHeranca;

public class _3PessoaFisica {
    protected String CPF;
    protected String nome;

    public _3PessoaFisica (String nome, String CPF) {
        this.nome = nome;
        setCPF (CPF);
    }

    protected void setNome(String nome) {
        this.nome = nome;
    }
    protected String getNome() {
        return nome;
    }

    protected void setCPF(String CPF) {
        if (validarCPF (CPF)) {
            this.CPF = CPF;
        } else {
            System.out.println("CPF inválido!");
        }
    }
    protected String getCPF() {
        return CPF;
    }

    private boolean validarCPF(String CPF) {
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