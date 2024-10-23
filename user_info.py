#make an empty list to store the user information
#define valid criteria for name and age
#ask user for name, age, number, if invalid print an error message, otherwise continue.
#store name and age using dictionary array and add to the list
#ask user if they want to continue, otherwise break the loop
#assume the first entry is the oldest, if the current age is greater than the previous age, update the oldest person
#print the name and age of the oldest person
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
        #This is to fine who is the oldest person in the List.
    if user_info:
        oldest_user = max(user_info, key=lambda user_info: user_info['age'])
        print(f"The oldest person in the List is {oldest_user['name']} with an age of {oldest_user['age']} and Phone Number {oldest_user['phone number']}.")
        print("Note: The information you provided will remain safe and secure within this code.")
        #This is to check if there are information entered.
    else:
        print("No user information was entered.")
    #This is to run the code.
if __name__ == '__main__':
    main()
