#include<cstdio>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = n - 1; j > i; j--) {
			printf(" ");
		}
		for (int j = 0; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}

	for (int i = n; i < 2 * n - 1; i++) {
		for (int j = n - 1; j < i; j++) {
			printf(" ");
		}
		for (int j = i; j < 2 * n - 1; j++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}