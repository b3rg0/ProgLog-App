#include <iostream>

int main(int argc, char *argv[]) {
    int a=1;
    int b=2;

    for(int i=0; i<10; i++){
    	a=b-i;
    	b=b+i;    	
    }

    std::cout << "a = " << a << std::endl;  
    return 0;
}