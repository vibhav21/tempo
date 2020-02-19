#include <iostream>

#include <bits/stdc++.h>
using namespace std;
int nthLargestNo(int n ,int a[],int l)
{
   
    for(int i=0;i<n;i++)
    {
        for (int j=0;j<l;j++)
        {
            if(a[j]>a[j+1])
            {
               swap(a[j],a[j+1]); 
            }
        }
        
    }
   return a[l-n];
}
int main() {
    int a[]={0,23,1,56,78,2,9,5,8};
    int n;
   
    cin>>n;
   int  l=end(a)-begin(a);
   cout<< nthLargestNo(n,a,l);
   return 0;
    
}