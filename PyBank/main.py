
#modules
import os
import csv

#set path for file
csvpath = os.path.join( 'Resources', 'budget_data.csv')

with open( csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#read the header row first
    csv_header = next(csvreader)
    total_months = []
    net_profit = []
    profit_change = []

    #read through each row of data after the header 
    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1]))
        
    for i in range(len(net_profit)-1):
        profit_change.append(net_profit[i+1]-net_profit[i])


increase = max(profit_change)
decrease = min(profit_change)
monthly_increase = profit_change.index(max(profit_change))+1
monthly_decrease = profit_change.index(min(profit_change))+1

# print statement 
print("Financial Analysis")
print("-------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(net_profit)}")
print(f"Average Change:{round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(decrease))})")

# export financial analysis
output = "output.txt"
with open("output","w") as new:

    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months:{len(total_months)}")
    print(f"Total: ${sum(net_profit)}")
    print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    print(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
    print(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(increase))})")
