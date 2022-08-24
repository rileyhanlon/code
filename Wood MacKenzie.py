class windfarm():
    def __init__(self, location, type, status, output, cost):
        self.location = location
        self.type = type
        self.status = status
        self.output = int(output)
        self.cost = int(cost)


def read():
    windfarms = []
    input_file = open("WindFarmData.txt", "r")
    reader_object = csv.reader(input_file)
    for line in reader_object:
        windfarms.append(windfarm(line[0], line[1], line[2], line[3], line[4]))

    input_file.close()

    print("Is there an increase in energy generating cost?")
    answer = input()
    while answer != "Yes" and answer != "No":
        print("Please enter 'Yes' or 'No' only.")
        answer = input()
    if answer == "Yes":
        print("What is the percentage increase? (As an integer only)")
        increase = (int(input()) / 100)
        print("Should this apply to any one type of wind farms?")
        itype = input()
        while itype != "Onshore" and itype != "Offshore" and itype != "No":
            print("Please enter either 'Onshore' or 'Offshore' or 'No' only.")
            itype = input()

        if itype != "No":
            if itype == "Onshore":
                for i in range(len(windfarms)):
                    if windfarms[i].type == itype:
                        windfarms[i].cost = windfarms[i].cost + (increase * windfarms[i].cost)

            if itype == "Offshore":
                for i in range(len(windfarms)):
                    if windfarms[i].type == itype:
                        windfarms[i].cost = windfarms[i].cost + (increase * windfarms[i].cost)

        elif itype == "No":
            for i in range(len(windfarms)):
                windfarms[i].cost = windfarms[i].cost + (increase * windfarms[i].cost)

    return windfarms


def preferences(mywindfarms):
    num_answer = ""
    type_answer = ""
    status_answer = ""
    output_answer = 0
    cost_answer = 0
    min = 0
    ptype_answer = ""
    pstatus_answer = ""
    poutput_answer = 0

    print("Do you want 'One' or a 'Portfolio' of wind farms?")
    num_answer = input()
    while num_answer != "One" and num_answer != "Portfolio":
        print("Please enter either 'One' or 'Portfolio' only.")
        num_answer = input()

    if num_answer == "One":

        print("Do you have a preference of 'Onshore' or 'Offshore' wind farms or not?")
        type_answer = input()
        while type_answer != "Onshore" and type_answer != "Offshore" and type_answer != "No":
            print("Please enter either 'Onshore' or 'Offshore' or 'No' only.")
            type_answer = input()

        print("Do you have a preference if the wind farm is in 'Production' or 'Planned' or not?")
        status_answer = input()
        while status_answer != "Production" and status_answer != "Planned" and status_answer != "No":
            print("Please enter either 'Production' or 'Planned' or 'No' only.")
            status_answer = input()

        print("Please enter the minimum output you want from a wind farm (As an integer only)")
        output_answer = int(input())
        while output_answer > 515:
            print("Sorry there is no singular wind farm that can produce this output please enter a different value or restart and choose a portfolio.")
            output_answer = int(input())

        print("Do you want to only see the results with the lowest hourly operating costs? Please enter 'Yes' or 'No'.")
        cost_answer = input()

    if num_answer == "Portfolio":

        print("Do you have a preference of 'Onshore' or 'Offshore' wind farms or not?")
        ptype_answer = input()
        while ptype_answer != "Onshore" and ptype_answer != "Offshore" and ptype_answer != "No":
            print("Please enter either 'Onshore' or 'Offshore' or 'No' only.")
            ptype_answer = input()

        print("Do you have a preference if the wind farm is in 'Production' or 'Planned' or not?")
        pstatus_answer = input()
        while pstatus_answer != "Production" and pstatus_answer != "Planned" and pstatus_answer != "No":
            print("Please enter either 'Production' or 'Planned' or 'No' only.")
            pstatus_answer = input()

        print("Please enter the minimum energy output you want your portfolio of windfarms to total. (As an integer only)")
        poutput_answer = int(input())

    return num_answer, type_answer, status_answer, output_answer, cost_answer, min, ptype_answer, pstatus_answer, poutput_answer


