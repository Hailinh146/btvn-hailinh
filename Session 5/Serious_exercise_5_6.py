def remove_dollar_sign(s):
    s = s.replace("$","")
    return s

s = '150$foranapple'
s_no_dollars_sign = remove_dollar_sign(s)
print(s_no_dollars_sign)

input()

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
