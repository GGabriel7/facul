package _1polimorfismoEmJava._2metodosEclassesFinal;

public abstract class classeFinal {
    //Atributos
    private float freq;
    private final int dias_letivos;
    private int presenca;

    //Métodos
    public classeFinal ( int dias_letivos ) {
        this.dias_letivos = dias_letivos;
    }

    // classe for declarada "final", todos os seus métodos são implicitamente "final" (isso não se aplica aos seus atributos). Métodos "final" não podem ser redefinidos nas subclasses. Com isso, ela não pode ser mais modifidificada, apenas inicializada.
    protected final void calcularFrequencia ( ) {
        freq = 100 * ( presenca / dias_letivos );
    }
    protected float recuperarFrequencia ( ) {
        return freq;
    }
    protected abstract float calcularMedia ( );
}