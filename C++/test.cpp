#include <iostream>
#include <typeinfo>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string test = "123456789";
    for (auto iter = test.begin() ; iter != test.end(); ++ iter)
    {
        cout << *iter + '0' << endl;
        
    }
    
}
