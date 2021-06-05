from random import randint



def acertar():
    # Se agregan los operadores lógicos de igualdad o equivalencia, para evitar errores en los cuales la diferencia fuese 5, 10 ó 20
    nombre = input('Ingrese su nombre')
    contador = 0
    numero_azar = randint(1,100)
    while True:
        numero = input('Ingresa el número que crees qué es, entre 1 y 100 (0 para parar)')
        try:
            numero = int(numero)
            diferencia = abs(numero - numero_azar)
            if diferencia == 0:
                contador = contador + 1
                print(f'Felicitaciones {nombre}, lo lograste en {contador} intentos')
                break
            elif numero == 0:
                print(f'Sorry {nombre}, No lo lograste a pesar de tratar {contador} veces. Más suerte para otra vez')
                break
            elif numero > 100:
                contador = contador + 1
                print("La entrada es incorrecta: escribe un número entero, entre 1 y 100")
            elif diferencia <= 5:
                contador = contador + 1
                print(f'Sorry {nombre}, ese no es pero estás a una distancia menor o igual a 5')
            elif diferencia <= 10:
                contador = contador + 1
                print(f'Sorry {nombre}, ese no es pero estás a una distancia mayor que 5 y menor o igual que 10')
            elif diferencia <= 20:
                contador = contador + 1
                print(f'Sorry {nombre}, ese no es pero estás a una distancia mayor que 10 y menor o igual que 20')
            elif diferencia > 20:
                contador = contador + 1
                print(f'Sorry {nombre}, ese no es pero estás a una distancia mayor que 20')
        except ValueError:
            contador = contador + 1
            print ("La entrada es incorrecta: escribe un número entero, entre 1 y 100")

if __name__ == '__main__':
    acertar()
