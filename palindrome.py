def palindrome(x):
    x = x.lower()
    c_x = ""

    for char in x:
        if char.isalnum():
                c_x += char

    reversed_X = ""
    for char in c_x:
        reversed_X = char + reversed_X

    return c_x == reversed_X

if __name__ == "__main__":
    u_input = input("Enter word: ")
    if palindrome(u_input):
        print(f"'{u_input}' is a palindrome.")
    else:
        print(f"'{u_input}' is not a palindrome")
