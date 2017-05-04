teclas = (
    ' _',    # 1
    ' ABC',  # 2
    ' DEF',  # 3
    ' GHI',  # 4
    ' JKL',  # 5
    ' MNO',  # 6
    ' PQRS', # 7
    ' TUV',  # 8
    ' WXYZ', # 9
)

def teclado(frase):
    frase_em_numeros = ''

    for letra in frase:
        for tecla, letras in enumerate(teclas, 1):
            if letra in letras:
                frase_em_numeros += str(tecla) * letras.index(letra)

    return frase_em_numeros.replace('1', '_')