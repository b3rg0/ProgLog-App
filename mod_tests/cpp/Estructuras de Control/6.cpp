#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10 - b;

    if(c%2==0){
    	c=12;
    }
    else if(c%3==0){
    	c='11';
    }
    else{
    	c=11;
    }
    std::cout << "c = " << c << std::endl;	
    
    
    return 0;
}