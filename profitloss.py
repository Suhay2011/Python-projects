actual_cost = float(input("Please Enter an actual Product Selling price :"))
sale_amount = float(input("Please Enter a Sale Amount :"))

if (sale_amount  > actual_cost):
 
 amount = sale_amount - actual_cost
 print("Total Profit = {0}".format(amount))
else:
 print("NO PROFIT!")