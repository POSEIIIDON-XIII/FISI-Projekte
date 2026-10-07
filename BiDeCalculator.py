def decimal_to_binary(number):
    if number == 0:
        return "0"

    remains = []

    while number > 0:
        remains.append(number % 2)
        number = number // 2

    binary = []
    remains.reverse()
    for every_cipher in remains:
        binary.append(str(every_cipher))

    binary_string = "".join(binary)
    return binary_string



def binary_formatting(binary_string):
    if binary_string == "0":
        return binary_string

    length_binary_string = len(binary_string)
    remains_binary_string = length_binary_string % 4

    if remains_binary_string == 0:
        missing_zeroes = 0
    else:
        missing_zeroes = 4 - remains_binary_string

    binary_result = "0" * missing_zeroes + binary_string
    nibbles = []

    for i in range(0, len(binary_result), 4):
        nibble = binary_result[i: i + 4]
        nibbles.append(nibble)

    formatted_binary_string = " ".join(nibbles)
    return formatted_binary_string



def binary_to_decimal(binary):
    result = 0
    for cipher in binary:
        result = result * 2 + int(cipher)
    return result




while True:
    try:
        mode = int(input("What would you like to convert?\n1 - Decimal to Binary\n2 - Binary to Decimal\n\nYour selection: "))
        if mode == 1:
            print(f"You have selected '{mode} - Decimal to Binary.")
        elif mode == 2:
            print(f"You have selected '{mode} - Binary to Decimal.")
        else:
            print("Invalid input! Please type 1 for decimal to binary or 2 for binary to decimal.")
            continue
        break
    except ValueError:
        print("Invalid input! Please type 1 for decimal to binary or 2 for binary to decimal.")



if mode == 1:
    while True:
        try:
            mode_1 = int(input("Which decimal number would you like to convert? "))
            break
        except ValueError:
            print("Invalid input! Please use only numbers.")


    result = binary_formatting(decimal_to_binary(mode_1))
    print(result)



elif mode == 2:
    while True:
        mode_2 = input("Which binary number would you like to convert? ")
        mode_2 = mode_2.replace(" ", "")
        if mode_2 == "":
            print("Invalid input! Please enter a binary number.")
        else:
            valid = True
            for character in mode_2:
                if character != "0" and character != "1":
                    valid = False
                    print("Invalid input! A binary number may only consist of 0s and 1s.")
                    break
            if valid:
                result = binary_to_decimal(mode_2)
                print(result)
                break        