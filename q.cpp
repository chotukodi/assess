#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
    ifstream file;
    file.open("ok.txt");
    int i=0;  
    char answer, all_answers[5];
    string question;
    while (!file.eof())
    {
        getline(file,question);
                cout<<question<<endl;
        if ( question[0]=='*' && question[1]=='*') {
            cin >> answer;
            all_answers[i++] = answer;
        }
    
    }

    file.close();
 
}
