


tech_stocks = []

tech_stocks.append("AAPL")
tech_stocks.append("GOOG")
tech_stocks.append("AMZN")

closing_price =[12.3,12.80,12.54,12.9,12.01]
highest_closing_price = max(closing_price)
#print(highest_closing_price)

number_of_prices_= len(closing_price)

#Dictionary list practice The keys are the stock prices and the stock price is the value
my_stocks_dictionary = {"AAPL": 445.32, "GOOG": 1485.82, "AMZN": 750.20}
top_traders_per_month = {}
top_traders_per_month ["January"] = "Susan" 
top_traders_per_month ["February"] = "Samuel"
#print(top_traders_per_month)

#Conditional practice before lesson activity
stock_price = 12.00
estimated_value = 18.25
buy_stock = stock_price < estimated_value
buy_stock = True
if buy_stock: 
    print("Buy this stock because it is on sale!")
else:
    print("Don't buy this stock it is too expensive")
print(buy_stock = stock_price < estimated_value)
task_completed = True
all_tasks_completed = False

its_raining = True
if its_raining:
    print("Bring an umbrella")
else:
    print("Wear some sunglasses!")


#double equal sign is letting us verify the variable
issue_currency = "CAD"
price = 30.00

if issue_currency == "USD": 
    print("The price is $", price)
else:
    print("The currency is not in USD.")

#Compound test with multiple conditionals
issue_currency = "USD"
price = 30.00

if issue_currency == "USD" and price< 40.00: 
    print("The price is $",price, "So we should buy")
else:
    print("The currency is not in USD.")

#Complex conditional statements
issue_currency = "USD"
price = 30.00

if issue_currency == "USD": 
    print("The price is $", price)
elif issue_currency == "EUR":
    print("The currency is", price)
else:
    print("The currency is not in USD or EUR.")

#Nested multiple conditionals
issue_currency = "USD"
price = -30.00
if price >= 0:
    
    if issue_currency == "USD": 
        print("The price is $", price)
    elif issue_currency == "EUR":
        print("The currency is", price)
    else:
        print("The currency is not in USD or EUR.")
else:
    print("Error, price is listed as a negative number")

#Function work
def add(first_number,second_number):
    total= first_number + second_number
    print("Your total is", total)
add(1,1)
add(2,3)
add(42,5001)
def scream():
    print("AAAAHHH")
scream()
scream()

def average_number(numbers):
    return sum(numbers)/len(numbers)
first_average = average_number([1,2,3])
second_average = average_number([4,5,6])
print(first_average, second_average)

#Lesson 6 practice loops
#the list of words are the iterable here
words = [ "cool", "awesome!", "why am I shouting?"]
#the for is what we use to grab each item from list above
#make sure indents are correct
for word in words:
    print("Original word", word)
    print("Uppercase Word", word.upper())
    print("Title Word", word.title())

principle = 103208.56
interest_rates = [.103, .067,.099,.10]
total_interest = 0.0
for rate in interest_rates:
    interest = rate * principle
    total_interest = total_interest + interest
    print(f"Your interest will be {interest: .2f}")
print(f"The total interest is {total_interest: .2f}%")

#nested data containers
table_data = [
    ["Ticker", "Open", "Close"],
    ["APPL", 363.25, 363.40],
    ["AMZN", 2756.00, 2757.99],
    ["GOOG", 1409.10, 1408.2]
]

for row in table_data:
    ticker = row[0]
    open = row[1]
    close = row[2]
    print(ticker)
    print(close)

#ways to create a variable and call it from the list index we created from above
#amazon_data = table_data[2]
#amazon_opening_price = amazon_data[1]
#amazon_closing_price = amazon_data[2]
#you can also combine the steps above
#apple_data = table_data[1]
#apple_opening_price = table_data[1][1]
#apple_closing_price= table_data[1][2]

#dictionary list and loops
table_data_dictionary = [
    {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.40
    },
    {
        "Ticker": "AMZN",
        "Open": 2756.0,
        "Close": 2757.99
    },
    {"Ticker": "GOOG",
    "Open": 1409.1,
    "Close": 1408.2
    }
]

for item in table_data_dictionary:
    ticker = item["Ticker"]
    #alternative method could be using ticker= item.get("Ticker")
    print(ticker)


