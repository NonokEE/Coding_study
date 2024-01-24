#include <iostream>
#include <typeinfo>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for(int i = 0 ; i < 26 ; i ++)
    {
        printf("%c ", i + 'A');
    }
    
}
