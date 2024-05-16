import speech_recognition as sr

# Crear un objeto reconocedor
recognizer = sr.Recognizer()

# Función para realizar reconocimiento de voz continuo desde el micrófono
def recognize_continuous_speech():
    with sr.Microphone() as source:
        print("Di algo...")

        # Calibrar el ruido de fondo para mejorar la precisión
        recognizer.adjust_for_ambient_noise(source)

        # Bucle infinito para escuchar continuamente
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)  # Escuchar durante 5 segundos o hasta que se detecte silencio
                text = recognizer.recognize_google(audio, language="es-ES")
                
                # Imprimir el texto reconocido
                print("Texto reconocido:", text)

            except sr.UnknownValueError:
                print("No se pudo entender el audio")

            except sr.RequestError as e:
                print(f"Error en la solicitud: {e}")

# Llamar a la función para reconocimiento de voz continuo
recognize_continuous_speech()