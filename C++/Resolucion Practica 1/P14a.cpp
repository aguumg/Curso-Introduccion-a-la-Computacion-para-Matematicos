#include <iostream>
#include <string>
#include <array>
using namespace std;
/*int potencia(int x, int y){
int n=1;
while (y!=0){
	n=n*x;
	y=y-1;
	}
return n;
}
int largo_array(int x){
int i=2;
while (potencia(2,i)<=x){
	i = i+1;
	}
return i;
}*/


int main(int argc, char* argv[]){
int x=5;
int var;
int i=0;
string a;
while (x>=2){
	a[i]=x%2;
	i=i+1;
	x=x/2;
	}
a[i]=x;
i=0;
while (i<=a.size()){
	cout << a[i];
	i=i+1;
	}
cout << "\n";
return 0;
}
