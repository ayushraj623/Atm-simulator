import tkinter as tk

# ==========================================
# 1. ATM STATE (Data)
# ==========================================
# These variables store the memory of the ATM
balance = 100000
record = []

# ==========================================
# 2. LOGIC FUNCTIONS
# ==========================================

def update_screen(message, color="black"):
    """Helper function to update the text on the ATM screen."""
    screen_label.config(text=message, fg=color)

def check_balance():
    update_screen(f"Your current balance is:\n₹{balance}", "blue")

def deposit():
    # We must use 'global' so Python knows we want to change the main balance variable
    global balance 
    try:
        amount = int(amount_entry.get())
        if amount > 0:
            balance += amount
            record.append(f"Deposited: +₹{amount}")
            update_screen(f"Success! Deposited ₹{amount}.\nNew Balance: ₹{balance}", "green")
            amount_entry.delete(0, tk.END) # Clears the typing box
        else:
            update_screen("Please enter a positive number.", "red")
    except ValueError:
        update_screen("Invalid! Please type numbers only.", "red")

def withdraw():
    global balance
    try:
        amount = int(amount_entry.get())
        if amount > 0:
            if amount <= balance:
                balance -= amount
                record.append(f"Withdrew: -₹{amount}")
                update_screen(f"Success! Withdrew ₹{amount}.\nNew Balance: ₹{balance}", "green")
                amount_entry.delete(0, tk.END)
            else:
                update_screen("Insufficient balance!", "red")
        else:
            update_screen("Please enter a positive number.", "red")
    except ValueError:
        update_screen("Invalid! Please type numbers only.", "red")

def view_statement():
    if not record:
        update_screen("No transactions yet.", "blue")
    else:
        # Join the list into a single string with line breaks
        statement = "\n".join(record)
        update_screen(f"--- Transaction History ---\n{statement}", "blue")


# ==========================================
# 3. FRONTEND WINDOW SETUP (Tkinter)
# ==========================================

# Create the main window
root = tk.Tk()
root.title("Python ATM Simulator")
root.geometry("400x500")
root.config(bg="#2c3e50") # Dark blue-gray background

# Title
title = tk.Label(root, text="🏦 AYUSH BANK ATM", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white")
title.pack(pady=20)

# The ATM "Screen" (Where messages appear)
screen_frame = tk.Frame(root, bg="#ecf0f1", bd=5, relief="sunken")
screen_frame.pack(pady=10, padx=20, fill="x")

screen_label = tk.Label(screen_frame, text="Welcome to the ATM.\nPlease select an option.", font=("Courier", 12), bg="#ecf0f1", height=5)
screen_label.pack(pady=10)

# Amount Input Area
input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Amount: ₹", font=("Helvetica", 14), bg="#2c3e50", fg="white").grid(row=0, column=0)
amount_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=15)
amount_entry.grid(row=0, column=1)

# Buttons Frame (To arrange them nicely)
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)

# Button styles
btn_style = {"font": ("Helvetica", 12, "bold"), "width": 15, "bg": "#3498db", "fg": "white", "pady": 5}

# Create and place the buttons in a grid
btn_balance = tk.Button(button_frame, text="Check Balance", command=check_balance, **btn_style)
btn_balance.grid(row=0, column=0, padx=10, pady=10)

btn_statement = tk.Button(button_frame, text="View Statement", command=view_statement, **btn_style)
btn_statement.grid(row=0, column=1, padx=10, pady=10)

btn_deposit = tk.Button(button_frame, text="Deposit", command=deposit, bg="#2ecc71", fg="white", font=("Helvetica", 12, "bold"), width=15, pady=5)
btn_deposit.grid(row=1, column=0, padx=10, pady=10)

btn_withdraw = tk.Button(button_frame, text="Withdraw", command=withdraw, bg="#e74c3c", fg="white", font=("Helvetica", 12, "bold"), width=15, pady=5)
btn_withdraw.grid(row=1, column=1, padx=10, pady=10)

# Start the application loop
root.mainloop()