import requests

def dolar():
    
    url = "https://api.sbif.cl/api-sbifv3/recursos_api/dolar?apikey=fb4091553e316d47f4604cdd7f8b3f89851dd2da&formato=json"
    data = requests.get(url).json()
    dolar_value = data["Dolares"][0]["Valor"]
    print("calor dolar: "+ str(dolar_value))
    return dolar_value




