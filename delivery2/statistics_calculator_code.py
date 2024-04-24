import json
import numpy as np

def analyze_json(json_file):
    #Open the JSON file with explicit encoding
    with open(json_file, 'r', encoding='utf-8') as f:
      data = json.load(f)
    #Count the number of instructions
    num_instructions = len(data)

    #Initialize lists to store input and output lengths
    input_lengths = []
    output_lengths = []

    # Iterate through each instruction in the JSON data
    for instruction in data:
        # Append the length of input and output to their respective lists
        input_lengths.append(len(instruction['input']))
        output_lengths.append(len(instruction['output']))


  
