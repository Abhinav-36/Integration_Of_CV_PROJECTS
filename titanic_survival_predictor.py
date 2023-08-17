import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib
def submit():
    age = age_var.get()
    gender = gender_var.get()
    passenger_class = class_var.get()
    male=0
    if gender=="male":
        male = 1
    else:
        male=0
    pclass1,pclass2,pclass3=0,0,0
    if passenger_class == "1":
        pclass1 = 1
        pclass2 = 0
        pclass3 = 0
    elif passenger_class == "2":
        pclass1 = 0
        pclass2 = 1
        pclass3 = 0
    else:
        pclass1 = 0
        pclass2 = 0
        pclass3 = 1
    sibsp = int()
    user_data = pd.DataFrame({
        'Age': [age],
        'Male': [male],
        '2' : [pclass2],
        '3' : [pclass3]
    })
    model = joblib.load("./Titnanic_Survival_Predictor.pkl")
    pred = model.predict(user_data)
    print(pred)
# Create the main window
def Titanic_Predictor():
    root = tk.Tk()
    root.title("Passenger Information")

    # Create and place labels and entry fields
    age_label = ttk.Label(root, text="Age:")
    age_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    age_var = tk.StringVar()
    age_entry = ttk.Entry(root, textvariable=age_var)
    age_entry.grid(row=0, column=1, padx=10, pady=5)

    gender_label = ttk.Label(root, text="Gender:")
    gender_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    gender_var = tk.StringVar()
    gender_entry = ttk.Entry(root, textvariable=gender_var)
    gender_entry.grid(row=1, column=1, padx=10, pady=5)

    class_label = ttk.Label(root, text="Passenger Class:")
    class_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    class_var = tk.StringVar()
    class_entry = ttk.Entry(root, textvariable=class_var)
    class_entry.grid(row=2, column=1, padx=10, pady=5)

    # Create and place the submit button
    submit_button = ttk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=5, columnspan=2, padx=10, pady=10)

    # Start the GUI event loop
    root.mainloop()
