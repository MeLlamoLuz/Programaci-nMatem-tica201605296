sencillo = 0

for l in range(3):
	for p in range(1+(200-100*l)/50):
		for m in range(1+(200-100*l-50*p)/20):
			for x in range(1+(200-100*l-50*p-20*m)/10):
			  for y in range(1+(200-100*l-50*p-20*m-10*x)/5):
			    for z in range(1+(200-100*l-50*p-20*m-10*x-5*y)/2):
			      sencillo = sencillo + 1

print sencillo + 1