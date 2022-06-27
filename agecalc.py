from datetime import date

current_year = date.today().year
print(f"Current year: {current_year}")
end = False
while end == False:
    try:
        age = int(input("Persons age: "))
        birthyear = current_year - age
        final_age = current_year - birthyear
        print(f"|Birthyear: {birthyear}| |Age: {final_age}|")
        year_dest = int(input("Persons age in a specified year: "))
        age_year_dest = year_dest - birthyear
        print(f"|Person was '{age_year_dest}' years old in '{year_dest}'.|")
        cont = input("Do you wish to continue? If not type 'no'. ").lower()
        if cont == "no":
            end = True
    except ValueError: 
        print("Please enter a number.")

