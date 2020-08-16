from threading import Thread

#Run all scripts concurrently to save time.

def one(): import AmericanApparel
def two(): import AmericanEagle
def three(): import Bershka 
def four(): import Forever21
def five(): import Gap
def six(): import HM
def seven(): import JCPenny
def eight(): import OldNavy
def nine(): import Reformation
def ten(): import uniqulo
# def eleven(): import UrbanOutfitters
def twelve(): import Zara

t1 = Thread(target=one)
t2 = Thread(target=two)
t3 = Thread(target=three)   #run scraper for fisrt three sites

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

t4 = Thread(target=four)    #reassign threads to run scraper for next three sites
t5 = Thread(target=five)
t3 = Thread(target=six)

t4.start()
t5.start()
t6.start()

t4.join()
t5.join()
t6.join()

t7 = Thread(target=seven)    #reassign threads to run scraper for next three sites
t8 = Thread(target=eight)
t9 = Thread(target=nine)

t7.start()
t8.start()
t9.start()

t7.join()
t8.join()
t9.join()

t10 = Thread(target=ten)    #reassign threads to run scraper for next three sites
t12 = Thread(target=twelve)

t10.start()
t12.start()

t10.join()
t12.join()


# Thread(target=four).start()
# Thread(target=five).start()
# Thread(target=six).start()
# Thread(target=seven).start()
# Thread(target=eight).start()
# Thread(target=nine).start()
# Thread(target=ten).start()
# # Thread(target=eleven).start()
# Thread(target=twelve).start()

