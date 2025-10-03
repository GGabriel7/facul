# Zenit Polar uma técnica de codificação simples onde cada letra do alfabeto é substituída pela letra que está três posições à frente. 
# Por exemplo, 'A' se torna 'D', 'B' se torna 'E', e assim por diante.
# As letras no final do alfabeto "dão a volta" para o início, então 'X' se torna 'A', 'Y' se torna 'B', e 'Z' se torna 'C'.

def zenitPolarReplace(text):
    # Aplicar a codificação Zenit Polar com metodo replace()
    
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),  # Minúsculas
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R'),] # Maiúsculas
    
    for old, new in replacements:
        text = text.replace(old, new) # Substitui todas as ocorrências de old por new
        
    return text

def main():
    #Entrada da frase e aplicação da codificação
    phrase = "O Zenit Polar é uma técnica de codificação simples."
    phraseTitle = phrase.title() # Primeira letra de cada palavra em maiúscula
    
    # Dividir a frase em palavras
    words = phraseTitle.split()
    
    # Processar cada palavra individualmente usando a função zenitPolarReplace
    codedWords = [zenitPolarReplace(word) for word in words]
    
    # Juntar as palavras codificadas de volta em uma frase
    codedPhrase = ' '.join(codedWords)
    print("Frase original:", phrase)
    print("Frase original:", phraseTitle)
    print("Frase codificada:", codedPhrase)
    
    
if __name__ == "__main__":
    main()
    
    