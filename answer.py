# Program to record temperature of various customers
def input_area():
    print("\t\t\tTemperature Record System[TRS]")
    print("\t\t\t\tSunway Company Pvt. Ltd.")
    print("\t\t\t\t\tMaitidevi, Kathmandu")
    num_people = int(input("Enter how many customers record you wanted to store: "))

    all_data = [None] * num_people
    for i in range(num_people):
        all_data[i] = store_num(i)
    output_area(all_data)


def store_num(i):
    name = input("Enter the name of the {0} customer that wanted to record the temperature: ".format(str(i + 1)))
    add = input("Enter the address of {0} customer: ".format(str(i + 1)))
    how_many = int(input("Enter how many days {0} customer wanted to record temperature?: ".format(str(i + 1))))
    print("Please enter {0} days’ temperature readings".format(str(how_many)))
    data = [None] * how_many
    all_data = ""
    for j in range(how_many):
        data[j] = int(input("Temperature day [{0}] = ".format(str(j + 1))))
    for k in data:
        all_data = all_data + "," + str(k)
    final_string = str(i) + "," + name + "," + add + "," + str(how_many) + all_data + ","
    return final_string


def output_area(all_data):
    data = []
    for z in all_data:
        temp = ""
        header = []
        for i in z:

            if (i != ','):
                temp = temp + i
            else:
                header.append(temp)

                temp = ""
        data.append(header)
    for h in range(len(data)):
        show_data(data, h)


def show_data(data, h):
    day_num = 0
    print("\t\tDaily Temperature")
    print("-----------------------------------------------------------")
    print("Customer [" + str((int(data[h][0]) + 1)) + "] : " + data[h][1] + "               Address : " + data[h][2])
    for i in range(int(data[h][3])):
        day_num = day_num + int(data[h][4 + i])
        day_type, day_catg = typeofday(int(data[h][4 + i]))
        print("Temperature day [" + str(i + 1) + "] = " + data[h][4 + i] + " Celsius " + day_type + "    " + day_catg)

    print("The avarage Temp for " + data[h][3] + " days = " + str(int(day_num / int(data[h][3]))) + " Celsius")
    number_hot, number_pleasent, number_normal, number_cold, catgA, catgB, catgC, catgD = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(int(data[h][3])):
        if (int(data[h][4 + i]) > 50):
            number_hot = number_hot + 1
            catgA = catgA + 1
        elif (int(data[h][4 + i]) >= 40 and int(data[h][4 + i]) <= 50):
            number_pleasent = number_pleasent + 1
            catgB = catgB + 1
        elif (int(data[h][4 + i]) > 25 and int(data[h][4 + i]) <= 39):
            number_normal = number_normal + 1
            catgC = catgC + 1
        else:
            number_cold = number_cold + 1
            catgD = catgD + 1

    print("Number of Hot days = {0} day/s".format(str(number_hot)))
    print("Number of Pleseant days = {0} day/s".format(str(number_pleasent)))
    print("Number of Normal days = {0} day/s".format(str(number_normal)))
    print("Number of Cold days = {0} day/s".format(str(number_cold)))
    print("|  Days Category")
    print("Number of A Category days = {0} day/s".format(str(catgA)))
    print("Number of B Category days = {0} day/s".format(str(catgB)))
    print("Number of C Category days = {0} day/s".format(str(catgC)))
    print("Number of D Category days = {0} day/s".format(str(catgD)))


def typeofday(dataoftemp):
    if (dataoftemp > 50):
        return "Very Hot", "A"
    elif (dataoftemp >= 41 and dataoftemp <= 50):
        return "Plesant Day", "B"
    elif (dataoftemp >= 25 and dataoftemp <= 40):
        return "Normal Day", "C"
    elif (dataoftemp < 25):
        return "Very Cold", "D"


def main():
    input_area()


main()




