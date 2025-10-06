cost_price = float(input("Enter the total cost of making your product: "))
selling_price = float(input("Enter the price of selling your product: "))
if cost_price>selling_price:
    x = cost_price-selling_price
    loss = (x/cost_price)*100
    print("You lost ",loss,"% after selling your product")
elif cost_price == selling_price:
    print("No Change")
else :
    y = selling_price-cost_price
    profit = (y/cost_price)*100
    print("You gained ",profit,"% after selling your product")