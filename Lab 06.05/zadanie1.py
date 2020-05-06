import requests

data = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
with open('./result.csv', 'w') as csv:
    csv.write(data.text)