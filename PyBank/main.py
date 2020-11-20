import os
import csv

#Variables
total_months = 0
total_revenue = 0
previous_profit = 0
changes = []
date_count = []
greatest_incr = 0
greatest_incr_month = 0
greatest_dec = 0
greatest_dec_month = 0

#Path set for File
csvpath = os.path.join('', 'PyBank', 'Resources', 'budget_data.csv')

#Open CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculation for total number of months and total revenue.
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])




    for row in csvreader:
        #The total number of months in the set.
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        #Calculation for changes that occured from one month to the previous months.
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])

         #Calculations for the greatest increase.
        if int(row[1]) > greatest_incr:
             greatest_incr = int(row[1])
             greatest_incr_month = row[0]

        #Calculations for the greatest decrease profits.
        if  int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]

    #Calculations for the dates and averages.
    average_change = sum(changes)/ len(changes)

    high = max(changes)
    low = min(changes)

#Print report
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits:{greatest_incr_month}(${high})")
    print(f"Greatest Decrease in Profits:{greatest_dec_month}(${low})")

#Write results to specified folder
output_file = os.path.join('','PyBank', 'Analysis', 'Financial_Analysis.txt')

#Open File to specify data.
with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_revenue}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_incr_month} (${high})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${low})\n")



    

    