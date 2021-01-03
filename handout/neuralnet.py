import sys
import numpy as np

def get_data(file_input):
  data_list = []
  with open(file_input, "r") as file:
    file = np.loadtxt(file, delimiter = ",")
    for row in file:
      data_list.append(row[1:])
  data_list = np.asarray(data_list)
  return data_list

def get_labels(file_input):
  label_list = []
  with open(file_input, "r") as file:
    file = np.loadtxt(file)
    for row in file:
      label_list.append(row[0])
  label_list = np.asarray(label_list)
  return label_list

def main():
  #arguments
  train_input = sys.argv[1]
  validation_input = sys.argv[2]
  train_out = sys.argv[3]
  validation_out = sys.argv[4]
  metrics_out = sys.argv[5]
  num_epoch = sys.argv[6]
  hidden_units = sys.argv[7]
  init_flag = sys.argv[8]
  learning_rate = sys.argv[9]
  
  num_epoch = int(num_epoch)
  hidden_units = int(hidden_units)
  init_flag = int(init_flag)
  learning_rate = float(learning_rate)
  #get data_list and label_list from input file
  train_data = get_data(train_input)
  train_labels = get_labels(train_input)
  validation_data = get_data(validation_input)
  validation_labels = get_labels(validation_input)
  #initialize random or zero
  weights
if __name__ == "__main__":
  main()
  print("Done.")