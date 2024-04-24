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

    #Iterate through each instruction in the JSON data
    for instruction in data:
        # Append the length of input and output to their respective lists
        input_lengths.append(len(instruction['input']))
        output_lengths.append(len(instruction['output']))
    
#Calculatin the average input and output lengths
    avg_input_length = np.mean(input_lengths)
    avg_output_length = np.mean(output_lengths)
    
    # Calculate the standard deviation of input and output lengths
    std_input_length = np.std(input_lengths)
    std_output_length = np.std(output_lengths)

    return num_instructions, avg_input_length, std_input_length, avg_output_length, std_output_length

#Use the file path and name of your JSON file  
json_file = "NLPP.json"  # Make sure this path is correct
#Call the function to analyze the JSON file
num_instructions, avg_input_length, std_input_length, avg_output_length, std_output_length = analyze_json(json_file)

#Print the analysis results
print("Total Number of Instructions:", num_instructions)
print("Average Input Length:", avg_input_length)
print("Input Length Standard Deviation:", std_input_length)
print("Average Output Length:", avg_output_length)
print("Output Length Standard Deviation:", std_output_length)
  
