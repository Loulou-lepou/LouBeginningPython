"""
https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
Create a dictionary of names and birthdays.
Ask the user to enter a name,
then return the birthday of that person.
"""
# dictionary of names and birthdays of 100 famous scientists:
birthdays_dict = {'Isaac Newton': 'January 4, 1643',
                  'Albert Einstein': 'March 14, 1879',
                  'Galileo Galilei': 'February 15, 1564',
                  'Nikola Tesla': 'July 10, 1856',
                  'Marie Curie': 'November 7, 1867',
                  'Charles Darwin': 'February 12, 1809',
                  'Thomas Edison': 'February 11, 1847',
                  'Stephen Hawking': 'January 8, 1942',
                  'Alexander Graham Bell': 'March 3, 1847',
                  'Louis Pasteur': 'December 27, 1822',
                  'Richard Feynman': 'May 11, 1918',
                  'Alan Turing': 'June 23, 1912',
                  'Michael Faraday': 'September 22, 1791',
                  'Benjamin Franklin': 'January 17, 1706'
                  }
print("Welcome to the birthday dictionary. We know the birthdays of:")
for key in birthdays_dict:
    print(key)

while True:
    input_part_name = input("Who's birthday do you want to look up?:\n").capitalize()
    for key, value in birthdays_dict.items():
        if input_part_name in key:
            print("{name}'s birthday is {birthday}."
                  .format(name=key, birthday=value))
        else:
            print("Sadly, we don't have his/her birthday.")
    user_choice = input("Do you want to continue? y/n")
    if user_choice == 'n':
        break
