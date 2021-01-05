# Program to record temperature of various customers
def customer():
    name = input("Enter the name of the customer: ")
    address = input("Enter the address of the customer: ")
    days = int(input("Enter how many days the customer wants to record temperature: "))
    temperature = []
    total = 0
    print("Please enter {0} days' temperature readings".format(days))
    for x in range(days):
        temp = int(input("Temperature day [{0}] = ".format(x + 1)))
        temperature.append(temp)
        total += temp

    average_temp = total / days

    # print(temperature)
    temperature_report, days_report = calculate_temperature_range(temperature)
    print(temperature_report)
    print(days_report)
    print("checker")
    return name, address, temperature, average_temp, temperature_report, days_report


def calculate_temperature_range(temperature):
    temperature_report = {}
    days_report = []
    hot_days = 0
    pleasant_days = 0
    normal_days = 0
    cold_days = 0
    for x in temperature:
        if x > 50:
            temperature_category = 'Very Hot'
            day_category = 'A'
            hot_days += 1

        elif 50 >= x > 40:
            temperature_category = 'Pleasant Day'
            day_category = 'B'
            pleasant_days += 1

        elif 40 >= x > 25:
            temperature_category = 'Normal Day'
            day_category = 'C'
            normal_days += 1

        elif x <= 25:
            temperature_category = 'Very Cold'
            day_category = 'D'
            cold_days += 1

        temperature_report[x] = [temperature_category, day_category]
        print(temperature_report)

    days_report.append(hot_days)
    days_report.append(pleasant_days)
    days_report.append(normal_days)
    days_report.append(cold_days)
    print(days_report)

    return temperature_report, days_report


def main():
    print("\t\t\tTemperature Record System[TRS]")
    print("\t\t\t\t\tSunway Company Pvt. Ltd.")
    print("\t\t\t\t\t\tMaitidevi, Kathmandu")
    number_of_customers = int(input("Enter the number of customers: "))
    for n in range(number_of_customers):
        name, address, temperature, average_temp, temperature_report, days_report = customer()
        print(list(temperature_report))
        print(days_report)
        print("checker 2")
        print("\t\tDaily Temperature Report")
        print("--------------------------------------------------------")
        print("Customer[{0}]: {1}\t\t\t\t\t\tAddress: {2}".format(n + 1, name, address))
        y = 0
        for x in temperature:
            y += 1
            print("Temperature day [{0}] = {1} Celsius {2}\t\t{3} Category Day".format(y, x))
        print("The average temp for {0} days = {1}".format(len(temperature), average_temp))
        print("Number of Hot days = {0}".format(str(days_report[0])))
        print("Number of Pleasant days = {0}".format(str(days_report[1])))
        print("Number of Normal days = {0}".format(str(days_report[2])))
        print("Number of Cold days = {0}".format(str(days_report[3])))
        print("\t\tDays Category")
        print("Number of A Category days = {0}".format(str(days_report[0])))
        print("Number of B Category days = {0}".format(str(days_report[1])))
        print("Number of C Category days = {0}".format(str(days_report[2])))
        print("Number of D Category days = {0}".format(str(days_report[3])))
        print("--------------------------------------------------------")


main()
