def buscar_frases(archivo, frases):
    with open(archivo, 'r') as archivo_txt:
        texto = archivo_txt.read()
        for frase in frases:
            indice = -1
            while True:
                indice = texto.find(frase, indice + 1)
                if indice == -1:
                    break
                print(f'Frase encontrada: "{frase}"')
                print('Contexto: ')
                inicio = max(0, indice - 30)
                fin = min(len(texto), indice + len(frase) + 30)
                contexto = texto[inicio:fin]
                contexto = contexto.replace(frase, f'\033[1m{frase}\033[0m')
                print(contexto)
                print('-' * 50)

# Ejemplo de uso
archivo = ("file location")
frases_buscar = ['phrase 1', 'phrase 2','phrase 3','phrase etc']
buscar_frases(archivo, frases_buscar)
