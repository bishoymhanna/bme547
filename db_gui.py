import tkinter as tk
from tkinter import ttk


def main_window():

    def ok_cmd():
        print("Patient name: {}".format(patient_name_entry.get()))
        print("Patient ID: {}".format(patient_id_entry.get()))
        print("Blood type: {}{}".format(blood_letter_selection.get(),
                                        rh_button.get()))
        print("Donation Center: {}".format(donor_center.get()))
        print("Clicked Ok button")

    def cancel_cmd():
        root.destroy()

    root = tk.Tk()
    root.title("Blood Donor Database")
    root.geometry("800x200")

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2,
                                                      sticky="w")

    patient_name_entry = tk.StringVar()
    ttk.Label(root, text="Name:").grid(column=0, row=1)
    ttk.Entry(root, width=50, textvariable=patient_name_entry).grid(column=1,
                                                                    row=1)

    patient_id_entry = tk.StringVar()
    ttk.Label(root, text="ID:").grid(column=0, row=2, sticky="e")
    ttk.Entry(root, textvariable=patient_id_entry).grid(column=1, row=2,
                                                        sticky="w")

    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter_selection,
                    value="A").grid(column=0, row=3, sticky="w")
    ttk.Radiobutton(root, text="B", variable=blood_letter_selection,
                    value="B").grid(column=0, row=4, sticky="w")
    ttk.Radiobutton(root, text="AB", variable=blood_letter_selection,
                    value="AB").grid(column=0, row=5, sticky="w")
    ttk.Radiobutton(root, text="O", variable=blood_letter_selection,
                    value="O").grid(column=0, row=6, sticky="w")

    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text="Rh Positive",
                    variable=rh_button,
                    onvalue="+",
                    offvalue="-").grid(column=1, row=4)

    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo["values"] = ["Durham", "Cary", "Raleigh"]
    donor_center_combo.state(["readonly"])

    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=6)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=6)

    root.mainloop()


if __name__ == '__main__':
    main_window()
