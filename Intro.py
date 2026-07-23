print("Welcome to Python programming!")
print("\n")
print("In this introduction you will learn about general python syntax, names, variables, mathematical operations")
# Introduction to Python

def main():
    print("=== Introduction to Python ===")

    # 1) Variables and basic data types
    language = "Python"
    year = 1991
    version = 3.12
    fun_to_learn = True

    print(f"Language: {language}")
    print(f"First released: {year}")
    print(f"Version example: {version}")
    print(f"Fun to learn? {fun_to_learn}")

    # 2) Basic math
    a = 10
    b = 5
    print("\nBasic Math:")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")

    # 3) User input
    name = input("\nEnter your name: ")
    age = int(input("Enter your age: "))

    # 4) Condition
    if age >= 18:
        print(f"Hi {name}, you are an adult.")
    else:
        print(f"Hi {name}, you are under 18.")

    # 5) Loop
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(i)

    print("\nProgram finished. Keep practicing Python!")

if __name__ == "__main__":
    main()
