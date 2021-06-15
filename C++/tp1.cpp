#include <iostream>
#include <string>
#include <array>
using namespace std;

int main(int argc, char* argv[]){
int n=atoi(argv[1]);
int i=2;
while (i<n){
	if(n%i==0){
	cout << n << " no es primo" << "\n";
	return 0;
	}
	i=i+1;
}
cout << n << " es primo" << "\n";
return 0;
}
