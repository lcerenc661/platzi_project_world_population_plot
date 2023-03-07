import csv

def read_csv(path):
  data = []
  with open(path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    for row in reader :
      iterable = dict(zip(header,row))
      data.append(iterable)
    
    return data
    
  
    
if __name__ == '__main__':
  #data = read_csv('./app/data.csv')
  data = world_data('./app/data.csv')
