#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:29:30 2022

@author: bishoyzaki
"""


class Patient:

    def __init__(self, first_name, last_name, patient_id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.patient_id = patient_id
        self.age = age
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name,
                         patient_last_name,
                         patient_id,
                         patient_age):
    new_patient = Patient(patient_first_name, patient_last_name,
                          patient_id, patient_age)
    return new_patient


def main():
    x = Patient("David", "Ward", "", "")
    print(x.full_name())
    y = Patient("Edward", "Smith", "", "")
    print(y.last_name)
    # db = {}
    # db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    # db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    # db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    # print_database(db)
    # add_test_result(db, 3, "HDL", 100)
    # print_database(db)
    # print("Patient {} is a {}".format(get_full_name(db[2]),
    #                                  adult_or_minor(db[2])))
    # print(find_patient(db, 3))
    # room_list = ["Room 1", "Room 2", "Room 3"]
    # for i, patient in enumerate(db):
    #     print("Name = {}, Room = {}".format(patient[0], room_list[i]))
    # for patient, room in zip(db, room_list):
    #     print("Name = {}, Room = {}".format(patient[0], room))


def print_database(db):
    for patient in db:
        print(patient)
        print("Name: {}, ID: {}, Age: {}".format(get_full_name(db[patient]),
                                                 db[patient]["Id"],
                                                 db[patient]["Age"]))


def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name


def find_patient(db, id_number):
    patient = db[id_number]
    return patient


def add_test_result(db, id_number, test_name, test_value):
    patient = find_patient(db, id_number)
    patient["Tests"].append((test_name, test_value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


if __name__ == "__main__":
    main()
