#make an empty list to store the user information
#define valid criteria for name and age
#ask user for name, age, number, if invalid print an error message, otherwise continue.
#store name and age using dictionary array and add to the list
#ask user if they want to continue, otherwise break the loop
#assume the first entry is the oldest, if the current age is greater than the previous age, update the oldest person
#find the people with the highest age
#if 2 or more people have the same higher age, print the name, age, and number of those people.
    #This is to define valid criteria for name, age, and number.
def is_valid_full_name(name):
    return all(part.isalpha() for part in name.split()) and len(name) >0

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 122

def is_valid_number(num):
    return num.isdigit() and len(num) == 11
    #This to store the user information.
def main():
    user_info = []
        #This is to ask user for the information, if invalid print error, otherwise continue.
    while True:
        name = input("Enter your Full Name: ")
        if not is_valid_full_name(name):
            print("Error: Invalid age. Please Enter a valid name.")
            continue

        age = input("Enter your Age: ")
        if not is_valid_age(age):
            print("Error: Invalid age. Please enter a valid age (0-122).")
            continue

        num = input("Enter your Phone number: ")
        if not is_valid_number(num):
            print("Error: Invalid number. Please input 11 digit number.")
            continue

        user_information = { #This is to store name, age, number.
            "name": name,
            "age": int(age),
            "phone number": num
        }
        user_info.append(user_information) #This is to add another entry.
            #This is for asking the user for another entry.
        another_entry = input("Do you want to enter another entry? (Yes/No): ").strip().lower()
        if another_entry == 'no':
            break
        
    if user_info:
        oldest_users = []
        max_age = -1

        for user_information in user_info:
            if user_information['age'] > max_age:
                max_age = user_information['age']
                oldest_users = [user_information]
            
            elif user_information['age'] == max_age:
                oldest_users.append(user_information)
        
        print(f"The following user/s is/are the oldest person with an age of {max_age}:")
        for user_information in oldest_users:
            print(f"- {user_information['name']}, {user_information['phone number']}") 

        #This is to check if there are information entered.
    else:
        print("No user information was entered.")
    #This is to run the code.
if __name__ == '__main__':
    main()
