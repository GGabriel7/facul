public class Referencia {
    private Nome a1, a2;
    public Referencia() {
        a1 = new Nome("Gabriel", "Ramos");
        a2 = new Nome("Adrielly", "Gomes");
        System.out.println("O nome do a1 é: " + a1.recuperarNome());
        System.out.println("O nome do a2 é: " + a2.recuperarNome());
        a2 = a1; // a2 passa a referenciar o mesmo objeto que a1
        System.out.println("O nome do a1 é: " + a1.recuperarNome());
        System.out.println("O nome do a2 é: " + a2.recuperarNome());
        a2.definirNome("Maria", "Silva"); // altera o nome do objeto referenciado por a2 (que é o mesmo que a1)
        System.out.println("O nome do a1 é: " + a1.recuperarNome());
        System.out.println("O nome do a2 é: " + a2.recuperarNome());
        manipularNome(a1); // passa a referência de a1 para o método manipular
        System.out.println("O nome do a1 é: " + a1.recuperarNome());
        System.out.println("O nome do a2 é: " + a2.recuperarNome());
    }
    
    public void manipularNome(Nome nome) {
        nome.definirNome("João", "Pereira"); // altera o nome do objeto referenciado por nome (que é o mesmo que a1 e a2)
    }

    public static void main(String[] args) {
        new Referencia();
    }
}

class Nome {
    private String nome;
    private String sobrenome;

    public Nome(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    public String recuperarNome() {
        return nome + " " + sobrenome;
    }

    public void definirNome(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }
}