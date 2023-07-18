#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
    ifstream file;
    file.open("ok.dat");

    int Q_No;
    cout<<"question no:"<<endl;
    cin>>Q_No;
   
     if (Q_No<=0)
    {
        cout<<"line number must be >= 1"<<endl;
        return 1;
    }

    if(file.fail())
    {
        cout<<"failed to open"<<endl;
        return 1;
    }

    
    string question;
    int current = 0;
    char answer ;

     
    while (!file.eof())
    {
        if(Q_No==1)
        {
        getline(file,question);
        cout<<question<<endl;
        if(question =="D. 5 5") break; 
        }
        if(Q_No==2)
        {
        getline(file,question);
        cout<<question<<endl;
        if(question =="D. int* arr = new int[10];") break;
        }
    }

    file.close();
 
}
