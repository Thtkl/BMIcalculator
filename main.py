import tkinter as tk

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  # convert cm to meters
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        bmi_result.set(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            bmi_category.set("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            bmi_category.set("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            bmi_category.set("You are overweight.")
        else:
            bmi_category.set("You are obese.")
    except ValueError:
        bmi_result.set("Invalid input, please enter numbers.")
        bmi_category.set("")

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("600x400")
window.configure(background='light blue')

# variables to hold the result and category
bmi_result = tk.StringVar()
bmi_category = tk.StringVar()

# Height label and entry
height_label = tk.Label(window, text="Height (cm):", bg='light blue', fg='black', font=('Arial', 14))
height_label.pack(pady=10)
height_entry = tk.Entry(window, font=('Arial', 14))
height_entry.pack(pady=10)

# Weight label and entry
weight_label = tk.Label(window, text="Weight (kg):", bg='light blue', fg='black', font=('Arial', 14))
weight_label.pack(pady=10)
weight_entry = tk.Entry(window, font=('Arial', 14))
weight_entry.pack(pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi, font=('Arial', 14))
calculate_button.pack(pady=20)

# BMI result label
bmi_result_label = tk.Label(window, textvariable=bmi_result, bg='light blue', fg='black', font=('Arial', 14))
bmi_result_label.pack(pady=10)

# BMI category label
bmi_category_label = tk.Label(window, textvariable=bmi_category, bg='light blue', fg='black', font=('Arial', 14))
bmi_category_label.pack(pady=10)

window.mainloop()
