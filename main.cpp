#include <iostream>
#include <cstdio>



extern "C" {
    int add(int a, int b)
    {
        return a+b;
    }


    int multiplicate(int a, int b)
    {
        return a*b;
    }
}