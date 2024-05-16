import random
from Lista import palavras
import string


def get_valid_word():
    palavra = random.choice(palavras)  #seleciona aleatoriamente uma palavra na lista
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
        
    return palavra

def jogo_da_forca():
    palavra = get_valid_word()
    palavras_letras = set(palavra) #letras da palavra
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set() #usuario responde
    
    Vidas = 6
    
    #obtendo entrada do usuario
    while len(palavras_letras) > 0 and Vidas > 0:
        #letras usadas
        # ' '.jogar(['a', 'b', 'cd']) --> 'a b cd'
        print('Voce tem',Vidas,'vidas,você usou essas letras: ',''.join(letras_usadas))
        
        # qual é a palavra atual (ie W - R D)
        lista_palavras = (letter if letter in letras_usadas else '-' for letter in palavras)
        print('Proxima letra ',''.join(lista_palavras))
        
        letras_usuario = input('Adivinhe uma letra ').upper()
        if letras_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letras_usuario)
            if letras_usuario in palavras_letras:
                palavras_letras.remove(letras_usuario)
            
            else:
                Vidas = Vidas - 1
                print('Errado.')
                
        elif letras_usuario in letras_usadas:
            print('Você já usou essa letra. Adivinhe outra. ')
        
        else:
            print('Letra errada.Tente novamente.')
    
    #chega aqui quando len(letras_palavras) == 0 OR quando vidas == 0
    if Vidas == 0:
        print('Voce morreu! A palavra é',palavra)
    else:
        print('Parabens! Voce adivinhou a palavra', palavra, '!!')
    
    
    
jogo_da_forca()