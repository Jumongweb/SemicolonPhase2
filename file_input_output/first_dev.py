import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

r = requests.get(url)
data = r.json()
# print(data)
# print(data['current_units'])
# print(data['current_units']['time'])
# print(r.text)

url2 = "https://media.licdn.com/dms/image/D4D03AQGwp_T_hsCEYg/profile-displayphoto-shrink_400_400/0/1707170200187?e=1715212800&v=beta&t=qDyUyQaoVsWnUDsFYUe-5CT9Fw3Bn9lzo209Gw4asu0"
r2 = requests.get(url2)
print(r2.text)
#data2 = r.json()
s
with open("femi.png", mode='wb') as mf:
    mf.write(r2.content)