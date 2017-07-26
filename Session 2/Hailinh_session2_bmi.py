
##xac dinh chi so BMI

height = float(input("Ban cao bao nhieu cm?"))
weight = float(input("Ban nang bao nhieu kg?"))
bmi = float(weight/(height*height*0.01*0.01))

if bmi < 16:
    print("Ban hoi thieu thit qua, bo sung khan cap")
elif 16 < bmi <= 18.5:
    print("Can bo sung them xiu thit cho day dan")
elif bmi <= 25:
    print("an uong day du dinh duong, tiep tuc phat huy hen")
elif bmi <= 30:
    print("Co ve ban hoi thua can :D")
else:
    print("Tap the duc nhieu vo nhe, hoi mum mim qua roi")

