from function import display_rang

input_number = input()
try:
    try:
        input_number = int(input_number)
    except:
        input_number = float(input_number)
except:
    input_number = str (input_number)
result = display_rang(input_number)
print(result)
