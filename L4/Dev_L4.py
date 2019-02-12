# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 08:58:18 2019

@author: mlbaldwi
"""
import unittest
from Funciones_Dev4 import *

def rFile(filename):
    aList = myPowerList()
    return(aList.readFromTextFile(filename))

class TestUM(unittest.TestCase):
   
    def setUp(self):
        self.directorio = directory()
        self.directorio.newRecord("Eric", "Avenida siempre viva", 123124, "eric@itesm.com")
        self.directorio.newRecord("Panchita", "Avenida Mariano Otero", 6798765, "panchita@itesm.com")
        pass
    
    #Standard Deviation function
    def test_stdev_entry_is_a_string(self):
         with self.assertRaises(TypeError):
            st_dev('string')
            
    def test_stdev_entry_is_an_array(self):
        with self.assertRaises(TypeError):
            st_dev([[1,2,3],[3,4,5]])
    
    def test_stdev_entry_is_a_Bool(self):
        with self.assertRaises(TypeError):
            st_dev(True)
    
    def test_stdev_entry_is_a_number(self):
        with self.assertRaises(TypeError):
            st_dev(1)
            
    def test_stdev_entrylist_is_a_string(self):
        with self.assertRaises(TypeError):
            st_dev(["hola", "mundo"])
            
    def test_stdev_giant_number(self):
        with self.assertRaises(OverflowError):
            st_dev([1,2,3,7,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999])

    def test_stdev_division_by_zero(self):
        lst = []
        with self.assertRaises(ZeroDivisionError):
             st_dev(lst)
    
    def test_stdev_negative_int(self):
        lst = [-10,-2,38,23,-38,23,21]
        stDev_val = round(st_dev(lst), 4)
        self.assertEqual(stDev_val, 26.0092)
        
    def test_stdev_negative_float(self):
        lst = [-10.35,-2.1,38.5,23,-38,23.16,21]
        stDev_val = round(st_dev(lst), 4)
        self.assertEqual(stDev_val, 26.1684)
        
    def test_stdev_positive_float(self):
        lst = [10.35,2.1,38.5,23,38,23.16,21]
        stDev_val = round(st_dev(lst), 4)
        self.assertEqual(stDev_val, 13.3085)
    
    def test_stdev_positive_int(self):
        lst = [10,35,2,1,38,5,23,38,23,16,21]
        stDev_val = round(st_dev(lst), 4)
        self.assertEqual(stDev_val, 13.8282)
        
    def test_stdev_entry_is_None(self):
         with self.assertRaises(TypeError):
            st_dev(None)

#    #Conversión a números romanos
#    def test_decimalToRoman_entry_list(self):
#        with self.assertRaises(TypeError):
#            decimalToRoman([1,2,3])
#    
#    def test_decimalToRoman_entry_string(self):
#        with self.assertRaises(TypeError):
#            decimalToRoman("hello")
            
#    def test_decimalToRoman_entry_float(self):
#        with self.assertRaises(ValueError):
#            decimalToRoman(1.1)
            
    #readFromTextFile(filename)
   

    def test_RFile_entry_is_a_int(self):
        with self.assertRaises(TypeError):
            rFile(123)
        
    def test_RFile_entry_is_a_bool(self):
        with self.assertRaises(TypeError):
            rFile(True)
    
    def test_RFile_entry_is_a_float(self):
        with self.assertRaises(TypeError):
            rFile(12.3)
    
    def test_RFile_entry_is_empty(self):
        with self.assertRaises(TypeError):
            rFile()
    
    def test_RFile_file_doesnt_exist(self):
         with self.assertRaises(FileNotFoundError):
             rFile("test2.txt")
            
    def test_RFile_empty_file(self):
        f1 = open("test.txt", "w+")
        f1.close()
        self.assertEqual(rFile("test.txt"),"")
    
    def test_RFile_read_a_string(self):
        f1 = open("test1.txt", "w+")
        f1.write("Hello World")
        f1.close()
        self.assertEqual(rFile("test1.txt"),"Hello World")
            
        #Directory
    
    def test_Directory_add_member(self):        
        direct = directory()
        direct.newRecord("Eric", "Avenida siempre viva", 123124, "eric@itesm.com")
        direct.newRecord("Panchita", "Avenida Mariano Otero", 6798765, "panchita@itesm.com")
        self.assertEqual(direct.record_search("Panchita"), ["Panchita", "Avenida Mariano Otero", 6798765, "panchita@itesm.com"]) 

    def test_Directory_add_member_missing_arg(self):        
        direct = directory()
        with self.assertRaises(TypeError):
            direct.newRecord("Avenida siempre viva", 123124, "eric@itesm.com")
            
    def test_Directory_user_not_found(self):
        self.assertEqual(self.directorio.record_search("Panchita1"), "This name is not in the directory")
        
    def test_Directory_save_to_file(self):
        direct = directory()
        direct.newRecord("Eric", "Avenida siempre viva", 123124, "eric@itesm.com")
        
        filename = "file1.txt"
        direct.saveAll(filename)
        
        file = open(filename, "r")
        record = file.readline()
        file.close()
        
        self.assertEqual(record, "[['Eric', 'Avenida siempre viva', 123124, 'eric@itesm.com']]")
           
    def test_Directory_save_load_file(self):
        direct = directory()
        direct.newRecord("Eric", "Avenida siempre viva", 123124, "eric@itesm.com")
        
        filename = "file2.txt"
        direct.saveAll(filename)
        loadData = direct.loadFile(filename)
        
        self.assertEqual(loadData, "[['Eric', 'Avenida siempre viva', 123124, 'eric@itesm.com']]")
        
    def test_Directory_load_file_not_found(self):
        self.assertEqual(self.directorio.loadFile("notfound.txt"), "File Not Found")
        
    def test_Directory_save_file_found(self):
        self.directorio.saveAll("found.txt")
        
        self.assertEqual(self.directorio.saveAll("found.txt"), "File name already exists, please give another file name")
        
    def test_convert_to_roman_int(self):
        self.assertEqual(convert_to_roman(4), "IV")
        
    def test_convert_to_roman_float(self):
        self.assertRaises(TypeError, convert_to_roman, 5.5)
        
    def test_convert_to_roman_negative_number(self):
        self.assertRaises(ValueError, convert_to_roman, -1)
        
    def test_convert_to_roman_big_number(self):
        self.assertRaises(ValueError, convert_to_roman, 5000)
        
    def test_convert_to_roman_string(self):
        self.assertRaises(TypeError, convert_to_roman, "string")
        
if __name__ == '__main__':
    unittest.main()            