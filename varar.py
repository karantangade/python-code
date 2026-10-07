def add(*a):
    s=0;
    for i in range(len(a)):
        s+=a[i];
    return s;

re=add(10,20,30,40);
print(re);
