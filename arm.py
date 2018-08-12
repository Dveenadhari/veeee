#include<stdio.h>
int main()
{
    int n1,n2,r,c = 0;
    
    printf("enter the number: ");
    scanf("%d",&n1);
    
    n2= n1;
    while(n2 !=0)
    {
        r=n2%10;
        c=r*r*r;
        n2=n1/10;
    }
    
    if(c == n1)
    {  
        printf("armstrong number ",n1);
    }
    else
    {
       print("not armstrong number",n1);
     }
  }   
      
