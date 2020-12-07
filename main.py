import sys
from os import path, getcwd
from time import perf_counter

def read_file(filename):
  try:
    with open(filename) as f:
        content = f.readlines()

    # I converted the file data to integers because I know 
    # that the input data is made up of numbers greater than 0
    content = [info.strip() for info in content]

  except:
    print('Error to read file')
    sys.exit()

  return content

def find_id_seat(data):
  list_ids = {
    int(
      letter.translate(str.maketrans('FBLR', '0101')), 2
      ) for letter in data
  }

  return list_ids

if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'inputData.txt')
    input_data = read_file(filename)

    result = find_id_seat(data=input_data)

    print(f'Result: {max(result)}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)