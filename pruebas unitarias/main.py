#Docstring

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string, es o no, un palindromo

    Args:
        sentence (str): string a evaluar 

    Returns:
        bool: true o false 

    
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence [::-1]

