item_cost = [1, 2, 5, 1]
item_name = ["apple", "chips", "taco", "peanuts"]

item_cost_name = [item_name, item_cost]

def show_receipt(items, item_costs):
	total_cost = 0
	for i in range(0, len(items)):
		print(items[i])
		print(item_costs[i])
		total_cost += item_costs[i]
	print(total_cost)

show_receipt(item_name, item_cost)