import java.util.Calendar;

public class Principal {
    // atributos
    private static Aluno aluno;
    private static Endereco endereco;

    //metodo main
    public static void main(String[] args) {
        int idade;
        Calendar data = Calendar.getInstance();
        endereco = new Endereco(null, null);
        endereco.DefinirPais("Brasil");
        endereco.definirUF("SP");
        endereco.definirCidade("São Paulo");
        endereco.definirRua("Rua dos Bobos");
        endereco.definirNumero("0");
        endereco.definirCEP("00000-000");
        endereco.definirComplemento("Casa");
        aluno = new Aluno("Gabriel", data, 12345678910L, endereco);
        aluno.atulizarIdade();
        idade = aluno.recuperarIdade();
        System.out.println("Idade do aluno: " + idade);
        System.out.println("Endereço do aluno: " + aluno.recuperarEndereco().recuperarRua() + ", " + aluno.recuperarEndereco().recuperarCidade() + ", " + aluno.recuperarEndereco().recuperarUF() + ", " + aluno.recuperarEndereco().recuperarPais());
    }
}
