//G5 5430 AC
#include <iostream>
#include <string>
#include <algorithm>
#include <deque>
#include <sstream>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    while(T--)
    {
        //입력
        string p;
        cin >> p;
        cin.ignore();

        int n;
        scanf("%d", &n);

        string arr_input;
        cin >> arr_input;
        cin.ignore();

        //문자열 처리
        deque<int> deq;
        bool is_left = true;
        bool is_error = false;
        
        arr_input = arr_input.substr(1, arr_input.length()-2);

        istringstream iss(arr_input);
        string buffer;
        
        while(getline(iss, buffer, ','))
        {
            deq.push_back(stoi(buffer));
        }
        
        //연산 수행
        for (string::iterator operation = p.begin(); operation != p.end(); ++operation)
        {
            // R: 뒤집기
            if (*operation == 'R')
            {
                is_left = !is_left;
            }

            // D: 삭제
            else
            {
                if (deq.empty())
                {
                    is_error = true;
                    break;
                }
                else
                {
                    if (is_left) deq.pop_front();
                    else         deq.pop_back();
                }
            }
        }

        //출력
        if(is_error) printf("error\n");
        else
        {
            if (! is_left) reverse(deq.begin(), deq.end());
            printf("[");
            if(! deq.empty())
            {
                for (auto e = deq.begin() ; e < deq.end() - 1 ; ++e)
                {
                    printf("%d,", *e);
                }
                printf("%d", deq.back());
            }
            printf("]\n");
        }
    }
}
