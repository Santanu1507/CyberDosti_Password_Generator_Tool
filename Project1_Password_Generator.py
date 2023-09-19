# Import necessary modules
import random
import string
import tkinter as tk
from tkinter import ttk

# Function to generate a random password
def generate_password(length):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate and display a password
def generate_and_display_password():
    # Get user inputs
    user_name = username_entry.get()
    password_length = int(password_length_entry.get())

    # Generate a random password of the specified length
    password = generate_password(password_length)
    
    # Display the generated password
    output_label.config(text=f"Password: {password}", foreground="black")

    # Configure the accept button to display username and password when clicked
    accept_button.config(command=lambda: show_output(user_name, password), state=tk.NORMAL)
    
    # Configure the reject button to generate a new password when clicked
    reject_button.config(command=generate_new_password, state=tk.NORMAL)

# Function to show the username and password
def show_output(user_name, password):
    # Display the username and password
    output_label.config(text=f"Username: {user_name}\nPassword: {password}", foreground="black")

    # Disable the accept and reject buttons after accepting the password
    accept_button.config(state=tk.DISABLED)
    reject_button.config(state=tk.DISABLED)

# Function to generate a new password
def generate_new_password():
    # Generate a new password when the user rejects the previous one
    password_length = int(password_length_entry.get())
    password = generate_password(password_length)
    
    # Display the new password
    output_label.config(text=f"New password: {password}", foreground="black")

    # Update the accept button command to use the new password
    accept_button.config(command=lambda: show_output(username_entry.get(), password))

    # Enable the accept and reject buttons for the new password
    accept_button.config(state=tk.NORMAL)
    reject_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Style for buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Frame for user input
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Username input
username_label = ttk.Label(input_frame, text="Enter User Name:", font=("Helvetica", 12))
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password length input
password_length_label = ttk.Label(input_frame, text="Password Length:", font=("Helvetica", 12))
password_length_label.grid(row=1, column=0, padx=10, pady=5)
password_length_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
password_length_entry.grid(row=1, column=1, padx=10, pady=5)

# Generate password button
generate_button = ttk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

# Output label
output_label = ttk.Label(root, text="", font=("Helvetica", 12), wraplength=300)
output_label.pack(pady=10)

# Accept and Reject buttons
button_frame = ttk.Frame(root)
button_frame.pack()

accept_button = ttk.Button(button_frame, text="Accept Password", state=tk.DISABLED, command=lambda: show_output("", ""))
reject_button = ttk.Button(button_frame, text="Reject Password", state=tk.DISABLED, command=generate_new_password)

accept_button.grid(row=0, column=0, padx=10, pady=5)
reject_button.grid(row=0, column=1, padx=10, pady=5)

# Start the Tkinter main loop
root.mainloop()
