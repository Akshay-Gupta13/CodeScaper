#include <iostream>

using namespace std;

void swapNumbers(int& a, int& b) {
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
}

int main() {
    int num1, num2;
 
    cin >> num1;
    cin >> num2;

    swapNumbers(num1, num2);

    cout << num1<<" " << num2 << endl;
   

    return 0;
}
