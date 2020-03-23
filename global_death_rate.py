#!/usr/local/bin/python3
import requests
import json
import dateutil.parser
import datetime

#params
#per_country = str(input('Looking for one specifict country? (yes/no) ').lower())
#all_countries = str(input('All countries? yes/no ').lower())


#get json
url = 'https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats'
headers = {
        "x-rapidapi-host": "covid-19-coronavirus-statistics.p.rapidapi.com",
        "x-rapidapi-key": "106f80e209msh7b615fb2a5ca0cep168f82jsnc69891b6353c"
}

data = requests.get(url, headers=headers)
data_json = data.json()

#Global Data
global_stats = [n for n in data_json['data']['covid19Stats']]
global_cases = sum([c['confirmed'] for c in global_stats])
global_deaths = sum([c['deaths'] for c in global_stats])
global_death_rate = round((global_deaths/global_cases)*100, 2)

#Print global
print('\nGlobal number of cases: ')
print(str(f'{global_cases:,}'))
print('\nGlobal number of deaths: ')
print(str(f'{global_deaths:,}'))
print('\nGlobal fatality rate: ')
print(str(global_death_rate)+'%')

#All countries
#if all_countries == 'yes':
#        for c in global_stats:
#                print('Country: ' + c['country'])
#                cases = c['confirmed']
#                deaths = c['deaths']
#                print('Cases: ' + str(cases))
#                print('Deaths: ' + str(deaths))
#                if deaths != 0:
#                        fatality = (deaths/cases)*100
#                        print('Fatality rate: ' + str(round(fatality, 2)) + '%')
#                print('\n')

print('\n')

#Specific Country
#if per_country == 'yes':
country = str(input('What country to look for? ').title())
query = {
        'country': country
}
data = requests.get(url, headers=headers, params=query)
data_json = data.json()
date_obj = dateutil.parser.parse(data_json['data']['lastChecked'])
date_str = date_obj.strftime('%B %d, %Y')
def finddata(variable):
        search = data_json['data']['covid19Stats'][0][variable]
        return search
country = finddata('country')
confirmed = finddata('confirmed')
recovered = finddata('recovered')
deaths = finddata('deaths')
fatality_rate = round((deaths/confirmed)*100, 2)
print('\nCovid19 stats on ' + str(date_str) + ' for ' + country.title())
print('Confirmed cases: ' + str(f'{confirmed:,}'))
print('Deaths: ' + str(f'{deaths:,}'))
print('Recovered: ' + str(f'{recovered:,}'))
print('Fatality Rate: ' + str(fatality_rate)+'%')

