// Tipagem estática: quando o tipo de uma variável é definido em tempo de compilação, como colocar tipo especifico na variavel, int, string...
// Tipagem dinamica: quando o tipo é determinado em tempo de execução, como usar 'var' em JavaScript, onde o tipo é inferido pelo compilador com base no valor atribuido.

// exemplo de tipagem dinamica
var a;
console.log("Tipo: " + typeof a);
a = 10;
console.log("Tipo: " + typeof a);
a = "Olá, mundo!";
console.log("Tipo: " + typeof a);
a = false;
console.log("Tipo: " + typeof a);
a = []
console.log("Tipo: " + typeof a);
a = function() {

}
console.log("Tipo: " + typeof a);

// em java, o tipo é definido em tempo de compilação, já sendo necessário declarar o tipo da variavel na hora de declarar ela. No entanto, a partir da versão 10 do java, foi introduzida a palavra-chave 'var', que permite a declarar a variavel sem especificar o tipo, deixando que o compilador infira com base no valor, mas ainda assim o tipo é definido em tempo de compilação, sendo uma vez declarada o tipo não pode ser alterado.