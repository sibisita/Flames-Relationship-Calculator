x=input("Enter first name : ").upper()
y=input ("Enter second name : ").upper()
u,v=list(x),list(y)
for i in x:
	if i in v:
		u.remove(i)
		v.remove(i)
flames = ['Friends','Love','Affections','Marry','Enemy','Sister']
t = len(u)+len(v)
pointer=0

if (t ==0):
	print ('All letters got cancelled')


else:
	while len(flames)>1:
		lenflames=len(flames)
		pointer = (pointer+t) % lenflames
		if pointer == 0:
			del(flames[-1])
		else:
			del(flames[pointer-1])
		if pointer == 0:
			pointer == len(flames)
		else:
			pointer-=1


	print('The Flames match of {} and {} is {}'.format(x,y,flames[0]))