#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10/b;
    a= a + c;

    if(b%2==0){
    	c=15;
        a=a;
    }
    else if(b%3==0){
    	c='15';
        a=b;
    }
    else{
    	c=15;
        a=c;
    }
    std::cout << "a = " << a << std::endl;	  
    
    return 0;
}