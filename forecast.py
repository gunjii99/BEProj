import requests
#import mysql.connector
#import urllib
import numpy as np

air = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=1275339&units=metric&APPID=7d4941cfeaaaff5aa938459474567a57&cnt=1')
#uv = requests.get('http://api.openweathermap.org/data/2.5/uvi/forecast?appid=7d4941cfeaaaff5aa938459474567a57&lat=19.01&lon=72.85&cnt=1')

data1 = air.json()
#data2 = uv.json()
#print(data1)
#print(data2)

temp=data1['list'][0]['main']['temp']
humidity=data1['list'][0]['main']['humidity']
#uv=data2[0]['value']

#print(humidity)

#print(str(temp))

forecast_data = np.array([temp, humidity])
#print(forecast_data)

#upload_data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=H6XCST902X08B6V8&field1="+str(temp)+"&field2="+str(humidity)+"&field3="+str(uv))


'''mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "smart_irrigation")

mycursor = mydb.cursor()

sql = "INSERT INTO air_forecast (temp, humidity, uv) VALUES (%s, %s, %s)"
val = (data1['list'][0]['main']['temp'], data1['list'][0]['main']['humidity'], data2[0]['value'])

mycursor.execute(sql, val)

mydb.commit()'''