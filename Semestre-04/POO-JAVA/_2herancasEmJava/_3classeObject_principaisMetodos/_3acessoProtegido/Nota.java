package _3classeObject_principaisMetodos._3acessoProtegido;

public class Nota {
    public float calcularMedia(float nota1, float nota2){
        return (nota1 + nota2) / 2;
    }

    protected float calcularCoeficienteRendimento(float media, float frequencia){
        return media * frequencia;
    }
}