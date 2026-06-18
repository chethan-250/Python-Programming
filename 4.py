Boy_Name = input("Boy_name: ")
Boy_Age = int(input("Boy_age: "))
Girl_Name = input("Girl_name: ")
Girl_Age = int(input("Girl_age: "))

'''
abs is absolute : 
because somt times boy might be younger
'''
Age_Diff = abs(Boy_Age - Girl_Age)

# String concatination

print(Boy_Name + " Loves " + Girl_Name + " Age diffrence is " + str(Age_Diff) + " Year " )
#formatted print
#print(f"{Boy_Name} Loves {Girl_Name}. age diffrence is {Age_Diff} Year")

