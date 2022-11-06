########        import statements        #######

import pandas as pd
import urllib

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
from forecast import *

import blynklib
import random
import time


########        normalization function         ########

def make_scalable(dataset):
    dataset_min = dataset.min()
    #print(dataset_min)
    dataset_max = dataset.max()
    dataset_range = dataset_max - dataset_min
    dataset_scaled = (dataset - dataset_min)/(dataset_range)
    #print(dataset_scaled)
    return dataset_scaled


########				SVM code			########https://api.thingspeak.com/channels/496094/feeds.csv?results=1000

env_data = pd.read_csv("https://api.thingspeak.com/channels/1041025/feeds.csv")
env_data = env_data[env_data['field3'].notna()]
#print(env_data)
X = env_data.drop(columns=['created_at','entry_id','field3'], axis = 1) # We drop our extra features and use all the remaining features in our dataframe to train the model.
y = env_data['field3']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.23, random_state = 0)
#svc_model = SVR(kernel='rbf', gamma='auto', C=1.0, epsilon=0.2)
#svc_model=LinearRegression()
svc_model=SVC()

#X_train_scaled = make_scalable(X_train)
#print(X_train_scaled)
#y_train_scaled = preprocessing.normalize(y_train)
#X_test_scaled = make_scalable(X_test)
#print(X_test_scaled)
#y_test_scaled = make_scalable(y_test)

#print(X_train)

#print(y_test_scaled)

svc_model.fit(X_train, y_train)

y_predict = svc_model.predict(X_test)
print(svc_model.score(X_test,y_test))
matrix = classification_report(y_test,y_predict)
print(matrix)

########			Predict using forecast data 			########

forecast_inp = forecast_data.reshape(1,-1)
field4 = svc_model.predict(forecast_inp)
#print(field4)
#print(str(float(field4)))

######## 			upload predicted value to channel			########

upload_data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=H6XCST902X08B6V8&field1="+str(temp)+"&field2="+str(humidity)+"&field4="+str(float(field4)))


######## 			Kmeans clustering 			########
forecast_new = pd.read_csv("https://api.thingspeak.com/channels/998677/feeds.csv")
field4_inp = forecast_new['field4']
field4_inp = field4_inp.values.reshape(-1,1)

km = KMeans(n_clusters=2)
clus = km.fit_predict(field4_inp)
#print(len(clus))
centroids = km.cluster_centers_
print(centroids)



########           Send Email notification to blynk app      ########

if (field4>=centroids[0] or field4>=centroids[1]):
	BLYNK_AUTH = 'BL6PB5eysjs-Bfzc4ptPk6_4cesG1dV2'
	TARGET_EMAIL = 'beprojectbgv@gmail.com'
	blynk = blynklib.Blynk(BLYNK_AUTH)
	EMAIL_PRINT_MSG = "[EMAIL WAS SENT to '{}']".format(TARGET_EMAIL)

	@blynk.handle_event("connect")
	def connect_handler():
		print('Sleeping 2 sec before sending email...')
		time.sleep(2)
		blynk.email(TARGET_EMAIL, 'SMART IRRIGATION SYSTEM', 'WATER YOUR FIELD!')
		print(EMAIL_PRINT_MSG)

###########################################################
# infinite loop that waits for event
###########################################################
	while True:
		blynk.run()
        

'''forecast = pd.read_sql("SELECT temp,humidity,uv FROM air_forecast ORDER BY timestamp DESC LIMIT 1",mydb)
#print(forecast)
mycursor.execute("SELECT timestamp FROM air_forecast ORDER BY timestamp DESC LIMIT 1")
timestamp = mycursor.fetchall()
#print(timestamp)
for x in timestamp:
  print(x)


forecast_list = forecast.values.tolist()
new_forecast=np.array([forecast_list])
forecast_scaled = make_scalable(new_forecast)
new_forecast_scaled = forecast_scaled.reshape(1,-1)
pred_soil_moisture = svc_model.predict(new_forecast_scaled)

sql = "INSERT INTO air_forecast (soil_mois,timestamp) VALUES (%s,%s)"
val = (pred_soil_moisture)

mycursor.execute(sql, val)

mydb.commit()'''