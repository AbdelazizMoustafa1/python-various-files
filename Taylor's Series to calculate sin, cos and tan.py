#to use PI and import all decimal methods
import math
from decimal import *

'''
Example on how Decimal method works
print('{:>10}  {:>5}  {:>2}'.format('a','b','c'))
Outputs:
         a    b c
10 to pass a, then 5 to pass b, then 2 to pass c
'''

#Taylor's Series to calculate sin, cos and tan
#function takes 2 arguments, x:Angle and p:precision
def sct(x,p):
    deg = x #deg is angle in degrees
    x = deg*math.pi/180 #x is now angle in radians
    print('Angle = '+str(x)+' rad')
    
    #for formatting eg if p=3, places are 3+p and decimal points are p+1
    o='{:0'+str(3+p)+'.'+str(p+1)+'f}'
    u='{:>'+str(int(10+(p+3)*0.5))+'}  {:>'+str(10+p+3)+'}  {:>'+str(10+p+3)+'}  {:>'+str(10+p+3)+'}'
    
    #initialize and fill arrays for sin, cos and final values
    sv=[]
    cv=[]
    FVal=[]
    
    for k in range(1,50):
        # sv.append( float( o.format((x**(2*k-1)) / math.factorial(2*k-1))))
        #cv.append( float( o.format((x**(2*k-2)) / math.factorial(2*k-2))))
        sv.append( (x**(2*k-1)) / math.factorial(2*k-1))
        cv.append( (x**(2*k-2)) / math.factorial(2*k-2))

    #identigying number of decimals-->
    #Decimal('1.41421356').quantize(Decimal('1.000')) Outputs:1.414
    for i in range(len(sv)):    #sv=o.format(sv[i])
        sv[i]=Decimal(str(sv[i])).quantize(Decimal('1.0'+'0'*p))
    for i in range(len(cv)):
        cv[i]=Decimal(str(cv[i])).quantize(Decimal('1.0'+'0'*p))

    #printing values when computong sin and cos

    print(u.format('sin(x) ','|TO|','|TN|', '|TO-TN|'))
    FV = 0
    for i in range(len(sv)-1):
       print(i+1)
       #(-1)**(k+1) * >>to work with iterating sin signes (+ & -)
       FV+=  (-1)**(i) * sv[i]
       TO=sv[i]
       TN=sv[i+1]
       print('{:>10}  {:>10}  {:>10}  {:>10}'.format(FV,TO,TN, o.format(TO-TN)))
       if (abs(TO-TN)) < (10**-p):
           FV+=  (-1)**(i) * sv[i+1]
           FVal.append(FV)
           print(2+i)
           print(FV)
           break

    print('\n'+u.format('cos(x) ','|TO|','|TN|', '|TO-TN|'))
    FV = 0
    for i in range(len(cv)-1):
       print(i+1 )
       #(-1)**(k+1) * >>to work with iterating cos signes (+ & -)
       FV+=  (-1)**(i) * cv[i]
       TO=cv[i]
       TN=cv[i+1]
       print('{:>10}  {:>10}  {:>10}  {:>10}'.format(FV,TO,TN, o.format(TO-TN))) 
       if (abs(TO-TN)) < (10**-p):
           FV+=  (-1)**(i) * cv[i+1]
           FVal.append(FV)
           print(2+i)
           print(FV)
           break

    #Calculating tan(x)
    FVal.append(FVal[0]/FVal[1])
    #limiting final results to the specified precision
    for i in range(len(FVal)):
        FVal[i]=Decimal(str(FVal[i])).quantize(Decimal('1.'+'0'*p))
    

    #print sin, cos and tan values
    print('\nFor '+str(deg)+' degrees:'+
            '\nSin  = '+ str( FVal[0]  ) +
            '\nCos = '+ str( FVal[1]  ) +
            '\nTan = '+ str( FVal[2]  )
              )




#specify precision and handle cases, eg entering strings, floats or enter
def precision():
    try:
        precision = int(input('Specify degree of precision? -default is 10-'))
    except:
        precision = 10
        print ("This is not an integer \n->precision = "+ str(precision))
    return precision

#print instructions
print('current precision = 10\n'+
          '1: set precision\n2: calculate sine, cosine and tan\n3: Quit')

nop = int(input('Enter number of procedure: '))

if nop != 3:
    if nop ==1:
        pre = precision()
    elif nop == 2:
        pre = 10
        
    #input degrees
    deg =float(input('Enter angle in degrees: '))
    sct(deg,pre)

    '''#used before getting the formula to calculate sine,cosine and tan 
    sval= [y]
    cval= [1]
    h=5
    while h<=20:
        #print('h is here')
        sval.append(y**h/math.factorial(h))
        cval.append(y**(h-1)/math.factorial(h-1))
        h+=4  
    n=3
    while n<=19:
        #print('n is here')
        sval.append(-y**n/math.factorial(n))
        cval.append(-y**(n-1)/math.factorial(n-1))
        n+=4
    pola = [sum(sval),sum(cval),sum(sval)/sum(cval)]
    return(pola)'''
