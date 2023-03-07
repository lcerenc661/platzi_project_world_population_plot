import read_csv_file as rcf

data = rcf.read_csv('./app/data.csv')

def population(data, country):
  result = list(filter(lambda data : data['Country/Territory'] == country, data))
  return result

def get_population(country_dict):
  population_dict = {
    '2022' : country_dict[0]['2022 Population'],
    '2020' : country_dict[0]['2020 Population'],
    '2015' : country_dict[0]['2015 Population'],
    '2010' : country_dict[0]['2010 Population'],
    '2000' : country_dict[0]['2000 Population'],
    '1990' : country_dict[0]['1990 Population'],
    '1980' : country_dict[0]['1980 Population'],
    '1970' : country_dict[0]['1970 Population'],
  }
  keys = list(population_dict.keys())
  values = list(population_dict.values())
  values = [int(val) for val in values]
  
  return keys , values

if __name__ == "__main__":
  argentina_population = population(data,'Argentina')
  key, val = get_population(argentina_population)
  print(key, val)