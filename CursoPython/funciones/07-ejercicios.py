def eliminar_espacios(textousuario):
    texto_sin_espacio = ""
    for _ in textousuario:
        if _ != " ":
            texto_sin_espacio += _
    return texto_sin_espacio


def reversa(textosinespacio):
    textoalreves = ""
    for char in textosinespacio:
        textoalreves = char + textoalreves
    return textoalreves


def es_palindromo(texto):
    texto_sin_espacio = eliminar_espacios(texto)
    texto_invertido = reversa(texto_sin_espacio)
    if texto_invertido == texto_sin_espacio:
        print(f"El texto {texto} es palindromo")
    else:
        print(f"El texto {texto} NO es palindromo")


es_palindromo("Hola mundo")
es_palindromo("amo la paloma")
