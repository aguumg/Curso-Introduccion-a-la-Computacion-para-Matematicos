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
}

int main(int argc, char* argv[]){
array <int, n-1> a=vector_n(n);
int i=0;
while (i<=n-1){
	n=n+a[i];
	i=i+1;
	}
cout << j << "\n";
return 0;
}*/

int main(int argc, char* argv[]){
int n=10;
int i=0;
int j=0;
while (i<=n){
	int k=i+j;
	j=k;
	i=i+1;
}
cout << j << "\n";
return 0;
}
