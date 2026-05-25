package _2usoDeHeranca;

public class _3Aluno extends _3PessoaFisica {
    String matricula;

    public _3Aluno (String nome, String CPF, String matricula) {
        super(nome, CPF);
        this.matricula = matricula;
    }

    public void setMatricula (String matricula) {
        this.matricula = matricula;
    }

    public String getMatricula () {
        return matricula;
    }

    @Override // sobrescreve o método toString da classe Object para exibir as informações do alunoo.
    public String toString () {
        return String.format("ObjID: %s => Nome:%s | CPF:%s | Matricula: %S\\n", Integer.toHexString(this.hashCode()), nome, CPF, matricula);
    }
}