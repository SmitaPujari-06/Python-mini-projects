def show_menu():
    print('\n1. Add expense')
    print('2. Show expenses')
    print('3. Exit')


FILE_NAME = 'total_expenses.txt'

while True:
    show_menu()
    choice = input('Choose an option (1-3): ').strip()

    # 🔹 ADD EXPENSE
    if choice == '1':
        date = input('Enter the date (DD/MM/YYYY): ').strip()
        category = input('Enter the category (groceries, transportation, etc.): ').strip()
        amount = input('Enter the amount of money spent: ').strip()

        expense = f"{date},{category},{amount}"

        with open(FILE_NAME, 'a') as f:
            f.write(expense + '\n')

        print('✅ Expense added!')

    # 🔹 SHOW EXPENSES
    elif choice == '2':
        try:
            with open(FILE_NAME, 'r') as f:
                print(f"\n{'Date':<15}{'Category':<15}{'Amount':<10}")
                print('-' * 40)

                empty = True

                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split(',')

                    if len(parts) != 3:
                        print(f"⚠ Skipping corrupted line: {line}")
                        continue

                    date, category, amount = parts
                    print(f"{date:<15}{category:<15}₹{amount:<10}")
                    empty = False

                if empty:
                    print("No expenses recorded yet.")

        except FileNotFoundError:
            print("No expenses recorded yet.")

    # 🔹 EXIT
    elif choice == '3':
        print('Bye bye!')
        break

    else:
        print('Invalid choice, please try again.')