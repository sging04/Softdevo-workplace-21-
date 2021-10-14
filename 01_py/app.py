#SUMMARY OF TRIO DISCUSSION
# With Ishraq:
# DISCOVERIES
# Alejandro, Ishraq, and Zhaoyu's group used a file reader to read files, and used "with" to call an object
# temporarily to return all the names, which are read in main() and chosen at random using random.choice(). # QUESTIONS
# COMMENTS
# Learned how to use random, how to import, learned how to use lists and dictionaries/hashmaps

#Sean Ging
#SoftDev
#K05: Better Living Through Amalgamation/selecting at random from a list/Python
#2021-10-14
import random
Roster = {
    'Period1': ['Sean','Deven', 'Theo'],
    'Period2': ['Pat','Peter','Paul']
}

def funct(
    num= random.randint(0,99)
    classList= []
    if num%2 != 1:              #if number generated is odd
        listlen= len(Roster['Period1'])
        classList= Roster['Period1']
    if num%2 != 0:
        listlen= len(Roster['Period2'])
        classList= Roster['Period2']
        
    rosternum= random.randint(0, listlen-1)
    retname= classList[rosternum]
    return retname

print(funct())
print(funct())
print(funct())
print(funct())
print(funct())
print(funct())
print(funct())
print(funct())
print(funct())
print(funct())
        

