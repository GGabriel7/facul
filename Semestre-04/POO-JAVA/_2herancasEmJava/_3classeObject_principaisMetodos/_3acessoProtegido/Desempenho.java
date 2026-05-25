package _3classeObject_principaisMetodos._3acessoProtegido;

import _3classeObject_principaisMetodos._3acessoProtegido.Nota;

public class Desempenho extends Nota{
    private float media, CR;
    private Nota nota;

    // A classe Desempenho é filha da classe Nota. Por isso, ela tem acesso aos métodos “calcularMedia” (público) e “calcularCoeficienteRendimento” (protegido) de Nota, mesmo estando em outro pacote.

    public Desempenho() {
        nota = new Nota();
        media = calcularMedia(6, 8);
        CR = calcularCoeficienteRendimento(media, 0.75f);
        // usar media = calcularMedia() ou media = nota.calcularMedia() tem o mesmo resultado, pois o metodo calcularMedia é publico e pode ser acessado por qualquer classe. 
        // No caso de calcularCoeficienteRendimento, mesmo ele sendo protegido, a classe Desempenho ainda pode acessar por Desempenho ser filho de Nota. Usar nota.calcularCoeficienteRendimento() não dará certo pois nota.calcularCoeficienteRendimento() entende-se que está puxando de importação. 
        // public - livre para filhas e importação / protected - livre para filhas, mas não para importação / private - não é livre para filhas e nem para importação
    }
}
