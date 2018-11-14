#include <iostream>

int main(int argc, char *argv[]) {
    int a=0;
    int b=2;

    do{
    	b=2*b;    	
    }while(b>a);

    std::cout << "b = " << b << std::endl;    
    return 0;
}