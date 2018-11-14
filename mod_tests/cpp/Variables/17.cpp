#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10 - a;
    b=2;
    c = a + a;
    
    std::cout << "c = " << b << std::endl;
    
    return 0;
}