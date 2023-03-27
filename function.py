def validate_number(number):
    passengers = (input)  # จำนวนผู้โดยสารทั้งหมด
    van_capacity = (input) # จำนวนผู้โดยสารสูงสุดของรถตู้
    number = passengers // van_capacity  # จำนวนรถตู้ที่จำเป็นต้องใช้

    if passengers % van_capacity != 0:
        number += 1

    

def display_rang(number):
    result = validate_number(number)
