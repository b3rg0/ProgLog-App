#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 20;
    int c = a * b; 
    a=4+b;
    c=3;
    b=a/2;
    std::cout << "c = " << b << std::endl;
    
    return 0;
}