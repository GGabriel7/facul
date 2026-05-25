package _3classeObject_principaisMetodos._2equalsEhashcode;

public class Equals {
    private static int I1, I2, I3;
    private static String S1, S2, S3;
    private static Pessoa p1, p2, p3;

    public static void main(String args[]) {
        // atributos para serem comparados
        I1 = 1;
        I2 = 2;
        I3 = 1;

        S1 = "a";
        S2 = "b";
        S3 = "a";

        p1 = new Pessoa("João");
        p2 = new Pessoa("Gabriel");
        p3 = new Pessoa("João");

        //quando forem comparados, mesmo p1 e p3 terem o mesmo nome, eles são objetos diferentes, ou seja, estão em posições diferentes da memória, por isso o resultado é diferente.

        compareEquals(p1, p2, p3);
        compareEquals(S1, S2, S3);
        compareEquals(I1, I2, I3);
    }

    public static class Pessoa {
        // necessario colocar static para acessar a classe Pessoa dentro do main
        private String nome;

        public Pessoa (String nome) {
            this.nome = nome;
        }

        public String getNome() {
            return nome;
        }
    }

    public static void compareEquals(Object o1, Object o2, Object o3) {
        // void serve para dizer que o método não tem retorno.
        System.out.println("Uso de EQUALS para comparar " + o1.getClass().getName());

        if ( o1.equals( o2 ) )
            System.out.println("o1 == o2");
        // equals é um método da classe Object, e por isso pode ser usado para comparar qualquer tipo de objeto. 
        else
            System.out.println("o1 != o2");
        if ( o1.equals(o3) )
            System.out.println("o1 == o3");
        else
            System.out.println("o1 != o3");
    }
}