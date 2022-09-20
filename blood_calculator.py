#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 23:45:15 2022

@author: bishoyzaki
"""

def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Total Cholestrol")
    print("9 - Quit")
    keep_running = True
    while keep_running:  
        choice = input("Enter your choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_cholestrol_driver()
            
        
def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)

def output_HDL_result(hdl_value, charac):
    print("The result of an HDL value of {} is {}".format(hdl_value, charac))
   
def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)

def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value <= 159:
        return "Borderline High"
    elif 160 <= LDL_value <= 189:
        return "High"
    else:
        return "Very High"
    
def LDL_driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)
    
def output_LDL_result(ldl_value, charac):
    print("The result of an LDL value of {} is {}".format(ldl_value, charac))
    
def input_total_cholestrol():
    total_cholestrol_input = input("Enter the Total Cholestrol value:")
    return int(total_cholestrol_input)

def check_total_cholestrol(total_cholestrol_value):
    if total_cholestrol_value < 200:
        return "Normal"
    elif 200 <= total_cholestrol_value <=239:
        return "Borderline High"
    else:
        return "High"
    
def total_cholestrol_driver():
    total_cholestrol_value = input_total_cholestrol()
    answer = check_total_cholestrol(total_cholestrol_value)
    output_cholestrol_result(total_cholestrol_value, answer)
    
def output_cholestrol_result(total_cholestrol_value, charac):
    print("The result of a Total Cholestrol Value of {} is {}".format(total_cholestrol_value, charac))

if __name__ == "__main__":
    interface()
