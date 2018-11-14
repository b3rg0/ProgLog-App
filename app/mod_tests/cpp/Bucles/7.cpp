#include <iostream>

int main(int argc, char *argv[]) {
    int a=5;
    int b=0;
    for(int i=b; i<a; i++){
    	a=a-i;
    	b=i;	
    }
    std::cout << "b = " << b << std::endl;    
    return 0;
}