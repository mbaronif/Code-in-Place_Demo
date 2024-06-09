def convert_c_to_f(temp_in_celsius):
    temp_in_farenheigt = temp_in_celsius * 1.8 + 32
    return temp_in_farenheigt

temperature_in_f = convert_c_to_f(26)
print(temperature_in_f)

