public abstract class MetodoAbstrato {
    // abstract servirá para criar um modelo para as classes filhas, ou seja, as classes filhas terão que implementar obrigatoriamente os metodos abstratos. Ela não pode ser instaciada, não podendo criar objetos a partir dela. O intuito é forças as classes filhas a implementar os metodos abstratos.

    protected String nome;
    protected String id;

    public MetodoAbstrato(String nome, String id) {
        this.nome = nome;
        this.id = id;
    }

    protected void atualizarNome ( String nome ) {
        this.nome = nome;
    }
    protected String recuperarNome ( ) {
        return this.nome;
    }

    protected abstract boolean atualizarID(String id);
    // O metodo abstrato não tem corpo, não tendo implementação. Ele é apenas uma assinatura, definindo o que o metodo deve fazer, mas não como ele deve fazer. A implementação do metodo abstrato fica a cargo das classes filhas, com elas devendo implementar o metodo abstrato obrigatoriamente.

    protected String recuperarID(){
        return this.id;
    }
}