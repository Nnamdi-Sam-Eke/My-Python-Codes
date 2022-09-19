#A code by Urelix®
#A program to determine the percentage of compatibility between two people
name_1 = input('Enter your name :')
name_2 = input('Enter your spouse\'s name:')
names = (name_1  + name_2)

T = names.count('t')
R = names.count('r')
U = names.count('u')
E = names.count('e')
true = str(T + R+ U+ E)

L = names.count('l')
O = names.count('o')
V = names.count('v')
E = names.count('e')
love = str(L + O + V + E)
score_ = true + love
print('Your compatibility level is :' + str( score_ +'%'))