public class ClasseFilha extends MetodoAbstrato {
    public ClasseFilha(String nome, String id) {
        super(nome, id);
    }

    @Override
    // O metodo abstrato é implementado na classe filha, com a implementação do metodo ficando a cargo da classe filha, ou seja, a classe filha tem a liberdade de implementar o metodo abstrato da forma que ela achar melhor, desde que ela implemente o metodo abstrato obrigatoriamente.
    protected boolean atualizarID(String id) {
        if (id.length() == 4) {
            this.id = id;
            return true;
        } else {
            return false;
        }
    }
}