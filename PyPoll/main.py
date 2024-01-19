# Import functionality of CSV & operating system modules
import csv
import os

# Find the CSV I am working on in my computer directory and make it accessible to Python
directory_path = r'python-challenge/PyPoll/Resources
file_name = 'election_data.csv'
csv_path = os.path.join(directory_path, file_name)

# Create a variable for the output file
output_file = 'output.txt'

# Specify the full path where you want to save the file
output_file_path = os.path.join(directory_path, output_file)

#-----------

# Find the total number of votes
# First specify the column I am working in (C) and initialize the variable of votes

column_index = 2
total_votes = 0

# Open the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the first row 
    next(csv_reader)
    
    # Loop through each row, adding one vote to total votes for each entry
    for row in csv_reader:
        if len(row) > column_index:
             total_votes += 1

#--------

# Specify the candidate names we are searching for as search strings. We are searching in column C. The count starts at 0 for each string.
search_strings = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
column_index = 2  
string_counts = {search_string: 0 for search_string in search_strings}

# Open the CSV file 
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Loop through each row and add one to the string count for every instance of the search string term recorded
    for row in csv_reader:
        if len(row) > column_index:
            cell_value = row[column_index]
            for search_string in search_strings:
                if cell_value == search_string:
                    string_counts[search_string] += 1

# Find the election winner by finding the string with the maximum number of counts                  
winner = max(string_counts, key=string_counts.get)

# Print the results of the total votes 
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")

# ----------------
# Find the percentage of votes each candidate received by dividing every string count by the total votes variable. 

for search_string, count in string_counts.items():
    percentage = (count / total_votes) * 100
    # Print the results of the calculation 
    print(f'{search_string}: {percentage:.3f}% ({count})')
print("-----------------------------")
# Print the candidate with the most votes 
print(f'Winner: {winner}')

with open(output_file_path, 'w') as output_file:
    # Write the string to the file
    output_file.write("Election Results")
    output_file.write(f"Total Votes: {total_votes}")
    output_file.write("-----------------------------")
    output_file.write(f'{search_string}: {percentage:.3f}% ({count})')
    output_file.write("-----------------------------")
    output_file.write(f'Winner: {winner}')
