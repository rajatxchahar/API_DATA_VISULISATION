import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Constants
API_KEY = 'your_openweathermap_api_key'  # Replace with your actual OpenWeatherMap API key
CITY = 'Mumbai'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Parse data
dates = []
temps = []

for entry in data['list']:
    dt = datetime.datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    dates.append(dt)
    temps.append(temp)

# Visualization using seaborn
sns.set(style="darkgrid")
plt.figure(figsize=(14, 6))
sns.lineplot(x=dates, y=temps)
plt.title(f'5-Day Temperature Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
