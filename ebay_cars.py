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

#Insights about the price and the odometer readings
print("The average price of a car on ebay is $5889 and the average odometer reading is 125770 km. "
      "Even at the 75% quartile price doesn't go over 7500 which means there aren't a lot of postings for expensive cars. "
      "More details below:")
print(cars[["price","odometer_km"]].describe(include='all'))

#Cleaning columns with dates
cars["ad_created"] = cars["ad_created"].str[:10]
cars["date_crawled"] = cars["date_crawled"].str[:10]
cars["last_seen"] = cars["last_seen"].str[:10]
print("\nMajority of the ads are from March and April, when the scraper ran, indicating that older car auctions (3 or more months older) did not sell.\n"
      "So can be easier to negotiate. \n"
      "If we were to go by the numbers you can expect your car to sell in 3-4 months after posting it on ebay.")
print(cars["ad_created"].str[:7].value_counts(normalize=True, dropna=False).sort_index(ascending=True))
print("\nObserving the ad posting behavior of the users, ads are posted pretty uniformly over the course of the month with not a lot of deviation.\n"
      "Same can be observed below")
print(cars["ad_created"].str[8:].value_counts(normalize=True, dropna=False))
print("\nThe Crawler ran for a month between March and April, scraping the majority ads in march as can be seen below:")
print(cars["date_crawled"].str[:7].value_counts(normalize=True, dropna=False).sort_index(ascending=True))

#Cleaning and analyzing registeration years
#print(cars["registeration_year"].describe())

#Minimum and maximum years for cars are given as 1000 and 9999 which are not possible.
cars = cars[cars["registeration_year"].between(1900,2016)]
print("\nThe registeration years of the cars posted on ebay can be visualized as a parabolic curve where the majority of cars posted are from the years 1999-2005."
      "\nSame can be seen below:")
print(cars["registeration_year"].value_counts(normalize=True).sort_index(ascending=True)[40:])


