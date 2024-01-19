import csv
import os
import sys

# Find the CSV I am working on in my computer directory and make it accessible to Python
directory_path = r'C:\Users\vjmar\Desktop\DataScience\PythonHomework\03-Python\Starter_Code\PyBank\Resources'
file_name = 'budget_data.csv'
csv_path = os.path.join(directory_path, file_name)

# Create a variable for the output file
output_file = 'output.txt'

# Specify the full path where you want to save the file
output_file_path = os.path.join(directory_path, output_file)

# Open the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Create placeholder variables for every calculation I am looking for
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

    # Skip the first row
    next(csv_reader)

    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])

        # Add to the total months variable by one for each instance & add that month's profit/loss to the running net total
        total_months += 1
        net_total += profit_loss

        # For every additional month, create a list of profit/loss changes. Append every new profit/loss to the list.
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Every time the change is calculated, review if it is larger than the most recent greatest increase or greatest decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Update the previous profit loss with the information from each row looped over
        previous_profit_loss = profit_loss

# Find the average change by dividing the sum of the changes by the number of changes.
# Make sure the number of changes is not zero, or there will be a dividing by zero error.
average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

# Open the file in write mode ('w') with the specified path
with open(output_file_path, 'w') as output_file:
    # Write the string to the file
    output_file.write("Financial Analysis\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total Profit/Loss: {net_total}\n")
    output_file.write(f"Average Change: {average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} {greatest_increase['amount']}\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} {greatest_decrease['amount']}\n")

# Print the results to the console
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Net Total Profit/Loss: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} {greatest_increase['amount']}")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} {greatest_decrease['amount']}")

