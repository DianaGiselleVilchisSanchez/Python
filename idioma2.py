from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Para resultados más consistentes
DetectorFactory.seed = 0  

def detectar_idioma(texto):
    try:
        idioma = detect(texto)
        return f"El idioma detectado es: {idioma}"
    except LangDetectException:
        return "No se pudo determinar el idioma."

# Pedir al usuario un texto
texto = input("Ingrese una palabra o frase: ")
resultado = detectar_idioma(texto)
print(resultado)
