# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:07:47 2020

@author: falconfoe
"""
import csv
import re





def main():
    dogfile = open('dog_tags.csv', newline='')
    reader = csv.DictReader(dogfile)
    
    '''find any name begins with ::  s  '''
    # exp = re.compile(r's.*', re.IGNORECASE)
    
    '''find any name contains ::  bi  '''
    # exp = re.compile(r'.*bi.*', re.IGNORECASE)
    
    '''find any name contains ::  space  '''
    # exp = re.compile(r'.*\s.*', re.IGNORECASE)
    
    '''find any name contains ::  non-alpha + "aka" + space  '''
    # exp = re.compile(r'.*\Waka\s.*', re.IGNORECASE)
    
    '''find any name contains ::  Z then Y with any letters inbetween  '''
    # exp = re.compile(r'(Z\w*).*(Y\w*)', re.IGNORECASE)
    
    '''find any name contains ::  a + space + c  '''
    # exp = re.compile(r'.*a.*\s.*c.*', re.IGNORECASE)
    
    '''starts and ends with same letter'''
    # exp = re.compile(r'([a-z]).*\1$', re.IGNORECASE)
    
    '''names with more than 24 characters'''
    exp = re.compile(r'[\w\s]{25,}', re.IGNORECASE)
    
    
    
    
    count = 0
    for row in reader:
        m = exp.match(row['DogName'])
        if m:
            # print(m)
            print(m.group())
            count += 1
    print(count)

if __name__ == "__main__":
    main()