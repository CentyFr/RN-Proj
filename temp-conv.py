def C_to_F(C):
    return (C * 9/5) + 32

def F_to_C(F):
    return (F - 32) * 5/9

def C_to_K(C):
    return C + 273.15

def K_to_C(K):
    return K - 273.15

if __name__ == "__main__":
    print("Choose The Conversion:")
    print("1. Celsius To Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius To Kelvin")
    print("4. Kelvin To Celsius \n")

    choice = int(input("Enter Your Choice (1-4): "))
    temp = float(input("Enter The Temperature: "))

    if choice == 1:
        print(f"{temp}°C is {C_to_F(temp):.2f}°F")
    elif choice == 2:
        print(f"{temp}°F is {F_to_C(temp):.2f}°C")
    elif choice == 3:
        print(f"{temp}°C is {C_to_F(temp):.2f}K")
    elif choice == 4:
        print(f"{temp}K is {C_to_F(temp):.2f}°C")
    else:
        print("Please Choose One Of The Options.")

