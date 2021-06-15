#include <iostream>
#include <string>
#include <array>
using namespace std;
int main(int argc, char* argv[]){
int n=atoi(argv[1]);
float i=1;
float j=0;
while (i<=n){
	float k=(1/i)+j;
	j=k;
	i=i+1;
}
cout << j << "\n";
return 0;
}
