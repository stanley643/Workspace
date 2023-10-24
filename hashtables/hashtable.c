#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<stdint.h>
#include<stdbool.h>

#define MAX_NAME 256
#define TABLE_SIZE 10

typedef struct {
	char name[MAX_NAME];
	int age;

}person;

usigned int hash(char *name)
{
	return 5;
}

int main() 
{
	printf("Jacob => %u\n", hash("Jacob"));	
	printf("Stan => %u\n", hash("Stan"));
	printf("Mike => %u\n", hash("Mike"));
	printf("Mary => %u\n", hash("Mary"));

	return 0;
}
