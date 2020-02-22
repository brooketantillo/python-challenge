# Modules
import os
import csv

# set file path
budget_csv = os.path.join('..','PyBank', 'budget_data.csv')
path_output = os.path.join('..','PyBank', 'budget_data.txt')

# set up different variables
total_months = 0
monthly_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
total_net = 0
average_monthly_change = 0

# open csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    date = next(csvreader)
    total_months = total_months + 1
    net = total_net + int(date[1])
    prev_net = int(date[1])

    # start the loop for the data
    for line in csvreader:
        total_months = total_months + 1
        net = net + int(line[1]) 
        
        change = int(line[1]) - prev_net
        prev_net = int(line[1])
        net_change_list = net_change_list + [change]
        monthly_change = monthly_change + [line[0]]

        if (change > greatest_increase[1]):
            greatest_increase[0] = [line[0]]
            greatest_increase[1] = change

        if (change < greatest_decrease[1]):
            greatest_decrease[0] = [line[0]]
            greatest_decrease[1] = change

average_monthly_change = sum(net_change_list) / len(net_change_list)  


output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net}\n"
    f"Average Monthly Change: {average_monthly_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

# export text file
with open(path_output, "w") as txt_file:
    txt_file.write(output)