def show_menu():
    print('1.Add expense')
    print('2.Show expenses')
    print('3.Exit')

while True:
    show_menu()

    choice = input('Choose an option (1-3):').strip()

    if choice == '1':
        date = input('Enter the date (DD/MM/YY): ')
        catagory = input('Enter the category (groceries, transportation,  etc.,): ')
        amount = input('Enter the amount of money spent: ')

        expenses = f'{date},{catagory},{amount}'
        with open('total_expenses.txt','a') as e:
            e.write(expenses)

        print('Expense added!')

    elif choice =='2':
        with open('total_expenses.txt','a') as e:
            content = e.read()
            print(content)

    elif choice == '3':
        print('Bye byee!')
        break
    else:
        print('Invalid choice')
