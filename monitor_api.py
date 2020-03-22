import requests

#Look up specific country
country = str(input('What country do you want to look up? ').title())
print_all_country = input('Print all countries? yes/no ').lower()
url_county_name = 'https://coronavirus-19-api.herokuapp.com/countries/' + country

#print specific country
country_data = requests.get(url_county_name)
country_data_json = country_data.json()

def get_variable(variable):
        return country_data_json[variable]

country = get_variable('country')
cases = get_variable('cases')
todayCases = get_variable('todayCases')
deaths = get_variable('deaths')
todayDeaths = get_variable('todayDeaths')
recovered = get_variable('recovered')
active = get_variable('active')
critical = get_variable('critical')
casesPerOneMillion = get_variable('casesPerOneMillion')
try:
        fatality_rate = (deaths/cases)*100
        r_fatality_rate = round(fatality_rate, 2)
except:
        fatality_rate = 0        

print('\nCountry: ' + country)
print('\nConfirmed Cases: ' + str(f'{cases:,}'))
print('New cases today: ' + str(f'{todayCases:,}'))
print('Deaths: ' + str(f'{deaths:,}'))
print('Deaths today: ' + str(f'{todayDeaths:,}'))
print('\nFatality Rate: ' + str(r_fatality_rate) + '%')
print('\nRecovered Patients: ' + str(f'{recovered:,}'))
print('Patients under care: ' + str(f'{active:,}'))
print('Critical Patients: ' + str(f'{critical:,}'))
print('Cases per one million: ' + str(f'{casesPerOneMillion:,}'))


#for k, v in country_data_json.items():
#        if isinstance(v, str):
#                print(k.title() + ': ' + v)
#        else:
#                print(k.title() + ': ' + str(f'{v:,}'))
#



#print stuff
if print_all_country == 'yes':
        url_all = 'https://coronavirus-19-api.herokuapp.com/all'
        url_countries = 'https://coronavirus-19-api.herokuapp.com/countries'

        countries_data = requests.get(url_countries)
        countries_json = countries_data.json()
        #World stats
        url_all = 'https://coronavirus-19-api.herokuapp.com/all'
        all_data = requests.get(url_all)
        all_data_json = all_data.json()

        w_cases = all_data_json['cases']
        w_deaths = all_data_json['deaths']
        w_recovered = all_data_json['recovered']
        w_fatality_rate = (w_deaths/w_cases)*100
        w_r_fatality_rate = round(w_fatality_rate, 2)

        print('*'*8)
        print('*'*8)
        print('World Stats\n')
        print('Total Cases: ' + str(f'{w_cases:,}'))
        print('Total Deaths: ' + str(f'{w_deaths:,}'))
        print('Total Recovered: ' + str(f'{w_recovered:,}'))
        print('Global Fatality Rate: ' + str(f'{w_r_fatality_rate:,}') + '%')
        print('*'*8)
        print('*'*8)

        def get_variable2(data_json, variable):
                return data_json[variable]
        for e in countries_json:
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
                print('\nCountry: ' + country)
                print('\nConfirmed Cases: ' + str(f'{cases:,}'))
                print('New cases today: ' + str(f'{todayCases:,}'))
                print('Deaths: ' + str(f'{deaths:,}'))
                print('Deaths today: ' + str(f'{todayDeaths:,}'))
                print('\nFatality Rate: ' + str(r_fatality_rate) + '%')
                print('\nRecovered Patients: ' + str(f'{recovered:,}'))
                print('Patients under care: ' + str(f'{active:,}'))
                print('Critical Patients: ' + str(f'{critical:,}'))
                print('Cases per one million: ' + str(f'{casesPerOneMillion:,}'))
                print('*********************')
else:
        pass