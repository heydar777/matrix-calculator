def menu():

    print("="*40)
    print("      MATRIX CALCULATOR")
    print("="*40)

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Scalar Multiply")
    print("5. Scalar Divide")
    print("6. Transpose")
    print("7. Determinant")
    print("8. Inverse")
    print("9. Identity Matrix")
    print("10. Zero Matrix")
    print("0. Exit")

    return input("\nChoose an option: ")

def main():

    while True:

        choice = menu()

        if choice == "0":

            print("Good Bye!")

            break
if __name__ == "__main__":
    main()