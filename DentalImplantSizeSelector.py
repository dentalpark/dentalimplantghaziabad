"""
Dental Implant Size Selector

Copyright (C) 2024 Dr. Aakash Arora

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

Developer Information:
Dr. Aakash Arora
Oral & Maxillofacial Surgeon
Dental Park Ghaziabad
"""
import tkinter as tk
from tkinter import messagebox

# Sample data structure to hold implant sizes
implant_database = {
    "CompanyA": [(10, 3.5), (12, 4.0), (14, 4.5)],
    "CompanyB": [(8, 3.0), (10, 3.5), (12, 4.0)]
}

# Function to add new implant sizes
def add_implant():
    company = entry_company.get()
    length = float(entry_length.get())
    diameter = float(entry_diameter.get())
    
    if company in implant_database:
        implant_database[company].append((length, diameter))
    else:
        implant_database[company] = [(length, diameter)]
    
    messagebox.showinfo("Success", "Implant size added successfully!")

# Function to recommend implant size
def recommend_implant():
    bone_length = float(entry_bone_length.get())
    bone_width = float(entry_bone_width.get())
    company = entry_company_dentist.get()
    
    if company not in implant_database:
        messagebox.showerror("Error", "Company not found!")
        return
    
    suitable_implants = [
        (l, d) for l, d in implant_database[company]
        if l <= bone_length and d <= bone_width
    ]
    
    if suitable_implants:
        recommendation = f"Recommended sizes: {suitable_implants}"
    else:
        recommendation = "No suitable implants found."
    
    messagebox.showinfo("Recommendation", recommendation)

# Main window setup
root = tk.Tk()
root.title("Dental Implant Size Selector")

# Admin Section
frame_admin = tk.LabelFrame(root, text="Admin Section")
frame_admin.pack(padx=10, pady=10)

tk.Label(frame_admin, text="Company Name").grid(row=0, column=0)
entry_company = tk.Entry(frame_admin)
entry_company.grid(row=0, column=1)

tk.Label(frame_admin, text="Implant Length").grid(row=1, column=0)
entry_length = tk.Entry(frame_admin)
entry_length.grid(row=1, column=1)

tk.Label(frame_admin, text="Implant Diameter").grid(row=2, column=0)
entry_diameter = tk.Entry(frame_admin)
entry_diameter.grid(row=2, column=1)

tk.Button(frame_admin, text="Add Implant", command=add_implant).grid(row=3, columnspan=2)

# Dentist Section
frame_dentist = tk.LabelFrame(root, text="Dentist Section")
frame_dentist.pack(padx=10, pady=10)

tk.Label(frame_dentist, text="Bone Length").grid(row=0, column=0)
entry_bone_length = tk.Entry(frame_dentist)
entry_bone_length.grid(row=0, column=1)

tk.Label(frame_dentist, text="Bone Width").grid(row=1, column=0)
entry_bone_width = tk.Entry(frame_dentist)
entry_bone_width.grid(row=1, column=1)

tk.Label(frame_dentist, text="Company Name").grid(row=2, column=0)
entry_company_dentist = tk.Entry(frame_dentist)
entry_company_dentist.grid(row=2, column=1)

tk.Button(frame_dentist, text="Recommend Implant", command=recommend_implant).grid(row=3, columnspan=2)

root.mainloop()
