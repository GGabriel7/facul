import java.util.Scanner;

public class _1comandosRelativos {
    public static void main (String args[]) throws InterruptedException {
        // throws serve para indicar que o método pode lançar uma exceção, e que a responsabilidade de tratar essa exceção é do chamador do método. No caso do método main, isso significa que se ocorrer uma InterruptedException (que é uma exceção de interrupção, como digitar Ctrl+C) dentro do método, ela não será tratada dentro do próprio método, mas sim propagada para o ambiente de execução, que pode lidar com ela de acordo com suas próprias regras.

        int divisor, dividendo, quociente = 0;
        String controle = "s";

        Scanner s = new Scanner(System.in); // Scanner é uma classe do Java que permite ler a entrada do usuário a partir do console. Ele é usado para capturar dados digitados pelo usuário, como números ou texto, e armazená-los em variáveis para uso posterior no programa.
        do {
            System.out.println ( "Entre com o dividendo." );
            dividendo = s.nextInt(); // nextInt() é um método da classe Scanner que lê o próximo token da entrada como um inteiro. Ele é usado para capturar um número inteiro digitado pelo usuário e armazená-lo em uma variável do tipo int. Se o usuário digitar algo que não seja um número inteiro, o método lançará uma InputMismatchException.
            System.out.println ( "Entre com o divisor." );
            divisor = s.nextInt();

            try {
                if (divisor == 0) {
                    throw new ArithmeticException ( "Divisão por zero não é permitida." ); // throw é usado para lançar uma exceção específica em um ponto específico do código. Ele é seguido por uma instância de uma classe de exceção, que pode ser personalizada com uma mensagem de erro. No exemplo, se o divisor for zero, o código lança uma ArithmeticException com a mensagem "Divisão por zero não é permitida."
                }
                quociente = dividendo / divisor;
            } catch (Exception e) {
                System.out.println ( "Ocorreu um erro: " + e.getMessage() ); // getMessage() é um método da classe Exception que retorna a mensagem de erro associada à exceção. Ele é usado para obter uma descrição mais detalhada do erro que ocorreu, permitindo que o programa informe ao usuário o motivo específico do problema.
            } finally {
                System.out.println ( "Bloco finally."); // finally é um bloco de código que é executado após o bloco try e catch, independentemente de uma exceção ter sido lançada ou não. Ele é usado para garantir que certas ações sejam realizadas, como liberar recursos ou fechar conexões, mesmo que ocorra um erro durante a execução do código dentro do bloco try.
            }
            System.out.println ( "O quociente é: " + quociente );
            System.out.println ( "Deseja continuar? (s/n)" );
            controle = s.next();
        } while (controle.equals("s"));
        s.close(); // O método close() é usado para fechar o recurso Scanner, liberando os recursos associados a ele. É uma boa prática fechar os recursos quando eles não são mais necessários para evitar vazamentos de memória e outros problemas relacionados a recursos não liberados.
    }
}
