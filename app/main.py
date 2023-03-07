import utils 
import read_csv_file as read
import charts


def run():
  data = read.read_csv('./app/data.csv')
  country = input('Type Country => ')

  result = utils.population(data,country)
  lab, val = utils.get_population(result)
  print(lab)
  print(val)
  charts.generate_bar_chart(lab, val)
  print('chart generated')


def run_world_pop():
  data = read.read_csv('./app/data.csv')
  countries = list(map(lambda df : df['Country/Territory'], data))
  print(countries)
  population_percent = list(map(lambda df : df['World Population Percentage'], data))
  charts.generate_pie_chart(countries, population_percent)
  
  
  
  
if  __name__ == '__main__': 
  #run()
  run_world_pop()
