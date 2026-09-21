#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cout << "TEST BOARD" << endl << endl;

    vector<int> int_vector;
    int_vector.push_back(1);
    int_vector.emplace_back(1);

    for(auto e = int_vector.begin() ; e != int_vector.end() ; ++e) cout << *e << " ";
    cout << endl;

    //

    queue<pair<int,int>> pair_queue;
    pair_queue.push(make_pair(1,2));
    pair_queue.emplace(1,2);
    while(! pair_queue.empty()) 
    {
        cout << "(" << pair_queue.front().first << "," << pair_queue.front().second << ") ";
        pair_queue.pop();
    }
    cout << endl;

    //

    map<int,int> dictionary;
    dictionary.insert(make_pair(1,2));
    dictionary.emplace(2,3);
    for(auto e = dictionary.begin() ; e != dictionary.end() ; ++e) cout << "[" << e->first << ":" << e->second << "] ";
    cout << endl;

    cout << dictionary.insert(make_pair(1,5)).second << endl;
    cout << dictionary.emplace(2,5).second << endl;
    cout << dictionary.emplace(3,5).second << endl;
    for(auto e = dictionary.begin() ; e != dictionary.end() ; ++e) cout << "[" << e->first << ":" << e->second << "] ";
    cout << endl;

    dictionary[1] = 10;
    dictionary[10] = 100;
    for(auto e = dictionary.begin() ; e != dictionary.end() ; ++e) cout << "[" << e->first << ":" << e->second << "] ";
    cout << endl;

    dictionary.erase(1);
    for(auto e = dictionary.begin() ; e != dictionary.end() ; ++e) cout << "[" << e->first << ":" << e->second << "] ";
    cout << endl;

}
