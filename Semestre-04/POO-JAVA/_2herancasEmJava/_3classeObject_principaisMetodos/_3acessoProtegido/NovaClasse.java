package _3classeObject_principaisMetodos._3acessoProtegido;

public class NovaClasse {
    private static Desempenho desempenho;

    public static void main(String args[]) {
        desempenho = new Desempenho();
        float media = desempenho.calcularMedia(6, 8);
        System.out.println("Média: " + media);

        float CR = desempenho.calcularCoeficienteRendimento(media, 0.75f);
        System.out.println("CR: " + CR);
    }
}
