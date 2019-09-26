import add
import sub
import prod
import div

choice = input("enter operaton:\n1-add\n2-sub\n3-prod\n4-div\nchoice:\t")
a = int(input("a: "))
b = int(input("b: "))
if choice==1:
	print(add(a, b))
if choice==2:
	print(sub(a, b))
if choice==3:
	print(prod(a, b))
if choice==4:
	print(div(a, b))