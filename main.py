Numbers=list(map(int,input().split()))
k=[]
p=[]
j=[]
n=[]
w=[]
print("1. Maximum number =",max(Numbers))
print("2. Minimum number =",min(Numbers))
print("3. Sum of the numbers =",sum(Numbers))
print("4. Average of the numbers =",int((sum(Numbers)/len(Numbers))))
list = set(Numbers)
list.remove(max(list))
print("5. Second maximum number =",max(list))
for i in Numbers:
    if i%2==0:
        k.append(i)
    else:
        p.append(i)
print("6. Even numbers =",str(k).replace("[","").replace("]",""))
print("7. Odd numbers =",str(p).replace("[","").replace("]",""))
for i in Numbers:
    if 9< i <100:
        j.append(i)
print("8. Two digit numbers =",str(j).replace("[","").replace("]",""))
for i in Numbers:
    if i>0:
        w.append(i)
    else:
        n.append(i)
print("9. Negative numbers =",str(n).replace("[","").replace("]",""))
print("10. Positive numbers =",str(w).replace("[","").replace("]",""))      
        


        
        
