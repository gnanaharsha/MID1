import add
import sub
import prod
import div


choice = input("enter operaton:\n1-add\n2-sub\n3-prod\n4-div\nchoice:\t")
global a, b
a = int(input("a: "))
b = int(input("b: "))
if choice=="1":
	ans = add.add(a, b)
if choice=="2":
	ans = sub.sub(a, b)
if choice=="3":
	ans = prod.product(a, b)
if choice=="4":
	ans = div.div(a, b)

print(ans)