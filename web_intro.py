import requests


# r = requests.get("https://api.github.com/repos/bishoymhanna/bme547/branches")
# print(r)
# print(type(r))
# print(r.text)
# if r.status_code == 200:
#     answer = r.json()
#     print(type(answer))
#     for branch in answer:
#         print(branch["name"])
# else:
#     print("Bad request: {}".format(r.text))
#
#
# output_info = {"name": "Bishoy Hanna",
#                "net_id": "bmh61",
#                "e-mail": "bishoy.hanna@duke.edu"}
#
# r = requests.post("https://vcm-21170.vm.duke.edu:5000/student",
#                   json=output_info)
# print(r)
# print(r.text)
#
# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)
#
# msg = {"user": "bmh61", "message": "hello bmh61"}
# r = requests.post("https://vcm-21170.vm.duke.edu:5001/add_message",
#                   json=msg)
# r1 = requests.get("https://vcm-21170.vm.duke.edu:5001/get_messages/bmh61")
# print(r1.text)
