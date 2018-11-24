def number_of_days(pages, first_day, the_last_day):
    """The function for calculating the number of days"""
    days = int(2 * pages / (first_day + the_last_day))
    print('You will finish reading this book in', days, 'days')


def main():
    """The main function"""
    print('Enter your values:')
    pages = int(input('The number of pages in the book:'))
    first_day = int(input('The number of pages you read on the first day:'))
    the_last_day = int(input('The number of pages you suppose to read on the last day:'))
    number_of_days(pages, first_day, the_last_day)


if __name__ == '__main__':
    main()
