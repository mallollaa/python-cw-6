# write your code here
# --- part 1 -----
person = {
    'name' : 'manal',
    'age' : 22,
    "hobbies" : ["reading" , "playing" , "music"]
}
print(f" my name is {person['name']} I am {person['age']}")

# ----- part 2 -----

person["age"] = 33
person['country'] = ' kuwait'

print(person)
print(len(person))

# ---- part 3 ----

person["hobbies"].append('watching tv')

def check_hobbies(person):
    if len(person['hobbies']) >= 8 :
        print("WOW YOU ARE AMAZING")
    else:
        print("try harder")

check_hobbies(person)