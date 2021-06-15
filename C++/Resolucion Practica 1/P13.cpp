#include <iostream>
#include <string>
using namespace std;

int main(char* argv[]){
int n=atoi(argv[1]); /* El primer argumento n, es para enlistar de 0 a n */
cout << "El argumento es: " << n << "\n";
int i=1;
cout << "Lista completa:" << "\n";
while (i<=n){
	cout << i << "\n";
	i=i+1;
	}
int m=atoi(argv[2]); /*El segundo argumento m, es para enlistar los primeros m 			impares */
cout << "El argumento es: " << m << "\n";
cout << "Lista primeros " << m << " impares:" << "\n";
i=1;
while (i<=2*m){
if (i%2!=0){
	cout << i << "\n";
	i=i+1;
	}
	else{
	i=i+1;
	}
} 
return 0;
}
