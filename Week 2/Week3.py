
# a = 42
# b = 3.13
# c = "Hello"
# d = [1, 2, 3]
# e = {"x": 10}
# f = True
# g = None
# print( type(a), type(b), type(c), type(e), type(f), type(g))

# score_text = "85"
# score_number = int(score_text)
# print(score_number + 10)

# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# x = 18
# y = 20

# print(x == y)
# print(x < y and x > 10)
# print(not (x == y))

# grade = 78

# if grade >= 90:
#     print("Excellent")
# elif grade >= 75:
#     print("Passed")
# else:
#     print("Need Improvement")    

# weather = "rainy"
# has_umbrella = False

# if weather == "rainy":
#     if has_umbrella:
#         print("You're covered")
#     else:
#         print("you might get wet")
# else:
#     print("Enjoy the sunshine")

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("i like", fruit)

# for i in range (1,10):
#     print("Count:", i)

# attemps = 0

# while attemps < 3:
#     print("Attempt number", attemps + 1)
#     attemps += 1

# score = [88, 92, 79, 95]

# print(score[0])
# print(score[-1])
# score.append(100)
# print(len(score))
# print(sum(score) / len(score))

# for scores in score:
#     if scores >= 90:
#         print(scores, "is a high sore")

# student = {
#     "name": "ana",
#     "age": 21,
#     "grades": [88, 89, 79]
# }

# print(student["name"])
# print(student["grades"][1])
# print["age"] = 22
# student["Year_level"] = 3
# print(student["Year_level"])

# for key, value in student.items():
#     print(key, ":", value)

# def calculate_average(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     return total / count
# result = calculate_average([80, 90, 100])
# print(result)

# def classify_bmi(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif bmi < 25:
#         return "Normal"
#     elif bmi < 30:
#         return "Overweight"
#     else:
#         return "obese"
    
# print(classify_bmi(24))

# def greet(name="student"):
#     print("Hello,",name)

# greet()
# greet("RM")

# def health_check(temperature, has_cough):
#     if temperature > 38 and has_cough:
#         return "possible flu, see a doctor"
#     elif temperature > 38:
#         return "fever detected, Monitor closely"
#     elif has_cough:
#         return "Mild cough, rest and hydrate"
#     else:
#         return "No symptoms detected"
# print(health_check(39, True))

# def assistant (user_inputs):
#     user_inputs = user_inputs.lower()

#     if "hello" in user_inputs:
#         return "Hi there! How can i help you?"
#     elif "weather" in user_inputs:
#         return "Its sunny day"
#     elif "time" in user_inputs:
#         return " i cant check the clock, but its good time to CODE"
#     elif "bye" in user_inputs:
#         return "Goodbye!"
#     else:
#         return "Sorry, i dont understand that"
    
# while True:
#     text = input("You: ")
#     if text.lower() == "quit":
#         break
#     print("Assistant", assistant(text))

# def check_adoption_ready(species, age_months, vaccinated):
#     if species not in ["dog", "cat"]:
#         return "Unsupported Choices"
#     elif not vaccinated:
#         return "Not Ready: Needs vaccination"
#     elif age_months >= 2:
#         return "Ready for adaption"
#     else:
#         return "Not ready: needs vaccination"
    
# dog_list = []
# cat_list = []
# waiting_for_vaccination = 0
    
# while True:
#     species_input = input("Enter animal species (dog/cat, or 'done' to stop)").strip().lower()

#     if species_input == "done":
#         break

#     name = input("Enter animals name: ").strip()
#     age_input = int(input("Enter age in months: "))
#     vaccinated_input = input("Is this animal vaccinated? (yes/no): ").strip().lower()

#     is_vaccinated = vaccinated_input  == "yes"

#     result = check_adoption_ready(species_input, age_input, is_vaccinated)

#     if result == "Ready for adaption":
#         if species_input == "dog":
#             dog_list.append(name)
#         elif species_input == "cat":
#             cat_list.append(name)
#         print(name + ": Ready for Adaption")
#     elif result == "Not Ready: Needs vaccination":
#         waiting_for_vaccination +=1
#         print(name + ": Not Ready, Need Vaccination")
#     else:
#         print(name + ": Unsupported species, not added to any list")

#     print()

#     print("Dog List", dog_list)
#     print("Cat list", cat_list)
#     print("Animals waiting on vaccination:", waiting_for_vaccination)