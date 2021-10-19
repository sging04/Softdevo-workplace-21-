#Sean Ging
#SoftDev
#K06: StI/O: Divine your Destiny!
#2021-10-19
#Summary: I went through the csv reader, added jobs and percentages to two lists
#Then I used choices from random which uses a list of things to choose from as well as the likliness to choose each itm
#as it returns a list, you then return the first item from the list
import random
from csv import reader

def funct():
    collJobs= []
    collPerc= []
    with open('occupations.csv', 'r') as f:
        csv_reader= reader(f)
        for row in csv_reader:
            JobClass= row[0]
            JobPercentage= row[1]
            if not(JobClass== "Job Class" or JobClass== "Total"):
                collJobs += [JobClass]
                collPerc += [float(JobPercentage)]
    return random.choices(collJobs, collPerc)[0]

for i in range(1,40):
    print(funct())
