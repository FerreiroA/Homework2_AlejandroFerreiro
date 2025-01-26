print("Welcome to the Net Salary Calculator!")

try:
    # Reading inputs
    gross = input("Enter your gross salary: ")
    gross = int(gross)  # Potential source of error
    num_children = input("How many children do you have? ")
    num_children = int(num_children)  # Potential source of error

    tax_rate = 0  # Default tax rate

    # Determining the base tax rate
    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    # Calculating tax cut based on children
    if gross < 2000:
        tax_cut = num_children * 0.01  # 1% per child
    else:
        tax_cut = num_children * 0.005  # 0.5% per child

    # Ensuring tax cut doesn't make tax rate negative
    tax_rate -= tax_cut
    if tax_rate < 0:
        tax_rate = 0

    # Calculating net salary
    net_salary = gross * (1 - tax_rate)

    print("Your net salary is:", round(net_salary, 2))

except ValueError:
    print("Invalid input. Please enter numeric values for gross salary and number of children.")