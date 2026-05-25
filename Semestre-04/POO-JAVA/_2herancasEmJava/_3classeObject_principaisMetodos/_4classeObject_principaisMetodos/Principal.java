package _3classeObject_principaisMetodos._4classeObject_principaisMetodos;

public class Principal {
    public static void main(String args[]) {
        PessoaFisica PF1 = new PessoaFisica("Ricardo", "12345678900");
        PessoaFisica PF2 = new PessoaFisica("Ricardo", "00987654321");
        PessoaFisica PF3 = new PessoaFisica("Carlos", "12345678900");
        Aluno A1 = new Aluno("Lucas", "12345678900", "AL001");
        Aluno A2 = new Aluno("Pedro", "12345678900", "AL002");
        Aluno A3 = new Aluno("Mateus", "12345678900", "AL003");

        System.out.println("Comparando PF1 e PF2");
        System.out.println("  PF1.equals(PF2) -> " + PF1.equals(PF2));
        System.out.println("Comparando PF1 e PF3");
        System.out.println("  PF1.equals(PF3) -> " + PF1.equals(PF3));
        System.out.println("Comparando PF2 e PF3" );
        System.out.println("  PF2.equals ( PF3 ) -> " + PF2.equals(PF3));


        System.out.println("\nComparando A1 e A2" );
        System.out.println("  A1.equals ( A2 ) -> " + A1.equals(A2));
        System.out.println("Comparando A1 e A3" );
        System.out.println("  A1.equals ( A3 ) -> " + A1.equals(A3));
        System.out.println("Comparando A2 e A3" );
        System.out.println("  A2.equals ( A3 ) -> " + A2.equals(A3));

        System.out.println("\nComparando PF1 e A1" );
        System.out.println("  PF1.equals ( A1 ) -> " + PF1.equals(A1));
        System.out.println("Comparando PF2 e A2" );
        System.out.println("    PF2.equals ( A2 ) -> " + PF2.equals(A2));

        //Imprime o identificador do objeto
        System.out.println("[PF1]: "+PF1 + " [PF2]: " + PF2 + " [PF3]: " + PF3);
        System.out.println("[A1]: " + A1 + " [A2]: " + A2 + " [A3]: " + A3);
    }
}