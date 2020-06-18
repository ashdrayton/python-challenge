import os
import csv

pybank_csv = os.path.join("..","Resources","budget_data.csv")

total_month = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
total_net = 0

with open(pybank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

  
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_month = total_month + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

   
    for row in csvreader:
        total_month = total_month + 1
        total_net = total_net + int(first_row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_average = sum(net_change_list)/len(net_change_list)
print("Financial Analysis")
print(f"Total Months: {total_month}")
print(f"Total: ${total_net}")
print(f"Average Change: ${net_monthly_average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


PyBank_Results = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_month}\n"
   f"Total: ${total_net}\n"
   f"Average  Change: ${net_monthly_average}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
with open("output.txt", 'w') as txt_file:
    txt_file.write(PyBank_Results)
    

        

