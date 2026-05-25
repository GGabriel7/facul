public class Principal {
    private static MetodoAbstrato ref[];// vetor de referencia do tipo da classe abstrata, ou seja, ele pode receber objetos de qualquer classe filha da classe abstrata.

    public static void main(String args[]) {
        ref = new MetodoAbstrato[2];

        ref[0] = new ClasseFilha("Gabriel", "123");
        ref[1] = new ClasseFilha("Maria", "456");
        for (int i=0; i<ref.length; i++) {
            System.out.println("Nome: " + ref[i].recuperarNome());
            System.out.println("ID: " + ref[i].recuperarID());
        }

        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=");

        ref[0].atualizarID("A001");
        ref[1].atualizarID("A002");
        for (int i=0; i<ref.length; i++) {
            System.out.println("Nome: " + ref[i].recuperarNome());
            System.out.println("ID: " + ref[i].recuperarID());
        }
    }
}