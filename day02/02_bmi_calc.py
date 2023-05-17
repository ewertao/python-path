# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_flt = float(height)
weight_flt = float(weight)

bmi_flt = (weight_flt / height_flt ** 2)
bmi_int = int(bmi_flt)
print(bmi_int)