import json
import requests
import dateutil.parser
import datetime

country = input(str('What country to look for? (ISO country code) ')).upper()

def f_number(n):
        return str(f'{n:,}')

def get_variables_locations(v):
        return country_data_json['locations'][0][v]

base_url = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code='
countr_data = requests.get(base_url+country)
country_data_json = countr_data.json()

country = get_variables_locations('country')
population = get_variables_locations('country_population')
latest = get_variables_locations('latest')
confirmed = latest['confirmed']
deaths = latest['deaths']
recovered = latest['recovered']
last_updated = get_variables_locations('last_updated')
fatality_rate = deaths/confirmed*100
r_fatality_rate = round(fatality_rate, 2)
date_obj = dateutil.parser.parse(last_updated)
date_str = date_obj.strftime('%B %d, %Y')
p_of_pop_infected = confirmed/population*100
r_p_of_pop_infected = round(p_of_pop_infected, 4)

print(f'\nCountry: {country}')
print(f'Last updated: {date_str}\n')

print(f'Confirmed Cases: {f_number(confirmed)}')
print(f'Deaths: {f_number(deaths)}')
print(f'Recovered: {f_number(recovered)}\n')

print(f'Fatality Rate: {r_fatality_rate}%\n')

print(f'Population: {f_number(population)}')
print(f'Percentage of population infected: {r_p_of_pop_infected}% ')
