import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/bmh61")
print(r.text)
donor_blood = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F2")
print(donor_blood.text)
recipient_blood = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M6")
print(recipient_blood.text)
print("B- cannot take blood from A- so not acceptable blood match")
match = {"Name": "bmh61", "Match": "No"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json=match)
print(r.text)