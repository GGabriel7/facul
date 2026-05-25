import java.util.Calendar;

public class Empregado extends Pessoa {
    // atributos
    protected String matricula;
    private Calendar dataAdmissao, dataDemissao;

    // métodos
    public Empregado(String nome, Calendar dataNascimento, long CPF, Endereco endereco) {
        super(nome, dataNascimento, CPF, endereco);
        this.matricula = gerarMatricula();
        dataAdmissao = Calendar.getInstance();
    }

    public void demitirEmpregado() {
        dataDemissao = Calendar.getInstance();
    }

    protected void gerarMatricula() {
        this.matricula = "Matricula não definida.";
    }

    protected String recuperarMatricula() {
        return this.matricula;
    }
} 
