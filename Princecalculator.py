import streamlit as st

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2
    else:
        return "Invalid operator! Use +, -, *, or /."

# Streamlit App UI
st.title("🧮 Simple Streamlit Calculator")
st.write("Perform basic arithmetic operations easily.")

# Input fields
num1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter the second number:", value=0.0, step=0.1)

# Operator selection
operator = st.radio(
    "Choose an operator:",
    ("+", "-", "*", "/")
)

# Button to calculate
if st.button("Calculate"):
    result = calculator(num1, num2, operator)
    st.success(f"The result is: {result}")
