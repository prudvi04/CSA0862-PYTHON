def shuffle(l1,l2):
  output= []
  for i in range(len(l1)):
    output.append(l1[i])
    if i<len(l2):
      output.append(l2[i])
  if len(l1)<len(l2):
    output= output+l2[len(l1):]
  print("Shuffled list =",output)
  
n = int(input("Enter the number of elements of l1: "))
l1=[]
for i in range(n):
  element = int(input("Enter the element: "))
  l1.append(element)
  
m = int(input("Enter the number of elements of l2: "))
l2=[]
for i in range(m):
  element = int(input("Enter the element: "))
  l2.append(element)
  shuffle(l1,l2)

