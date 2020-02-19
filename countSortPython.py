a=list(map(int,input().split()))
maxi=max(a)
yo=[0 for i in range(0,maxi+1)]
for i in range(0,len(a)):
    yo[a[i]]+=1
print(yo)    
    
g=0
    
for i in range(0,len(yo)):
    while(yo[i]>0):
        a[g]=i;
        g=g+1
        yo[i]=yo[i]-1
print(a)        
    
