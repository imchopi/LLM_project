import requests
import json

# URL del servidor Generation Text WebUI
url = "http://127.0.0.1:5000/v1/completions"
headers = {"Content-Type": "application/json"}

print("¡CrEaDoR dE hIsToRiAs!")

# Solicitar información al usuario
nombre_principal = input("Nombre del personaje principal: ")
nombre_secundario = input("Nombre del personaje secundario: ")
lugar = input("Lugar donde transcurre la historia: ")
accion = input("Describe una acción importante que debe suceder en la historia: ")

# Crear el prompt con la información obtenida de manera fluida
prompt = (f"Escribe una historia sobre los siguientes personajes:\n"
          f"- El personaje principal se llama {nombre_principal}, un joven curioso.\n"
          f"- El personaje secundario es {nombre_secundario}, un amigo leal que siempre le acompaña.\n"
          f"- La historia se desarrolla en {lugar}, un lugar lleno de misterios y belleza.\n"
          f"- La acción importante en esta historia es que {nombre_principal} y {nombre_secundario} están buscando un piso de alquiler en este lugar.\n"
          f"\nUsa esta información para crear una narrativa intrigante y atractiva que explore su aventura en la búsqueda de un nuevo hogar.\n"
          f"Desarrollo de la historia:")

# Preparar el cuerpo de la solicitud
body = {
    "prompt": prompt,
    "max_tokens": 500,  # Controla la longitud máxima de la historia
    "temperature": 0.7  # Ajusta la creatividad del modelo
}

# Hacer la solicitud al servidor
response = requests.post(url, headers=headers, json=body, verify=False)
message_response = json.loads(response.content.decode("utf-8"))
assistant_message = message_response["choices"][0]["text"]

# Imprimir la respuesta generada
print("\n" + assistant_message)
