//G4 9935 문자열 폭발
#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string base, bomb;
    cin >> base >> bomb;
    
    string res = "";

    for(int base_index = 0 ; base_index < base.size() ; base_index++)
    {
        res += base[base_index];
        if(res.back() == bomb.back())
        {
            bool trigger = true;
            if(res.size() < bomb.size()) continue;
            for(int bomb_index = 0 ; bomb_index < bomb.size() ; bomb_index++)
            {
                if(res[res.size() - bomb.size() + bomb_index] != bomb[bomb_index])
                {
                    trigger = false;
                    break;
                }
            }
            if(trigger)
            {
                for(int i = 0 ; i < bomb.size() ; i++) res.pop_back();
            }
        }
    }
    if(res.empty()) cout << "FRULA";
    else            cout << res;
}
