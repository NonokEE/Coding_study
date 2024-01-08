//G5 11729 하노이 탑 이동 순서
#include <iostream>
using namespace std;

void hanoi(int count, int left, int middle, int right)
{
    if(!count) return;
    hanoi(count - 1, left, right, middle);
    printf("%d %d\n",left, right);
    hanoi(count - 1, middle, left, right);
}

int main()
{
    int N;
    scanf("%d", &N);
    
    printf("%d\n",(1<<N)-1);
    hanoi(N, 1,2,3);

    return 0;
}
