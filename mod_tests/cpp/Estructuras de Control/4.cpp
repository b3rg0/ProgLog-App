#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10;
    int c = a;
    if(5>2){
    	a = c + 1;
    	std::cout << "c = " << c << std::endl;	    	
    }    
    else{
    	std::cout << "a = " << a << std::endl;
    }    
    
    return 0;
}