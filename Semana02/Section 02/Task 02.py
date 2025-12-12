"""  if Statement """

# The if statement is used to execute code conditionally.
# Syntax:
# if condition:
#     # code to execute if condition is True

# The if statement allows a program to make decisions based on a condition.
# Syntax:
# if condition:
#     # block of code executed when the condition evaluates to true
# else:
#     # block of code executed when the condition evaluates to false

# Example:
age = 23
if age >= 18:
    print("You are an adult.")

# Using if...else:
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Using if...elif...else:
if age > 60:
    print("You are an elderly person.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")


# Example: Validating a name with if and else
name = "Lo"

# Check the length of the name
print(len(name), type(len(name)))

INVALID_NAME = len(name) < 3

if INVALID_NAME:
    print("Name must be at least 3 characters long.")
else:
    print("Valid name.")

# Using the opposite logic
if not INVALID_NAME:
    print("Valid name.")
else:
    print("Name must be at least 3 characters long.")


# Validação de múltiplas entradas
# Condições:
# - O nome deve ter pelo menos 3 caracteres
# - A idade deve ser no mínimo 18

name = "Los"
age = 18
errors = []

if len(name) < 3:
    errors.append("Name must be at least 3 characters long.")

if age < 18:
    errors.append("Age must be at least 18.")

# In Python, empty lists are considered False in conditionals
if errors:
    print("Errors:", errors)
else:
    print("All inputs are valid.")


# Classifying a number
number = -4

# Check if the number is positive, negative, or zero
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")


# Validating grades and calculating the average
# Approval criteria:
# - Both grades must be valid (between 0 and 10)
# - The final average must be at least 6 to be approved
# - An average between 4 and 5.9 requires a retake
# - An average below 4 results in failure

grade1 = 5.6
grade2 = 10.0

GRADE1_VALID = 0 <= grade1 <= 10
GRADE2_VALID = 0 <= grade2 <= 10

if GRADE1_VALID and GRADE2_VALID:
    average = (grade1 + grade2) / 2
    if average >= 6:
        print("Approved")
    elif average >= 4:
        print("Retake")
    else:
        print("Failed")
else:
    print("Invalid grades")