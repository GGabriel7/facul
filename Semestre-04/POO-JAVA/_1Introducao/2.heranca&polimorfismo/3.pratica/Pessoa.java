import java.util.Calendar;

public class Pessoa {
    //atributos
    private String nome;
    private int idade;
    private Calendar dataNascimento;
    private long CPF;
    private Endereco endereco;

    //métodos
    public Pessoa(String nome, Calendar dataNascimento, long CPF, Endereco endereco) {
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.CPF = CPF;
        this.endereco = endereco;
        atualizarIdade();
    }

    protected void atualizarNome(String nome) {
        this.nome = nome;
    }

    protected String recuperarNome() {
        return nome;
    }

    protected void atualizarIdade() {
        Calendar dataAtual = Calendar.getInstance();
        int anoAtual = dataAtual.get(Calendar.YEAR);
        int anoNascimento = dataNascimento.get(Calendar.YEAR);
        this.idade = anoAtual - anoNascimento;
    }

    protected int recuperarIdade() {
        return idade;
    }

    protected void atualizarCPF(long CPF) {
        this.CPF = CPF;
    }

    protected long recuperarCPF() {
        return CPF;
    }

    protected void atualizarEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    protected Endereco recuperarEndereco() {
        return endereco;
    }

    private int calcularIdade() {
        Calendar dataAtual = Calendar.getInstance();
        int anoAtual = dataAtual.get(Calendar.YEAR);
        int anoNascimento = dataNascimento.get(Calendar.YEAR);
        return anoAtual - anoNascimento;
    }
}