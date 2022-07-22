print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = (name1 + name2).lower()

T = int(combined_names.count("t"))
R = int(combined_names.count("r"))
U = int(combined_names.count("u"))
E = int(combined_names.count("e"))
TRUE = str (T + R + U + E)
# TRUE_sum = str ((TRUE // 10) + (TRUE % 10))


L = int(combined_names.count("l"))
O = int(combined_names.count("o"))
V = int(combined_names.count("v"))
E = int(combined_names.count("e"))
LOVE = str (L + O + V + E)

# LOVE_sum = str ((LOVE // 10) + (LOVE % 10) )

love_score = int (TRUE + LOVE)

if love_score <10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >40 and love_score <50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")



