m=int(input("ENTER THE VALUE of m:"))
n=int(input("ENTER THE VALUE of n:"))

if(n==0):
    print("GCD=",m)
        
elif(m%n!=0):
    r=m%n
    print("These number will have remainder",r)
    
    if(n%r==0):
        print("GCD=",r)
    elif(n%r!=0):
        s=n%r
        print("These number will have remainder",s)
        
        if(r%s==0):
            print("GCD=",s)
        elif(n%r!=0):
            t=r%s
            print("These number will have remainder",t)

            if(s%t==0):
                print("GCD=",t)
            elif(s%t!=0):
                u=s%t
                print("These number will have remainder",u)

                if(t%u==0):
                    print("GCD=",u)
                elif(t%u!=0):
                    v=t%u
                    print("These number will have remainder",v)

                    if(u%v==0):
                        print("GCD=",v)
                    elif(u%v!=0):
                        w=u%v
                        print("These number will have remainder",w)



            
else:
    m%n==0
    print("GCD=",n)
    
                
