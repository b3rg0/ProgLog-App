#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = a + a;
    c=b*2;
    b=1;
    std::cout << "c = " << (a+c) << std::endl;
    
    return 0;
}