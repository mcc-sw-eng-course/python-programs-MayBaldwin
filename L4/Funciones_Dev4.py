# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:23:36 2019

@author: mlbaldwi
"""

def st_dev(lst):
    x1=mean(lst)
    suma=0
    n=len(lst)
    for i in range (0, n,1):
        x=lst[i]
        suma=(x-x1)**2+suma
    result=(suma/(n-1))**(1/2)
    return(result)

def mean(lst):
    m=sum(lst) / float(len(lst))
    return(m) 
    
def convert_to_roman(number):
    if type(number) == int:
        if number > 0 and number <= 3999:
            aux = number
            count = 0
            res = ''

            # 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
            rom = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
            num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

            while aux > 0:
                while aux >= num[count]:
                    aux -= num[count]
                    res += rom[count]
                if count < 13:
                    count += 1

            return res

        else:
            raise ValueError("Use only numbers between 1 and 3999")
    else:
        raise TypeError("Use only whole numbers")

class myPowerList():
    
    def __init__(self):
        self.lst=[]
                    
    def readFromTextFile(self,filename):
        if type(filename) == str:
            file = open(filename, "r")
            return(file.read())
            
        else:
            raise TypeError

def filenameExists(filename):
    try:
        file = open(filename, "r")
        file.close()
        return(True)
    except IOError: 
        return(False)
        
class directory():
    
    def __init__(self):
        self.users_data=[]
        
    def newRecord(self, name, address, phone, email):
        self.name= name
        self.address= address
        self.phone= str(phone)
        self.email= email
        self.users_data.append([name,address,phone,email])
        return(self.users_data)
    
    def saveAll(self, filename):
        if(filenameExists(filename)):
            return("File name already exists, please give another file name")
        else:
            file = open(filename, "w")
            file.write(str(self.users_data)) 
            file.close()
            return("Saved")
            
    def loadFile(self,filename):
        if(filenameExists(filename)):
            file = open(filename, "r")
            return(file.read())
        else:
            return("File Not Found")
            
    def record_search(self,name):
        for record in range (0, len(self.users_data),1):
            if(name in self.users_data[record]):
                return(self.users_data[record])
        return("This name is not in the directory")