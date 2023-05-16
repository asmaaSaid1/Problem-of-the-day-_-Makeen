# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:49:52 2023

@author: Asma

"""

# program to print the frist non repeated number by using count
arr= [1,2,7,5,8,2,1]
for number in arr:
      if arr.count(number)==1:
              print(number)
              break
    
