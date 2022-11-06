import requests
import urllib
import pandas as pd
import time

air = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Mumbai,in&units=metric&APPID=7d4941cfeaaaff5aa938459474567a57')
#uv = requests.get('http://api.openweathermap.org/data/2.5/uvi?appid=7d4941cfeaaaff5aa938459474567a57&lat=19.01&lon=72.85')

data1 = air.json()
#data2 = uv.json()
#print(data1)
#print(data2)

env_data = pd.read_csv("https://api.thingspeak.com/channels/977297/feeds.csv")
n = len(env_data)
for i in range(n-2,0,-1):
	air_temp = data1['main']['temp']
	air_humidity = data1['main']['humidity']
	#uv = data2['value']
	soil = env_data.at[i,'field4']

	data_upload=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=AKCUXJOUI50703HV&field1="+str(air_temp)+"&field2="+str(air_humidity)+"&field3="+str(soil))
	time.sleep(1)


#print(air_humidity)

#data_upload=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=T9DXE8ELNVGKU63Y&field1="+str(air_temp)+"&field2="+str(air_humidity)+"&field3="+str(uv)+"&field4="+str(20))

#data_upload=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=T9DXE8ELNVGKU63Y&field4="+str(14))
#air_humidity1=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=T9DXE8ELNVGKU63Y&field2="+str(air_humidity))
#uv1=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=T9DXE8ELNVGKU63Y&field3="+str(uv))

#print(air_humidity1)
#print(data1['weather'][0]['main'])

'''mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "smart_irrigation")

mycursor = mydb.cursor()

sql = "INSERT INTO air (air_temp, air_humidity, uv) VALUES (%s, %s, %s)"
val = (data1['main']['temp'], data1['main']['humidity'], data2['value'])

mycursor.execute(sql, val)

mydb.commit()'''