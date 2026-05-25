package criandoExcecao;

public class Principal {
    public static void main(String[] args) {
        String CPF;
        
        System.out.println("Digite seu CPF");
        CPF = System.console().readLine();

        try {
            Pessoa pessoa1 = new Pessoa("Gabriel", CPF);

            pessoa1.atualizarCPF(CPF);
            System.out.println("CPF atualizado com sucesso!");
            
            System.out.println("\nDados do usuário:");
            System.out.println("Nome: " + pessoa1.retornarNome());
            System.out.println("CPF: " + pessoa1.retornarCPF());
        } catch (ErroValidacaoCPF e) {
            System.out.println(e);
        }

    }
}