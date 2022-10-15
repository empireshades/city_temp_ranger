import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Update this with a real API key if you use openweather
openweather_api='xxxxxxxxxlolwtfxxxxxxxxxxxxxxxxx'

# Cities and lat/lon in preferred order
latlon = {
    'LAS':('36.169941','-115.139832'),
    'NYC':('40.758180','-73.984602'),
    'LDN':('51.507351','0.127758'),
    'BAR':('41.385063','2.173404'),
    'BNG':('12.971599','77.594566'),
    'SEO':('37.5600','126.9900'),
    'SYD':('-33.8650','151.2094')
}

# Create empty forecast list
temps = []

for city in latlon:
    # change the units according to your liking (Celsius or Fahrenheit). Refer to openweather docs
    query_params = {'lat':latlon[city][0], 'lon':latlon[city][1], 'units':'imperial', 'appid':openweather_api}
    
    try:
        # Get the current temps
        curr = requests.get('https://api.openweathermap.org/data/2.5/weather', params=query_params)
        # "{:.0f}".format() is to round to 0 decimal places
        now = int("{:.0f}".format(curr.json()['main']['temp']))
        
        # Get the forecast to extract today's high and lows
        forecast = requests.get('https://api.openweathermap.org/data/2.5/forecast/daily', params=query_params)
        low = int("{:.0f}".format(forecast.json()['list'][0]['temp']['min']))
        high = int("{:.0f}".format(forecast.json()['list'][0]['temp']['max']))
        
        # Add city's dict to temporary list, to be parsed as dataframe later
        temps.append({'city':city, 'now':now, 'low':low, 'high':high})
    except:
        # If the above errs out, just all temps to 25
        temps.append({'city':city, 'now':25, 'low':25, 'high':25})


# transparent plot bg color, last 0 sets opacity to none
sns.set(rc={'axes.facecolor':(0,0,0,0), 'figure.facecolor':(0,0,0,0), 'grid.linestyle': '--', 'grid.color': '#303030',})

# alternatively set plot bg color to cornflowerblue
#sns.set(rc={'axes.facecolor':'cornflowerblue', 'figure.facecolor':'cornflowerblue'})

# or plot background color = #111111
#sns.set(rc={'axes.facecolor':'#111111', 'figure.facecolor':'#111111', 'grid.linestyle': '--', 'grid.color': '#303030',})

# Read in temp list of city dicts generated above. Reverse order so
# cities appear in correct order top down.
df = pd.DataFrame(temps).loc[::-1]

# The vertical plot is made using the hline function
#df = temps.sort_values(by='high')
fig, ax = plt.subplots(figsize=(3,5))
plt.tight_layout()

# Customize the grid
#ax.grid(linestyle='-', linewidth='0.5', color='red')
ax.yaxis.grid(False) # Hide the horizontal gridlines
ax.xaxis.grid(True) # Show the vertical gridlines

# axis labels
ax.tick_params(colors='#eeeeee', which='both')  # 'both' refers to minor and major axes

# Plot temperature text for current, high, and low temps
for i, j in enumerate(zip(df['now'], df['low'], df['high'])):
    # now (current) temp
    # draw current temp on the range line
    #ax.text(j[0]-2.8, i+1.1, str(j[0]), fontsize=18, color='#adadef')

    # draw current temp to the right of city name
    # logic is to take the lowest temp and set the x coord a few notches to the left
    ax.text(df['low'].min() - 6, i+.8, str(j[0]), fontsize=14, color='#adadef')

    # forecast low
    ax.text(j[1]-2, i+.7, str(j[1]), fontsize=12, color='#606060')

    # forecast high
    ax.text(j[2]-2, i+.7, str(j[2]), fontsize=12, color='#606060')

# Set axis font size
plt.xticks(fontsize=12)
plt.yticks(fontsize=14, rotation=70, va='center', position=(0,0.28))

# Set length to number of cities
length = range(1,len(df) + 1)

# Draw temp bar from low to high temp
plt.hlines(y=length, xmin=df['low'], xmax=df['high'], color='#a0a0a0', alpha=0.8)

# Plot low, high, and legend
plt.scatter(df['low'], length, color='skyblue', alpha=0.5, label='low')
plt.scatter(df['high'], length, color='#efabab', alpha=0.5, label='high')
#plt.legend(loc=4)

# kill legend (if needed)
#plt.legend([],[], frameon=False)

# Indicate current temp with a '|' marker
plt.scatter(df['now'], length, color='red', alpha=1, label='now', marker='|', s=100)

# Add some padding to the graph
#x1,x2,y1,y2 = plt.axis()
#plt.axis((x1,x2,y1 - .5 ,y2 + .5))
#plt.axis((x1,x2,y1,y2))

# Add title and axis names
plt.yticks(length, df['city'])

#plt.xlabel('Degrees F°', color='#999999')
#plt.ylabel('Cities', color='#999999')

# remove all borders
sns.despine(left=True, bottom=True)

# use this if displaying in jupyter notebook
#plt.show()

plt.savefig('weather.png')
