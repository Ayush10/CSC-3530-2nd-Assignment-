def main():
    inputarea()


def inputarea():
    print("\t\tTemperature Record System")
    print("\t\t Sunway Company Pvt. Ltd.")
    print("\t\t  Matitedevi,Kathmandu")
    numpeople = int(input("Enter how many customers wanted to record data :"))

    alldata = [None] * numpeople
    for i in range(numpeople):
        alldata[i] = storenum(i)
    outputarea(alldata)


def storenum(i):
    name = input("Enter the name of the " + str(i + 1) + " customer that wanted to record the temperature: ")
    add = input("Enter the address of " + str(i + 1) + " customer: ")
    howmuch = int(input("Enter how many days " + str(i + 1) + " customer wanted to record temperature?: "))
    print("Please enter " + str(howmuch) + " days’ temperature readings")
    data = [None] * howmuch
    alldata = ""
    for j in range(howmuch):
        data[j] = int(input("Temperature day [" + str(j + 1) + "] = "))
    for k in data:
        alldata = alldata + "," + str(k)
    finalstring = str(i) + "," + name + "," + add + "," + str(howmuch) + alldata + ","
    return finalstring


def outputarea(alldata):
    data = []
    for z in alldata:
        temp = ""
        heder = []
        for i in z:

            if (i != ','):
                temp = temp + i
            else:
                heder.append(temp)

                temp = ""
        data.append(heder)
    for h in range(len(data)):
        showdata(data, h)


def showdata(data, h):
    daynum = 0
    print("\t\tDaily Temperature")
    print("-----------------------------------------------------------")
    print("Customer [" + str((int(data[h][0]) + 1)) + "] : " + data[h][1] + "               Address : " + data[h][2])
    for i in range(int(data[h][3])):
        daynum = daynum + int(data[h][4 + i])
        daytype, daycat = typeofday(int(data[h][4 + i]))
        print("Temperature day [" + str(i + 1) + "] = " + data[h][4 + i] + " Celsius " + daytype + "    " + daycat)

    print("The avarage Temp for " + data[h][3] + " days = " + str(int(daynum / int(data[h][3]))) + " Celsius")
    numhot, numple, numnor, numcol, catA, catB, catC, catD = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(int(data[h][3])):
        if (int(data[h][4 + i]) > 50):
            numhot = numhot + 1
            catA = catA + 1
        elif (int(data[h][4 + i]) >= 41 and int(data[h][4 + i]) <= 50):
            numple = numple + 1
            catB = catB + 1
        elif (int(data[h][4 + i]) >= 25 and int(data[h][4 + i]) <= 40):
            numnor = numnor + 1
            catC = catC + 1
        elif (int(data[h][4 + 1]) < 25):
            numcol = numcol + 1
            catD = catD + 1

    print("Number of Hot days = " + str(numhot) + " day/s")
    print("Number of Plesant days = " + str(numple) + " day/s")
    print("Number of Normal days = " + str(numnor) + " day/s")
    print("Number of Cold days = " + str(numcol) + " day/s")
    print("|  Days Category")
    print("Number of A Category days = " + str(catA) + " day/s")
    print("Number of B Category days = " + str(catB) + " day/s")
    print("Number of C Category days = " + str(catC) + " day/s")
    print("Number of D Category days = " + str(catD) + " day/s")


def typeofday(dataoftemp):
    if (dataoftemp > 50):
        return "Very Hot", "A"
    elif (dataoftemp >= 41 and dataoftemp <= 50):
        return "Plesant Day", "B"
    elif (dataoftemp >= 25 and dataoftemp <= 40):
        return "Normal Day", "C"
    elif (dataoftemp < 25):
        return "Very Cold", "D"


main()