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

t1 = Thread(target=four)    #reassign threads to run scraper for next three sites
t2 = Thread(target=five)
t3 = Thread(target=six)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

t1 = Thread(target=seven)    #reassign threads to run scraper for next three sites
t2 = Thread(target=eight)
t3 = Thread(target=nine)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

t1 = Thread(target=ten)    #reassign threads to run scraper for next three sites
t2 = Thread(target=twelve)

t1.start()
t2.start()

t1.join()
t2.join()

