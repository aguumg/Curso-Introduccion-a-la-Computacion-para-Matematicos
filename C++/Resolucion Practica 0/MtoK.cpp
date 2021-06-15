#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
int main(int argc, char* argv[]){
float Mill=atof(argv[1]);
float Km;
Km= Mill*1.61;
printf("\t%.2f millas equivalen a %.2f kilometros.\n", Mill, Km);
return 0;
}
