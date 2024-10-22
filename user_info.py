#make an empty list to store the user information
#define valid criteria for name and age
#ask user for name, age, number, if invalid print an error message, otherwise continue.
#store name and age using dictionary array and add to the list
#ask user if they want to continue, otherwise break the loop
#assume the first entry is the oldest, if the current age is greater than the previous age, update the oldest person
#print the name and age of the oldest person

def is_valid_full_name(name):
    return all(part.isalpha() for part in name.split()) and len(name) >0

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 122

def is_valid_number(num):
    return num.isdigit() and len(num) == 11

def main():
    user_info = []
    