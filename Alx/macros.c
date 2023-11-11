#include "main.h"

#define SIZE 5
#define PRODUCT(X, Y) X * Y

int main(int argc, char *argv[])
{
	int arr[SIZE];
	int i;
	int a =2, b = 6;

	for (i = 0; i < SIZE; i++)
	{
		arr[i] = i * 2;
	}

	for (i = 0; i < SIZE; i++)
	{
		printf("%d\n", arr[i]);
	}
	printf("product is %d\n", PRODUCT(a, b));
	return 0;
}
