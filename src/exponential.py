def convert_exponential_to_number(exp_num):
    # Convert the exponential number to a float
    num = float(exp_num)

    # Format the number to remove scientific notation and show as an integer if possible
    if num.is_integer():
        return str(int(num))
    else:
        return str(num)


# Example usage:
exp_num1 = "1e3"
exp_num2 = "2.5e2"
exp_num3 = "3.14159e-3"

print(convert_exponential_to_number(exp_num1))  # Output: "1000"
print(convert_exponential_to_number(exp_num2))  # Output: "250.0"
print(convert_exponential_to_number(exp_num3))  # Output: "0.00314159"
