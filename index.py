hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for k in prices:
  total_price += k
print(total_price)

average_price =  total_price / len(prices)
print("Average Haircut Price: $" + str(average_price))

new_prices = [l - 5 for l in prices]
print(new_prices)

new_total_price = 0

for j in new_prices:
  new_total_price += j
print(new_total_price)

new_average_price = new_total_price / len(new_prices)
print("New Average Haircut Price: $" + str(new_average_price))

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue = prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyle for hairstyle, price in zip(hairstyles, new_prices) if price < 30]
print(cuts_under_30)