//G4 10830 행렬 제곱
#include <iostream>
using namespace std;

//
long long n, b;
int arr[5][5];
int res[5][5];
int temp[5][5];

//
void matmul(int mat1[5][5], int mat2[5][5])
{
    for(int i = 0 ; i < n ; i++)
    {
        for(int j = 0 ; j < n ; j++)
        {
            temp[i][j] = 0;
            for(int k = 0 ; k < n ; k++) temp[i][j] += mat1[i][k] * mat2[k][j];
            temp[i][j] %= 1000;
        }
    }

    for(int i = 0 ; i < n ; i++)
    {
        for(int j = 0 ; j < n ; j++) mat1[i][j] = temp[i][j];
    }
}

//

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> b;

    for(int i = 0 ; i < n ; i++)
    {
        for(int j = 0 ; j < n ; j++) cin >> arr[i][j];
        res[i][i] = 1;
    }
    //

    while(b)
    {
        if(b%2) matmul(res, arr);
        matmul(arr, arr);
        b /= 2;
    }

    //
    for(int i = 0 ; i < n ; i++)
    {
        for(int j = 0 ; j < n ; j++) cout << res[i][j] << " ";
        cout << endl;
    }
}
