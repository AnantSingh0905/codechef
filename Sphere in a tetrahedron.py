from math import *
def sq(a):
    return a*a
k = int(input())
for i in range(k):
    a,b,c,d,e,f=map(int,input().split())
    vol  = sqrt(4*sq(a)*sq(b)*sq(c)-sq(a)*sq(sq(b)+sq(c)-sq(f))-sq(b)*sq(sq(a)+sq(c)-sq(e))-sq(c)*sq(sq(a)+sq(b)-sq(d))+(sq(b)+sq(c)-sq(f))*(sq(c)+sq(a)-sq(e))*(sq(a)+sq(b)-sq(d)))/12;
    t1 = (a+b+d)/2.0;
    t2 = t1*(t1-a)*(t1-b)*(t1-d);
    as1 = sqrt(t2);
    t1 = (a+c+e)/2.0;
    t2 = t1*(t1-a)*(t1-c)*(t1-e);
    as2 = sqrt(t2);
    t1 = (b+c+f)/2.0;
    t2 = t1*(t1-b)*(t1-c)*(t1-f);
    as3 = sqrt(t2);
    t1 = (d+e+f)/2.0;
    t2 = t1*(t1-d)*(t1-e)*(t1-f);
    as4 = sqrt(t2);
    sa = as1+as2+as3+as4;
    r = 3.0*vol/sa;
    print('%.4f' %r)
