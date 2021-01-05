# # Program to record temperature of various customers
# def customer():
#     name = input("Enter the name of the customer: ")
#     address = input("Enter the address of the customer: ")
#     days = int(input("Enter how many days the customer wants to record temperature: "))
#     temperature = []
#     average_temp = 0
#     print("Please enter {0} days' temperature readings".format(days))
#     for x in range(days):
#         temp = int(input("Temperature day [{0}] = ".format(x + 1)))
#         temperature.append(temp)
#         average_temp += temp
#
#     print(temperature)
#     calculate_temperature_range(temperature)
#
#     return name, address, temperature, average_temp
#
#
# def calculate_temperature_range(temperature):
#     temperature_report = {}
#     days_report = []
#     hot_days = 0
#     pleasant_days = 0
#     normal_days = 0
#     cold_days = 0
#     for x in temperature:
#         if x > 50:
#             temperature_category = 'Very Hot'
#             day_category = 'A'
#             hot_days += 1
#         elif 50 >= x > 40:
#             temperature_category = 'Pleasant Day'
#             day_category = 'B'
#             pleasant_days += 1
#         elif 40 >= x > 25:
#             temperature_category = 'Normal Day'
#             day_category = 'C'
#             normal_days += 1
#         elif x <= 25:
#             temperature_category = 'Very Cold'
#             day_category = 'D'
#             cold_days += 1
#
#         temperature_report[x] = [temperature_category, day_category]
#         days_report = [hot_days, pleasant_days, normal_days, cold_days]
#         print(temperature_report)
#
#     return temperature_report, days_report
#
#
# number_of_customers = int(input("Enter the number of customers: "))
# for n in range(number_of_customers):
#     name, address, temperature, average_temp = customer()
#     for n in range(number_of_customers):
#         print("\t\tDaily Temperature Report")
#         print("--------------------------------------------------------")
#         print("Customer[{0}]: {1}\t\t\t\t\t\tAddress: {2}".format(n + 1, name, address))
#         for x in temperature:
#             print("Temperature day [{0}] = ".format(x + 1))
#         print("The average temp for {0} days = {1}".format(len(temperature)))
#         print("Number of Hot days = ".format())
#         print("Number of Pleasant days = ".format())
#         print("Number of Normal days = ".format())
#         print("Number of Cold days = ".format())
#         print("\t\tDays Category")
#         print("Number of A Category days = ".format())
#         print("Number of B Category days = ".format())
#         print("Number of C Category days = ".format())
#         print("Number of D Category days = ".format())
#         print("--------------------------------------------------------")
#
