#include <iostream>
#include <string>
#include <array>
using namespace std;
/*array vector_n(int n){
array <int, n-1> a;
int i=0;
while (i<=n){
	a[i]=n-i;
	i=i+1;
}
return a;
}*/
int main(int argc, char* argv[]){
int n=atoi(argv[1]);
/*array <int, n-1> a=vector_n(n);
int i=0;
while (i<=n-1){
	n=n*a[i];
	i=i+1;
	}
cout << n << "\n";*/
int i=1;
int j=1;
while (i<=n){
	int k=i*j;
	j=k;
	i=i+1;
		}
cout << j << "\n";
return 0;
}
