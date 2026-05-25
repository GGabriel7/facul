// Herança: é um mecanismo que permite criar uma nova classe a partir de uma classe existente, herdando seus atributos e métodos. Ela promove a reutilização de código e a criação de hierarquias de classes, facilitando a organização e manutenção do código.

import java.util.UUID; // cria IDs únicos que será utilizando para gerar matriculas

// Pacotes - Servem para organizar as classes em grupos relacionados, evitando conflitos de nomes. Eles também ajudam a controlar o acesso às classes e seus membros.
//package _1hierarquiaDeHeranca;

// Classe base (superclasse) - será utilizada para criar outras classes.
class Pessoa {
    // atributos comuns de todas as pessoas
    protected String nome, nacionalidade, naturalidade; //protected permite que as subclasses acessem esses atributos diretamente, mas impede o acesso de outras classes que não sejam subclasses ou do mesmo pacote.
    protected String identificador;

    // Métodos
    public Pessoa(String nome, String nacionalidade, String naturalidade) {
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.naturalidade = naturalidade;
    } // Construtor para inicializar os atributos da classe Pessoa

    protected void atualizarNome(String nome) {
        this.nome = nome;
    } //void indica que o metodo nao retorna nenhum valor, apenas executa uma acao.
    protected void atualizarID (String identificador) {
        if (this.identificador == null || this.identificador.isBlank()) {
            this.identificador = UUID.randomUUID().toString();
        }
    }

    protected String recuperarNome() {
        return this.nome;
    } // String indica que o metodo retorna um valor, sendo nesse caso STRING.
    protected String recuperarNacionalidade() {
        return this.nacionalidade;
    }
    protected String recuperarNaturalidade() {
        return this.naturalidade;
    }
    protected String recuperarID() {
        return this.identificador;
    }
    // Qualquer objeto instanciado a partir dessa classe Pessoa terá os atributos “nome”, “nacionalidade” e “naturalidade”, além de uma cópia dos métodos mostrados. 
}

// declaração de subclasse Aluno que herda de classe Pessoa
class Aluno extends Pessoa {

    public Aluno(String nome, String nascionalidade, String naturalidade) {
        super(nome, nascionalidade, naturalidade); // super é para chamar o construtor da classe base Pessoa
        this.identificador = UUID.randomUUID().toString(); // Gerando um ID usando UUID
        recuperarID(); //chamando o metodo atualizarID para atualizar o ID do aluno com o valor gerado.
    }
}

// mostrando em tela
public class _1HerancaEinstalacaoDeObjetos{
    public static void main(String[] args) {
        // static void main(Sring[] args) é o ponto de entrada do programa, onde a execução começa. Ele sempre é necessário para que o programa seja executado, e deve ser declarado como public para que possa ser acessado de fora da classe, static para ser chamado sem necessidade de criar uma instância da classe, e void para criar um metodo que não retorna nenhum value. O parâmetro String[] args é um array de string que pode ser usado para passar argumentos para o programa a partir da linha de comando, mas nesse caso não estamos utilizando ele.

        // Criando um objeto da classe Pessoa
        Pessoa pessoa1 = new Pessoa("Gabriel", "Brasileira", "Fortaleza");

        // Acessando os atributos e metrodos do objeto pessoa1
        System.out.println("Nome: " + pessoa1.recuperarNome());
        System.out.println("Nacionalidade: " + pessoa1.recuperarNacionalidade());
        System.out.println("Naturalidade: " + pessoa1.recuperarNaturalidade());

        pessoa1.atualizarNome("João Gabriel");
        System.out.println("Nome atualizado: " + pessoa1.recuperarNome());

        // criando um objeto da classe Aluno
        Aluno aluno1 = new Aluno("Maria", "Colombiana", "Bogotá");
        System.out.println("Nome: " + aluno1.recuperarNome());
        System.out.println("ID do aluno: " + aluno1.recuperarID());
    }
}