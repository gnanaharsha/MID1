import add
import sub
import prod
import div
import sys

global a, b


args = sys.argv
# print("enter operaton:\n1-add\n2-sub\n3-prod\n4-div\nchoice:\t")
choice, a, b = args[1], int(args[2]), int(args[3])
print(choice, a, b)
# a = int(input("a: "))
# b = int(input("b: "))
ans = 0
if choice=="1":
	ans = add.add(a, b)
if choice=="2":
	ans = sub.sub(a, b)
if choice=="3":
	ans = prod.product(a, b)
if choice=="4":
	ans = div.div(a, b)

print(ans)