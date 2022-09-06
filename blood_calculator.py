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
   
interface()
