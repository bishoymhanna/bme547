#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:29:30 2022

@author: bishoyzaki
"""


def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient


def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    add_test_result(db, 3, "HDL", 100)
    print(find_patient(db, 3))
    room_list = ["Room 1", "Room 2", "Room 3"]
    for i, patient in enumerate(db):
        print("Name = {}, Room = {}".format(patient[0], room_list[i]))
    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient[0], room))


def print_database(db):
    for patient in db:
        print("Name: {}, ID: {}, Age: {}"
              .format(patient[0], patient[1], patient[2]))


def find_patient(db, id_number):
    for patient in db:
        if patient[1] == id_number:
            return patient
    return False


def add_test_result(db, id_number, test_name, test_value):
    patient = find_patient(db, id_number)
    patient[3].append((test_name, test_value))


if __name__ == "__main__":
    main()
