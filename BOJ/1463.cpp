#include<cstdio>
#include<algorithm>
using namespace std;

int arr[1000001];

int main() {
	int n;
	arr[1] = 0;
	arr[2] = 1;
	arr[3] = 1;
	scanf("%d", &n);
	for (int i = 4; i <= n; i++) {
		arr[i] = arr[i - 1] + 1;
		if (i % 2 == 0) {
			arr[i] = min(arr[i - 1] + 1, arr[i / 2] + 1);
		}
		if (i % 3 == 0) {
			arr[i] = min(arr[i - 1] + 1, arr[i / 3] + 1);
		}
	}
	printf("%d\n", arr[n]);

	return 0;
}