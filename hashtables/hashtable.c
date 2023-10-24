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

unsigned int hash(char *name)
{
	int length = strnlen(name, MAX_NAME);
	unsigned int hash_value = 0;
	for (int i=0; i<length; i++)
	{
		hash_value += name[i];
		hash_value = hash_value * name[i];
	}
	return hash_value;
}

int main() 
{
	printf("Jacob => %u\n", hash("Jacob"));	
	printf("Stan => %u\n", hash("Stan"));
	printf("Mike => %u\n", hash("Mike"));
	printf("Mary => %u\n", hash("Mary"));

	return 0;
}
