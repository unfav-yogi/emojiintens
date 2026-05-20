import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim
import time

df = pd.read_csv(r"C:\Users\yoeshwar\OneDrive\Desktop\internships\cleaned_superstore.csv")

print(df.head())

print(df.columns)

df = df.dropna()

state_sales = df.groupby("State")["Sales"].sum().reset_index()

city_sales = df.groupby("City")["Sales"].sum().reset_index()

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

top_states = state_sales.sort_values(by="Sales", ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(data=top_states, x="State", y="Sales")
plt.title("Top 10 States by Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,8))
plt.pie(
    region_sales["Sales"],
    labels=region_sales["Region"],
    autopct='%1.1f%%'
)
plt.title("Region Wise Sales Distribution")
plt.show()

top_cities = city_sales.sort_values(by="Sales", ascending=False).head(20)

geolocator = Nominatim(user_agent="geo_project")

latitudes = []
longitudes = []

for city in top_cities["City"]:

    try:
        location = geolocator.geocode(city)

        if location:
            latitudes.append(location.latitude)
            longitudes.append(location.longitude)

        else:
            latitudes.append(None)
            longitudes.append(None)

        time.sleep(1)

    except:
        latitudes.append(None)
        longitudes.append(None)

top_cities["Latitude"] = latitudes
top_cities["Longitude"] = longitudes

top_cities = top_cities.dropna()

plt.figure(figsize=(12,6))
sns.scatterplot(
    data=top_cities,
    x="Longitude",
    y="Latitude",
    size="Sales",
    sizes=(100,1000)
)

for i in range(len(top_cities)):
    plt.text(
        top_cities["Longitude"].iloc[i],
        top_cities["Latitude"].iloc[i],
        top_cities["City"].iloc[i]
    )

plt.title("High Demand Areas for Business Expansion")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

recommended = top_cities.sort_values(by="Sales", ascending=False).head(5)

print(recommended[["City", "Sales"]])

recommended.to_csv("recommended_locations.csv", index=False)

print("PROJECT COMPLETED SUCCESSFULLY")