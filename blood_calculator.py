#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 23:45:15 2022

@author: bishoyzaki
"""

def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:  
        choice = input("Enter your choice: ")
        if choice =='9':
            return
        
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
    output_result(hdl_value, answer)

def output_result(hdl_value, charac):
    print("The result of an HDL value of {} if {}".format(hdl_value, charac))
   
interface()
