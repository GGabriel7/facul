from PIL import Image # Biblioteca para manipulação de imagens
import numpy as np  # Biblioteca para manipulação de arrays

def main():
    # Carregar a imagem original
    img = Image.open('imagem.png')
    
    # Converter a imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()
    
    print("\nFormato da Imagem:", img_data.shape, "\n")  # Exibir a forma da imagem (altura, largura, canais)
    
    # Salvar os dados binários em um arquivo
    with open('imagem.bin', 'wb') as bin_file:
        bin_file.write(binary_data)
        
    # Copiar o arquivo binário para um novo arquivo
    with open('imagemCopia.bin', 'wb') as copy_file:
        copy_file.write(binary_data)
        
    # Manipilação dos dados do arquivo binário cópia
    # Exemplo: Inverter os bytes
    with open('imagemCopia.bin', 'rb') as copy_file:
        data = bytearray(copy_file.read())
        
    # inverter na horizontal
    data = data[::-1]
        
    with open('imagemCopia.bin', 'wb') as copy_file:
        copy_file.write(data)  # Inverter os bytes e salvar novamente
        
    # Carregar e mostrar a imagem manipulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    
    # Inverter todos os bytes
    modified_data = np.fliplr(modified_data)
    
    modifild_img = Image.fromarray(modified_data)
    modifild_img.show()
    
if __name__ == "__main__":
    main()