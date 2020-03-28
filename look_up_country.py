import json
import requests
import dateutil.parser
import datetime

#get country to look up
country = input(str('What country to look for? (ISO country code) ')).upper()

#methods
def f_number(n):
        return str(f'{n:,}')

def get_variables_locations(v):
        return country_data_json['locations'][0][v]

# data of country to look up
base_url = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code='
countr_data = requests.get(base_url+country)
country_data_json = countr_data.json()

#data global
latest_url = base_url.replace('locations?country_code=', 'latest', 1)
latest_data = requests.get(latest_url)
latest_json = latest_data.json()

#global variables
global_confirmed = latest_json['latest']['confirmed']
global_deaths = latest_json['latest']['deaths']
global_recovered = latest_json['latest']['recovered']
global_fatality_rate = global_deaths/global_confirmed*100
r_global_fatality_rate = round(global_fatality_rate, 2)
global_population = 7800000000
global_p_of_pop_infected = global_confirmed/global_population*100
r_global_p_of_pop_infected = round(global_p_of_pop_infected, 4)

#country cariables
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

#print global
print(f'\nLast updated on {date_str}\n')
#print(f'Last updated on {date_str}\n')
print('Global Stats\n')
print(f'Confirmed cases: {f_number(global_confirmed)}')
print(f'Deaths: {f_number(global_deaths)}')
print(f'Recovered: {f_number(global_recovered)}')

print(f'\nFatality rate: {f_number(r_global_fatality_rate)}%')
print(f'Percentage of global population infected: {r_global_p_of_pop_infected}% ')

#print country
print(f'\nStats for {country}\n')

print(f'Confirmed Cases: {f_number(confirmed)}')
print(f'Deaths: {f_number(deaths)}')
print(f'Recovered: {f_number(recovered)}\n')

print(f'Fatality Rate: {r_fatality_rate}%\n')

print(f'Population: {f_number(population)}')
print(f'Percentage of population infected: {r_p_of_pop_infected}% ')