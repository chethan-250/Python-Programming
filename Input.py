print("Input and Output Operation")

boy_name = input("Boy_name: ")
boy_Age = int(input("Age: "))
girl_name = input("Girl_name: ")
girl_age = int(input("Age: "))

print(boy_name)
print(girl_name)

#abs for absolute if girl is elder
age_diff = abs(boy_Age - girl_age)

print(boy_name + " loves " + girl_name + ". the age difference is " + str(age_diff), " years ")

print(f"{boy_name} loves {girl_name}. the age diffrence is {age_diff} years")

