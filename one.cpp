#include<iostream>
using namespace std;

void printstars(int n) {

        int i,j;

 for(i=0;i<n;i++) {
    for (j=0; j<=i; j++) {

    cout << j+1;

    }
    cout << "\n";

 }
}


int main(){  

printstars(5);
printstars(100);
   
    return 0;
}