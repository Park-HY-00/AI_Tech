import csv

line_counter = 0
data_header = []
customer_list = []

with open("C:\\Users\\user\\OneDrive\\바탕 화면\\AI_Tech\\5-2\\customers.csv") as customer_data:

    while True:
        data = customer_data.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer_list.append(data.split(", "))
        line_counter += 1

print("Header :\t", data_header)
for i in range(0, 10):
    print("Data", i, ":\t", customer_list[i])
print(len(customer_list))
