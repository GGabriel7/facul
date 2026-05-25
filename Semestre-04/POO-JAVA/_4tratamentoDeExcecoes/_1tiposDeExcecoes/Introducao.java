// Exceções são eventos que ocorrem durante a execução de um programa que interrompem o fluxo normal do programa. Elas podem ser causadas por erros de programação, condições inesperadas ou situações que o programa não pode lidar. Em Java, as exceções são representadas por objetos, chamado de exception objects, que contêm informações sobre o erro ocorrido.

// Exemplo

public class Introducao {
    public static void main(String[] args) {
        int num1, num2, resultado;
        
        System.out.println("Digite o primeiro número: ");
        num1 = Integer.parseInt(System.console().readLine()); //lendo o numero do usuario
        System.out.println("Digite o segundo número: ");
        num2 = Integer.parseInt(System.console().readLine()); //lendo o numero do usuario

        try {
            resultado = num1 / num2;
            System.out.printf("O resultado da divisão é: %.2f", resultado);
            // println e printf se diferenciam porque o printf permite formatar a saída, como no exemplo acima onde limitamos o resultado a 2 casas decimais.

        } 
        catch (NumberFormatException e) { //tratando a exceção de formato de número. Não aceitará outros caracteres
            System.out.println("Erro: Você deve digitar um número válido.");

        } 
        catch (ArithmeticException e) { //tratando a exceção de divisão por zero
            System.out.println("Erro: Não é possível dividir por zero.");      

        } 
        finally {
            System.out.println("Programa finalizado."); //bloco finally é executado independentemente de ocorrer ou não uma exceção

        }
    }
}