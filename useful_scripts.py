# get the list of prices
prices = driver.find_elements(By.XPATH, "//*[@class='standardprice']")
prices_list = []
for value in prices:
    prices_list.append(value.text)

# remove unnecessary elements and convert to int
string = ''.join(prices_list).replace("$", " ").replace(".00", " ").split("  ")
convert_int = [int(x) for x in string]
print(convert_int)

# create list within selected filter
selected_prices = [x for x in convert_int if 25 <= x < 50]
print(selected_prices)

# check if filtered prices are correct
if len(convert_int) == len(selected_prices):
    print("Price filter works fine")
else:
    raise Exception('Price filter works incorrectly')



