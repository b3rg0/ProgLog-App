#include <iostream>

int main(int argc, char *argv[]) {
    int a=5;
    int b=0;

    while(b<=a){
        b+=1;// o b = b + 1;
    }
    std::cout << "b = " << b << std::endl;    

    return 0;
}