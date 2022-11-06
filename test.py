'''import urllib
import requests

air = urllib.request.urlopen("https://api.thingspeak.com/channels/977297/feeds.json?results=2")

x=air.read()

s=x.decode()

print(s)

y=list(s)
print(y)'''

'''mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "smart_irrigation")

mycursor = mydb.cursor()'''

#air = pd.read_sql("SELECT * FROM air",mydb)

#soil = pd.read_sql("SELECT * FROM soil",mydb)

#env_data['field1'] = env_data['field1'].astype(float)
#env_data['field2'] = env_data['field2'].astype(float)
#env_data['field3'] = env_data['field3'].astype(float)
#env_data['field4'] = env_data['field4'].astype(float)
#env_data = env_data.replace('NaN',0)


import csv
import requests
import urllib
import pandas as pd
from sklearn.cluster import KMeans

from forecast import *
from pred import *

'''forecast_new = pd.read_csv("https://api.thingspeak.com/channels/998677/feeds.csv")
field4_inp = forecast_new['field4']
field4_inp = field4_inp.values.reshape(-1,1)

km = KMeans(n_clusters=2)
clus = km.fit_predict(field4_inp)'''
#print(forecast_data)


#env_data = pd.read_csv("https://api.thingspeak.com/channels/977297/feeds.csv")
#print(env_data)
#print(len(env_data))
#print(env_data.at[10,'field4'])

def make_scalable(dataset):
    dataset_min = dataset.min()
    #print(dataset_min)
    dataset_max = dataset.max()
    dataset_range = dataset_max - dataset_min
    dataset_scaled = (dataset - dataset_min)/(dataset_range)
    #print(dataset_scaled)
    return dataset_scaled

forecast_inp = forecast_data.reshape(1,-1)
#forecast_inp = forecast.drop(columns=['created_at','entry_id','field4'], axis = 1)
forecast_inp1 = make_scalable(forecast_inp)
field4 = svc_model.predict(forecast_inp1)