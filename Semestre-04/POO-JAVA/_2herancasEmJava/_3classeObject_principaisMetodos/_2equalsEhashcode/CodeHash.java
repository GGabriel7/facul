package _3classeObject_principaisMetodos._2equalsEhashcode;

public class CodeHash {

    public static void main(String args[]) {
        Pessoa p1 = new Pessoa("João");
        Pessoa p2 = new Pessoa("Gabriel");
        Pessoa p3 = new Pessoa("Favio");

        System.out.println("HashCode de p1: " + p1.hashCode());
        System.out.println("HashCode de p2: " + p2.hashCode());
        System.out.println("HashCode de p3: " + p3.hashCode());
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

    public int hashCode() {
        // o hashcode é um número inteiro que representa o objeto, e é usado para comparar objetos. 
        // o hashcode é gerado a partir dos atributos do objeto, e por isso, se dois objetos tiverem os mesmos atributos, eles terão o mesmo hashcode.
        //return nome.hashCode();

        if (this instanceof Pessoa) {
            // instanceof é um operador que verifica se um objeto é uma instância de uma classe.
            Pessoa other = (Pessoa) this;
            return other.nome.hashCode();
        } else {
            return super.hashCode();
        }
    }
    }
}