#给定一个N*N矩阵，令a[i][j]位矩阵的第i行j列元素
#矩阵应该满足以下三个条件：
#a[k][1]=a[i][k]=1,k为奇数
#a[k][1]=a[1][k]=2,k为偶数
#a[i][j]=a[i-1][j]+a[i][j-1](2<=i,j<=N)
#给定N的大小,试求该矩阵的最大元素值
N=int(input())
l=[]
for i in range (N) :    
    if i%2==0:
        l.append(1)
    else:
        l.append(2)
for i in range(N-1):
    for j in range(N-1-i) :
        if j==0:
            l[j]=l[1]+l[1]
        elif j==N-2-i :
            l[j]=l[j-1]+l[j+1]
            del l[-1]
        else :
            l[j]=l[j-1]+l[j+1]
