def main():
    print('\nWelcome to My Program')
    print('---------------------')
    print('1. Show Summary')
    print('2. Generate More Data')
    print('3. Update Results')
    print('4. Exit')

    choice = input('\nChoose an option: ')

    if choice == '1':
        print('Run code to show summary')
    elif choice == '2':
        print('Run code to generate data')
    elif choice == '3':
        print('Run code to update results')
    elif choice == '4':
        print('Bye!')
    else:
        print('Invalid choice')

if __name__ == '__main__':
    main()