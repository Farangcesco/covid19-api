import requests

#Look up specific country

country = ['Switzerland', 'Thailand', 'Italy']
country_data_json = []
for c in country:
        url_county_name = 'https://coronavirus-19-api.herokuapp.com/countries/' + c
        country_data = requests.get(url_county_name)
        country_data_json.append(country_data.json())

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
