import openpyxl
import matplotlib.pyplot as plt
import sys
import pandas as pd
file = 'F1 Fantasy.xlsx'
data = pd.ExcelFile(file)
ps = openpyxl.load_workbook(file, data_only=True)
sheet = ps['Blad1']

# Python Script to plot a points graph for the F1 Championship and a F1 Fantasy League
# Code is very ugly since I see no point in spending the time to clean a hobby project that works :)

## Driver class ##
class Driver :
    def __init__(self, name):
        self.name = name        ## Name of Driver
        self.y = [0]            ## List of total points after each race

class Hallonbåt :
    def __init__(self, name):
        self.name = name        ## Team name Hallonbåt
        self.y = [0]            ## List of total points after each race

# Global Variables  
# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
Drivers = []
Hallonbåtar = []
RacesSheet = 'CD'#EFGHIJKLMNOPQRSTUVWXYZ'
Races = ["Australia","China","Japan","Bahrain","Saudi","Miami","Imola","Monaco","Spain","Canada","Austria","Britain","Belgium","Hungary","Netherlands","Italy","Azerbaijan","Singapore","Austin","Mexico","Brazil","Las Vegas","Qatar","Abu Dhabi"]

## Build a List for all Drivers and one for all HallonbåtGP teams ##
def arrayBuild() :
    for row in range(54,74):
        Drivers.append(Driver(sheet['A' + str(row)].value))

    for row in range(1, 52) :
        Hallonbåtar.append(Hallonbåt(sheet['B' + str(row)].value))

## Append per race points to list for all drivers for WDC plot ##
def driverPoints() :
    driverRow = int
    for Driver in Drivers :
        tempPoint = 0
        for row in range(54,74) :
            if(Driver.name == sheet['A' + str(row)].value) :
                driverRow = row
        for col in RacesSheet :
            if sheet[col + str(driverRow)].value is not None :
                # print(sheet[col + str(driverRow)].value)
                y = sheet[col + str(driverRow)].value
                tempPoint += y
                Driver.y.append(tempPoint)

## Append per race points to list for all Hallonbåt Teams ##
def hallonbåtPoints() :
    hallonbåtRow = int
    for Hallonbåt in Hallonbåtar :
        tempPoint = 0
        for row in range(89,505) :
            if(Hallonbåt.name == sheet['A' + str(row)].value) :
                hallonbåtRow = row
        for col in RacesSheet :
            if sheet[col + str(hallonbåtRow)].value is not None :
                y = sheet[col + str(hallonbåtRow)].value
                tempPoint += y
                Hallonbåt.y.append(tempPoint)
        # print(Hallonbåt.name)
        # print(Hallonbåt.y)
## Setup Graph ##
def graphSettings() :
    plt.figure(figsize=(20,12))
    # plt.ylim(0, (Hallonbåtar[0].y[-1]+5))
    plt.xlim(0,len(RacesSheet))
    plt.minorticks_off()
    plt.grid(visible=True, which='both', axis='both')

## Print Graph ##
def graphPrint() :
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.subplots_adjust(right=0.875)
    plt.subplots_adjust(left=0.050)
    plt.subplots_adjust(bottom=0.050)
    plt.subplots_adjust(top=0.975)
    plt.show()


## Plot graph
def plotFunc() :
    graphSettings()
    tempP = 0
    colors = 0
    x = [0]

    for i in range(len(RacesSheet)) :
        x.append(Races[i])

    if (sys.argv[1]) == "WDC" :
        plt.ylim(0, (Drivers[0].y[-1]+5))
        for Driver in Drivers :
            if tempP != Driver.y :
                tempP = Driver.y
                colors += 1
            plt.plot(x, Driver.y, label = Driver.name, color=('C' + str(colors)))
    elif (sys.argv[1]) == "Hallon" :
        plt.ylim(0, (Hallonbåtar[0].y[-1]+5))
        for Hallonbåt in Hallonbåtar :
            if tempP != Hallonbåt.y :
                tempP = Hallonbåt.y
                colors += 1
            plt.plot(x, Hallonbåt.y, label = Hallonbåt.name, color=('C' + str(colors)))
    else :
        print("Use argument WDC or Hallon")
        sys.exit()

    plt.title(sys.argv[1])
    plt.xlabel('Races')
    plt.ylabel('Points')
    graphPrint()


## NO MAIN FUNC IN MY CODE :) ##
if (len(sys.argv)) == 1 :
        print("Use argument WDC or Hallon")
        sys.exit()
arrayBuild()
driverPoints()
hallonbåtPoints()
if (len(sys.argv)) == 2 :
    plotFunc()