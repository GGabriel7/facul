import java.util.Random; // Importa a classe Random para gerar números aleatórios

public class Aluno {
    // Atributos
    private String nome;
    private int idade;

    private Endereco endereco; // Associação: O aluno tem um endereço, mas o endereço pode existir independentemente do aluno
    private Curso cursos[]; // Agregação: O aluno pode estar matriculado em vários cursos, mas os cursos podem existir independentemente do aluno
    private Matricula matricula; // Composição: O aluno tem uma matrícula, e a matrícula depende do aluno para existir

    private double codigo_id;
    private Random aleatorio;

    // Construtor
    public Aluno(String nome, int idade, Endereco endereco, Curso[] cursos) {
        aleatorio = new Random();

        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
        this.cursos = cursos;
        this.matricula = new Matricula(String.valueOf(aleatorio.nextDouble() + 5));
        this.codigo_id = aleatorio.nextDouble() + 1; // Gera um número aleatório para o código de identificação
    }

    // Métodos
    public void definirNome(String nome) {
        this.nome = nome;
    }
    public void definirIdade(int idade) {
        this.idade = idade;
    } // Esse métodos servem para definir o nome e a idade do aluno, respectivamente. Eles recebem um parâmetro (nome ou idade) e atribuem esse valor ao atributo correspondente da classe Aluno usando a palavra-chave 'this' para se referir ao objeto atual.
    public void definirEndereco(Endereco endereco) {
        this.endereco = endereco;
    } 
    public void adicionarCurso(Curso curso) {
        // Cria um novo array com tamanho maior para adicionar o novo curso
        Curso[] novosCursos = new Curso[cursos.length + 1];
        System.arraycopy(cursos, 0, novosCursos, 0, cursos.length); // Copia os cursos existentes para o novo array
        novosCursos[cursos.length] = curso; // Adiciona o novo curso ao final do array
        cursos = novosCursos; // Atualiza a referência do array de cursos
    }
    public void definirMatricula(Matricula matricula) {
        this.matricula = matricula;
    }

    public static void main(String[] args) {

        Aluno aluno1 = new Aluno("Gabriel", 22, new Endereco("Rua A", "Cidade B"), new Curso[]{new Curso("Matemática"), new Curso("Física")});

        System.out.println("Nome: " + aluno1.nome);
        System.out.println("Idade: " + aluno1.idade);
        System.out.println("Código: " + aluno1.codigo_id);
        System.out.println("Endereço: " + aluno1.endereco);
        System.out.println("Matrícula: " + aluno1.matricula);
        System.out.println("Cursos: " + aluno1.cursos.length);
    }
}

// Associação
class Endereco {
    private String rua;
    private String cidade;

    public Endereco(String rua, String cidade) {
        this.rua = rua;
        this.cidade = cidade;
    }
}

// Agregação
class Curso {
    private String nome;

    public Curso(String nome) {
        this.nome = nome;
    }
}

// Composição
class Matricula {
    private String numero;

    public Matricula(String numero) {
        this.numero = numero;
    }
}