def search_preferences(mywindfarms, mynum_answer, mytype_answer, mystatus_answer, myoutput_answer, mycost_answer,myptype_answer, mypstatus_answer, mypoutput_answer):

    min = 0
    results = []
    if mynum_answer == "One":
        print("")
        print("Below is the most suitable wind farm(s) for your preferences:")
        print("")
        print("Location".ljust(12), "Type".ljust(12), "Status".center(12), "Ouput(mw/h)".rjust(12),
              "Cost(per mw)".rjust(12))
        print("")

        if mycost_answer == "Yes" and mytype_answer != "No" and mystatus_answer != "No":
            for i in range(12):
                if mywindfarms[i].type == mytype_answer and mywindfarms[i].status == mystatus_answer and mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status,mywindfarms[i].output, mywindfarms[i].cost))
            min = results[0].cost
            for i in range(len(results)):
                if results[i].cost < min:
                    min = results[i].cost
            for i in range(len(results)):
                if results[i].cost == min:
                    print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))


        elif mycost_answer == "No" and mytype_answer != "No" and mystatus_answer != "No":
            for i in range(12):
                if mywindfarms[i].type == mytype_answer and mywindfarms[i].status == mystatus_answer and mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status,mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))

        elif mycost_answer == "Yes" and mytype_answer == "No" and mystatus_answer != "No":
            for i in range(12):
                if mywindfarms[i].status == mystatus_answer and mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            min = results[0].cost
            for i in range(len(results)):
                if results[i].cost < min:
                    min = results[i].cost
            for i in range(len(results)):
                if results[i].cost == min:
                    print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))

        elif mycost_answer == "No" and mytype_answer == "No" and mystatus_answer != "No":
            for i in range(12):
                if mywindfarms[i].status == mystatus_answer and mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))

        elif mycost_answer == "Yes" and mytype_answer != "No" and mystatus_answer == "No":
            for i in range(12):
                if mywindfarms[i].type == mytype_answer and mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            min = results[0].cost
            for i in range(len(results)):
                if results[i].cost < min:
                    min = results[i].cost
            for i in range(len(results)):
                if results[i].cost == min:
                    print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))

        elif mycost_answer == "No" and mytype_answer != "No" and mystatus_answer == "No":
            for i in range(12):
                if mywindfarms[i].type == mytype_answer and mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))

        elif mycost_answer == "No" and mytype_answer == "No" and mystatus_answer == "No":
            for i in range(12):
                if mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))

        elif mycost_answer == "Yes" and mytype_answer == "No" and mystatus_answer == "No":
            for i in range(12):
                if mywindfarms[i].output > myoutput_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            min = results[0].cost
            for i in range(len(results)):
                if results[i].cost < min:
                    min = results[i].cost
            for i in range(len(results)):
                if results[i].cost == min:
                    print((results[i].location).ljust(12), (results[i].type).ljust(12), (results[i].status).center(12), (str(results[i].output)).rjust(12), (str(results[i].cost)).rjust(12))

    if mynum_answer == "Portfolio":

        ptotal = 0
        portfolio = []
        reached = False

        if myptype_answer != "No" and mypstatus_answer != "No":
            for i in range(12):
                if mywindfarms[i].type == myptype_answer and mywindfarms[i].status == mypstatus_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                if ptotal < mypoutput_answer and reached != True:
                    ptotal = ptotal + results[i].output
                    portfolio.append(windfarm(results[i].location, results[i].type, results[i].status, results[i].output, results[i].cost))
                if ptotal > mypoutput_answer:
                    reached = True

        if myptype_answer == "No" and mypstatus_answer != "No":
            for i in range(12):
                if mywindfarms[i].status == mypstatus_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                if ptotal < mypoutput_answer and reached != True:
                    ptotal = ptotal + results[i].output
                    portfolio.append(windfarm(results[i].location, results[i].type, results[i].status, results[i].output,results[i].cost))
                if ptotal > mypoutput_answer:
                    reached = True

        if myptype_answer != "No" and mypstatus_answer == "No":
            for i in range(12):
                if mywindfarms[i].type == myptype_answer:
                    results.append(windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                if ptotal < mypoutput_answer and reached != True:
                    ptotal = ptotal + results[i].output
                    portfolio.append(windfarm(results[i].location, results[i].type, results[i].status, results[i].output, results[i].cost))
                if ptotal > mypoutput_answer:
                    reached = True

        if myptype_answer == "No" and mypstatus_answer == "No":
            for i in range(12):
                results.append(
                    windfarm(mywindfarms[i].location, mywindfarms[i].type, mywindfarms[i].status, mywindfarms[i].output, mywindfarms[i].cost))
            for i in range(len(results)):
                if ptotal < mypoutput_answer and reached != True:
                    ptotal = ptotal + results[i].output
                    portfolio.append(windfarm(results[i].location, results[i].type, results[i].status, results[i].output, results[i].cost))
                if ptotal > mypoutput_answer:
                    reached = True

        print("")
        print("Below are the most suitable Wind Farms to make up your portfolio:")
        print("")
        print("Location".ljust(12), "Type".ljust(12), "Status".center(12), "Ouput(mw/h)".rjust(12),
              "Cost(per mw)".rjust(12))
        print("")
        for i in range(len(portfolio)):
            print((portfolio[i].location).ljust(12), (portfolio[i].type).ljust(12), (portfolio[i].status).center(12),
                  (str(portfolio[i].output)).rjust(12), (str(portfolio[i].cost)).rjust(12))


# Main Program

import csv

mywindfarms = read()
mynum_answer, mytype_answer, mystatus_answer, myoutput_answer, mycost_answer, mymin, myptype_answer, mypstatus_answer, mypoutput_answer = preferences(mywindfarms)
search_preferences(mywindfarms, mynum_answer, mytype_answer, mystatus_answer, myoutput_answer, mycost_answer,myptype_answer, mypstatus_answer, mypoutput_answer)



