import requests

respuesta = requests.get("http://api.open-notify.org/astros.json")
data = respuesta.json()
print(data)

cantidad_astronautas = data["number"]
if cantidad_astronautas > 4:
    print("Party en el espacio")
else:
    print("Invita a la gente")

cant_astro_iss = 0
for person in data['people']:
    if person['craft'] == 'ISS':
        cant_astro_iss += 1

if cant_astro_iss == cantidad_astronautas:
    print("El party es en el ISS")




#parametros = {"lat": 9.0, "lon": 75.25}

#respuesta = requests.get("http://api.open-notify.org/iss-pass.json", params=parametros)
#print(respuesta.content)

#data = respuesta.json()
#print(data)

#respuesta = requests.get("http://api.open-notify.org/iss-pass.json?lat=9.0&lon=79.25")
#print(respuesta.content)