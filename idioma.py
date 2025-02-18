from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # Para resultados más consistentes

def detectar_idioma(palabra):
    try:
        idioma = detect(palabra)
        if idioma == "es":
            return "La palabra está en español."
        elif idioma == "en":
            return "La palabra está en inglés."
        else:
            return "No se pudo determinar el idioma con certeza."
    except:
        return "No se pudo analizar la palabra."

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")
resultado = detectar_idioma(palabra)
print(resultado)
