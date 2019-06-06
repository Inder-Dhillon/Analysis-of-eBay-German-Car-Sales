import pandas as pd
import numpy as np
cars = pd.read_csv('autos.csv',encoding='Latin-1')

#Checking dataset info
#print(cars.info(),'\n')
#print(cars.head(),'\n')
#print(cars.columns)

#Converting column names from camelCase to snakecase
cars.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest',
       'vehicle_type', 'registeration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registeration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'nr_of_pictures', 'postal_code',
       'last_seen']

# seller, offer_type and nr_of_pictures columns can be deleted as they have the same value and provide no insight
cars = cars.drop(["seller","offer_type","nr_of_pictures"],axis=1)
#Changing d-type of price and odometer
cars["price"] = cars["price"].str.replace("$","")
cars["price"] = cars["price"].str.replace(",","")
cars["price"] = cars["price"].astype(float)

cars["odometer"] = cars["odometer"].str.replace("km","")
cars["odometer"] = cars["odometer"].str.replace(",","")
cars["odometer"] = cars["odometer"].astype(int)

cars.rename({"odometer":"odometer_km"},axis=1, inplace=True)

#Finding outliers in price and odometer
#print(cars["price"].value_counts().sort_index(ascending=True))

#Handling said outliers
cars = cars[cars["price"].between(1,351000)]