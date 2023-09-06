import requests

# URL base
base_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/"

# Itera a través de los números del 1 al 999
for i in range(1, 1000):
    # Formatea el número con ceros a la izquierda para que tenga tres dígitos (por ejemplo, 001, 002, ..., 999)
    pokemon_number = str(i).zfill(3)
    
    # Crea la URL completa para descargar
    url = f"{base_url}{pokemon_number}.png"
    
    # Realiza la solicitud para descargar la imagen
    response = requests.get(url)
    
    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Escribe la imagen en un archivo
        with open(f"{pokemon_number}.png", "wb") as file:
            file.write(response.content)
        print(f"Descargado: {pokemon_number}.png")
    else:
        print(f"Error al descargar: {url}")
