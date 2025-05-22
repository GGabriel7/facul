1. Arvore Binária de Busca:
    - Estrutura de dados que armazena elementos de forma ordenada. Cada nó é rotulado com uma chave, e os nós à esquerda têm chaves menores que o nó pai, enquanto os nós à direita têm chaves maiores.

    - Árvores baleceadas são importantes para garantir eficiência nas operações de busca, inserção e remoção. Elas mantêm a altura da árvore o mais baixa possível, o que resulta em operações de tempo O(log n) em média.
    - Tipos de árvores balanceadas:
        - Red-Black Tree: Uma árvore binária de busca balanceada onde cada nó tem uma cor (vermelho ou preto) e segue regras específicas para garantir que a árvore permaneça balanceada após inserções e remoções.
        - AVL Tree: Uma árvore binária de busca balanceada onde a diferença de altura entre as subárvores esquerda e direita de qualquer nó é no máximo 1. Isso garante operações de busca, inserção e remoção em tempo O(log n).