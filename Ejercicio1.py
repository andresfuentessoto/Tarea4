
def contar_digitos_letras_caract(cadena):
    digitos = 0
    letras = 0
    

    for i in cadena:
     if i.isdigit():
            digitos+= 1
     elif i.isalpha():
            letras+= 1
     else:
            pass       
    return digitos, letras
Texto = input("Ingrese el texto: ")
resultado = contar_digitos_letras_caract(Texto)

Caracteres_Especiales= len(Texto)-resultado[0]-resultado[1]

print('Cantidad de dígitos: %i' % resultado[0])
print('Cantidad de letras: %i' % resultado[1])
print('Cantidad de caracteres especiales: %i' % Caracteres_Especiales)
