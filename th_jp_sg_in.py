import requests

#Look up specific country

country = ['Thailand', 'Japan', 'Singapore', 'Indonesia']
country_data_json = []
for c in country:
        url_county_name = 'https://coronavirus-19-api.herokuapp.com/countries/' + c
        country_data = requests.get(url_county_name)
        country_data_json.append(country_data.json())


#Print Global
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
print(str(global_death_rate)+'%\n')
#print specific country
def get_variable2(data_json, variable):
        return data_json[variable]
for e in country_data_json:
        country = get_variable2(e, 'country')
        cases = get_variable2(e, 'cases')
        todayCases = get_variable2(e, 'todayCases')
        deaths = get_variable2(e, 'deaths')
        todayDeaths = get_variable2(e, 'todayDeaths')
        recovered = get_variable2(e, 'recovered')
        active = get_variable2(e, 'active')
        critical = get_variable2(e, 'critical')
        casesPerOneMillion = get_variable2(e, 'casesPerOneMillion')
        try:
                fatality_rate = (deaths/cases)*100
                r_fatality_rate = round(fatality_rate, 2)
        except:
                fatality_rate = 0        
        print('*********************')
        print('Country: ' + country)
        print('\nConfirmed Cases: ' + str(f'{cases:,}'))
        print('New cases today: ' + str(f'{todayCases:,}'))
        print('Deaths: ' + str(f'{deaths:,}'))
        print('Deaths today: ' + str(f'{todayDeaths:,}'))
        print('\nFatality Rate: ' + str(r_fatality_rate) + '%')
        print('\nRecovered Patients: ' + str(f'{recovered:,}'))
        print('Patients under care: ' + str(f'{active:,}'))
        print('Critical Patients: ' + str(f'{critical:,}'))
        print('Cases per one million: ' + str(f'{casesPerOneMillion:,}'))
        print('*********************\n')
else:
        pass