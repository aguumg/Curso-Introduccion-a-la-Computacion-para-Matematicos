#include <iostream>
#include <string>
#include <array>
using namespace std;

int main(int argc, char* argv[]){
int n=atoi(argv[1]);
int j=1;
int i=1;
while (j<=n){
	while (i<=j){
		cout << "*";
		i=i+1;
		}
	cout << "\n";
	j=j+1;
	i=1;
}
return 0;
}
