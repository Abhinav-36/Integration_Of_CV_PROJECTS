from tkinter import *
from cvprojects import background_blur, face_distance_measure
from handgestures import hand
import os
import text_to_speech as ts
from owner_face_detect import face_detector
window = Tk()
window.title("MY PROJECT")
window.configure(bg="#1D5D9B")  # Set background color

label = Label(window, text="OpenCV Projects", font=("Arial Bold", 30), fg="orange", bg="#1D5D9B", anchor="center")
label.pack(pady=20)  # Add padding between the label and buttons

# Create a scrollable canvas
canvas = Canvas(window, bg="#f2f2f2")
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create a scrollbar
scrollbar = Scrollbar(window, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas to work with the scrollbar
canvas.config(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


# Create a frame inside the canvas to hold the buttons
frame = Frame(canvas, bg="#f2f2f2")
canvas.create_window((0, 0), window=frame, anchor="nw")

# Function to create buttons with icons and description
def create_button(text, command, description, icon):
    button_frame = Frame(frame, bg="#f2f2f2")  # Frame for each button
    button_frame.pack(pady=10, anchor="w")
    
    button = Button(button_frame, text=text, command=command, font=("Arial Bold", 14), fg="white", bg="#ff8800", 
                    activebackground="#ffbb33", relief="flat", padx=20, pady=10)
    button.grid(row=0, column=0, sticky="w")
    
    icon_label = Label(button_frame, text=icon, font=("Arial", 20), bg="#f2f2f2")
    icon_label.grid(row=0, column=1, sticky="w")
    
    description_label = Label(button_frame, text=description, font=("Arial", 12), bg="#f2f2f2")
    description_label.grid(row=0, column=2, sticky="w", padx=10)


# Function to run background blur
def run1():
    ts.say("oh! you don't want to be spotted")
    background_blur()

# Function to run face distance measure
def run2():
    ts.say("You want to check how far you are... cool...")
    face_distance_measure()

def run4():
    ts.say("Now you can control Amazon services using Hand gestures")
    hand()
    
def run5():
    ts.say("Opening Face Lock Feature..")
    face_detector()
    
create_button("Face Blur Filter", run1, "Blur the face in the background", "😷")
create_button("Face Distance Measure", run2, "Measure the distance to your face", "📏")
create_button("Hand Gestures Control", run4, "Control Amazon services with hand gestures", "🖐️")
create_button("Face Unlock Feature", run5, "Detects the owner face and Unlocks", "😀")

window.geometry("800x600")  # Set initial window size

# Bind mouse scroll event to the canvas
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
canvas.bind_all("<MouseWheel>", on_mousewheel)

window.mainloop()