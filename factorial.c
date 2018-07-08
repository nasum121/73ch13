#include<stdio.h>
int main()
{
int a,fact,i;
fact=1;
printf("");
scanf("%d",&a);
if (a==1)
{
	printf("%d",a);
}
for (i=1;i<=a;i++)
{
	fact=fact*i;
	
}
printf("%d",fact);
}
