#include <iostream>
#include <string>
#include <array>
using namespace std;
string divisores(int n){
string a;
int i=1;
int j=0;
while (i<n){
	if (n%i==0){
		a[j]=i;
		j=j+1;
		}
	i=i+1;
}
return a;
}

int sum(string a){
int i=1;
int n=a[0];
while (i<=a.size()){
	n=n+a[i];
	i=i+1;
	}
return n;
}

int main(int argc, char* argv[]){
int n=10;
string a;
if (n==sum(a)){
	cout << n << " es perfecto" << "\n";
	}
		else{
			cout << n << " no es perfecto" << "\n";
		}
return 0;
}
