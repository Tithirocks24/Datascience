def show_balance(balance):
    print(f"Your Balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter your amount: "))
    if amount < 0:
        print("Your amount is not valid.")
        return 0
    return amount

def withdraw(balance):
    amount = float(input("Enter your amount: "))
    if amount > balance:
        print("You have entered an excess amount.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            withdrawal_amount = withdraw(balance)
            balance -= withdrawal_amount
        elif choice == "4":
            is_running = False
        else:
            print("You entered a wrong number.")

    print("Thank you! Have a nice day.")

if __name__ == "__main__":
    main()
def show_balance(balance):
    print(f"Your Balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter your amount: "))
    if amount < 0:
        print("Your amount is not valid.")
        return 0
    return amount

def withdraw(balance):
    amount = float(input("Enter your amount: "))
    if amount > balance:
        print("You have entered an excess amount.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            withdrawal_amount = withdraw(balance)
            balance -= withdrawal_amount
        elif choice == "4":
            is_running = False
        else:
            print("You entered a wrong number.")

    print("Thank you! Have a nice day.")

if __name__ == "__main__":
    main()
