package criandoExcecao;

import java.util.InputMismatchException;

public class Pessoa {
    String nome, CPF;

    public Pessoa(String nome, String CPF) {
        this.nome = nome;
        this.CPF = CPF;
    }

    // atualizando e puxando nome
    void atualizarNome(String nome) {
        this.nome = nome;
    }
    String retornarNome() {
        return this.nome;
    }
    
    public boolean atualizarCPF(String CPF) throws ErroValidacaoCPF {
        if (validarCPF(CPF)) {
            this.CPF = CPF;
            return true;
        } else {
            System.out.println("Erro: CPF invalido!");
            return false;
        }
    }

    private boolean validarCPF(String CPF) throws ErroValidacaoCPF {
        char DV10, DV11;
        int soma, num, peso, i, resto;

        // Remove pontos e traços
        CPF = CPF.replace(".", "").replace("-", "");

        // Verifica sequência de dígitos iguais e tamanho (11 dígitos)
        if (CPF.equals("00000000000") || CPF.equals("11111111111") ||
            CPF.equals("22222222222") || CPF.equals("33333333333") ||
            CPF.equals("44444444444") || CPF.equals("55555555555") ||
            CPF.equals("66666666666") || CPF.equals("77777777777") ||
            CPF.equals("88888888888") || CPF.equals("99999999999") ||
            (CPF.length() != 11)) {

            throw new ErroValidacaoCPF("Entrada inválida!");
        }

        try {

            // 1º Dígito Verificador
            soma = 0;
            peso = 10;

            for (i = 0; i < 9; i++) {
                num = (int) (CPF.charAt(i) - 48);
                soma += (num * peso);
                peso--;
            }

            resto = 11 - (soma % 11);

            if ((resto == 10) || (resto == 11))
                DV10 = '0';
            else
                DV10 = (char) (resto + 48);

            // 2º Dígito Verificador
            soma = 0;
            peso = 11;

            for (i = 0; i < 10; i++) {
                num = (int) (CPF.charAt(i) - 48);
                soma += (num * peso);
                peso--;
            }

            resto = 11 - (soma % 11);

            if ((resto == 10) || (resto == 11))
                DV11 = '0';
            else
                DV11 = (char) (resto + 48);

            // Verifica os dígitos verificadores
            if ((DV10 == CPF.charAt(9)) && (DV11 == CPF.charAt(10))) {
                return true;
            } else {
                throw new ErroValidacaoCPF("DV inválido.");
            }

        } catch (InputMismatchException erro) {
            return false;
        }
    }

    String retornarCPF() {
        return this.CPF;
    }
}