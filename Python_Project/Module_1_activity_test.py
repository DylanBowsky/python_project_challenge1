#Conditional Activity 
# 1. @TODO: Create two new variables to hold user data:
# Populate this variable with our first user, who is based in the United States
# and is already registered on the platform.
# YOUR CODE HERE!
location = "United States"
registered = True
if location == "United States" and registered:
    print("Now Available! Crypto Accepted!")
else:
    print("Crypto Payments - Coming Soon!")
# 2. @TODO: Write a conditional statement. If user is based in the U.S. and
# already registered, advertise the new service. Otherwise, give them
# notice that the feature is coming soon.
# YOUR CODE HERE!

# 3. @TODO: Change the user location to Japan and print the results again.
# Does your conditional statement program work as expected?
# YOUR CODE HERE!
location = "Japan"
registered = True
if location == "United States" and registered:
    print("Now Available! Crypto Accepted!")
else:
    print("Crypto Payments - Coming Soon!")

#Nested Conditionals Acitivity
# @TODO: Create variables with the initial ad price and company type
# YOUR CODE HERE!
initial_ad_price = 15.00
company_type = "Existing"
# @TODO: Convert the following decision logic into valid Python code.
# if the ad price is affordable (less than 20):
#     if the company is a startup:
#         print that the expected profit is 500
#     elif the company is existing:
#         print that the expected profit is 100
#     else:
#         print that the company type is not specified
# else:
#     print that the ad price is too expensive
if initial_ad_price < 20.00:
    if company_type == "Start up":
        print("We are expecting $500 in profit")
    elif company_type == "Existing":
        print("We are expecting $100 in profit")
else:
    print("This ad is too expensive")

#Future and Present Value Activity
# @TODO: # Use the following variables for present value calculations.
home_price = 115000  # Investment cost
expected_sale_price = 130000  # Future Value of the home
hurdle_rate = 0.09  # 0.10 = 10% # Annual Discount Rate; minimum return expected
holding_months = 12  # Number of months until sold (until Future Value)

# @TODO: Using `expected_sale_price`, `hurdle_rate`, and `holding_months`,
# calculate the present value of the home. Save the result as a new
# variable named `present_value`.
# Use the **monthly** version of the present value formula. 
# YOUR CODE HERE!
present_value = (expected_sale_price)/(1+(hurdle_rate/holding_months))** holding_months
print(f"Present Value is ${present_value: .2f}")

# @TODO: Put `present_value` into a conditional statement:
# If present value is greater than cost to buy (home_price), print a statement to buy the property:
# Otherwise, print a statement that you will pass on the opportunity:
# Bonus! The edge case: print that you expect to break even on this deal
# YOUR CODE HERE
if present_value > home_price:
    print("Buy the property")
elif present_value < home_price:
    print("We will pass on this opportunity")
elif present_value == home_price:
    print("This is the break even case you will earn", hurdle_rate)

    # @TODO: Create a function that prints two messages.
# The first message should state the cost of the transaction.
# THe second message should state that the payment has been processed.
# YOUR CODE HERE
def process_payment():
    print("The total cost of this transaction will be 75 cents")
    print("Ka-ching! Payment has been processed.")

# Call the function to run the code in the function.
process_payment()

#Returned goods activity 
# @TODO: Define a new function called process_claims
# Inside of the function:
# Create a variable called `total_claims`, that is the sum of all claims
# Calculate a total payout, which is 30% of total_claims:
# Return only the total_payout amount
def process_claims(claims):
    total_claims=sum(claims)
    total_payout= total_claims * .30
    return total_payout

# @TODO Paste the list of weekly claims:
weekly_claims = ([5000, 1000, 8000, 10000, 3000, 3500])

# What's the total insurance payout?
# Use the print() statement to print the returned value from the function.
# @TODO: Call the function using `weekly_claims` as the function argument
# YOUR CODE HERE!
total_insurance_payout=  process_claims(weekly_claims)
print(f"The total insurance payout for the week is ${total_insurance_payout: .2f}")








#Present/ Future Value Advance
# @TODO: Create a function called `price_this_home`.
# This function should have the following 4 parameters: home_price, expected_sale_price, hurdle_rate, holding_months
# Inside of the function:
    # Calculate the present value
    # HINT: Present Value = Future Value (Face Value of the Loan) / (1 + annual_discount_rate/12) ** remaining_months        
def price_this_home(home_price, expected_sale_price, hurdle_rate, holding_months):
        present_value = expected_sale_price / (1 + (hurdle_rate / 12)) ** holding_months

    # Put `present_value` into a conditional statement:
    # If present value is greater than cost to buy (home_price), buy it:
        if present_value > home_price:
            print("Buy this one, junior analyst! It's worth more than it's selling for.")
    # Otherwise, take a pass:
        elif present_value < home_price:
            print("Don't buy this, as it's offered at a price higher than what it's worth.")
    # Bonus! The edge case:
        elif present_value == home_price:
            print(
            "Breakeven case! You can expect to earn exactly your hurdle rate on this deal.")
             
    # Have the function calculate and return the expected profit, or `net_present_value`, of the home being evaluated. 
    # This is defined as the `present_value` of the home, minus the `current home_price`.
        net_present_value = present_value - home_price
    # @TODO: Return the net_present_value (the expected profit)
    # YOUR CODE HERE!
        return net_present_value

# Run the function
npv = price_this_home(home_price=100000, expected_sale_price=180000, hurdle_rate=0.10, holding_months=36)

# Print the npv
print(f"The Expected Profit is: ${npv: .2f}")



# Suppose each stock price is the same
stock_price = 30

# But that dividend yields vary across five stocks in your portfolio
dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]

# @TODO: Create a variable to hold tallied dividend income
# YOUR CODE HERE!
total_dividen_income = 0
# @TODO: Create a for loop to calculated and add up all the dividend income
# YOUR CODE HERE!
for div_yield in dividend_yields:
    dividen_income = div_yield * stock_price
    total_dividen_income = total_dividen_income+ dividen_income
    print("Your dividen income will be", dividen_income)
# @TODO: Once it's all done, print the dividend income for the entire portfolio
# YOUR CODE HERE!
print("The total dividen icnome in my portfolio is", total_dividen_income)

