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

person * hash_table
unsigned int hash(char *name)
{
	int length = strnlen(name, MAX_NAME);
	unsigned int hash_value = 0;
	for (int i=0; i<length; i++)
	{
		hash_value += name[i];
		hash_value = (hash_value * name[i] % TABLE_SIZE);
	}
	return hash_value;
}
void init_hash_table()
{
	for (int i=0; i<TABLE_SIZE; i++)
	{
		hash_table[i] = NULL;
	}
}

void print_table()
{
	for (int i=0; i< TABLE_SIZE; i++)
	{
		if(hash_table[i] ==NULL)
		{
			printf("\t%i\t---\n");
		}
		else{
			printf("\t%i\t%s\n", hash_table[i]->name);
		}
	}
}
int main() 
{
	init_hash_table();
	print_table();
/**
	printf("Jacob => %u\n", hash("Jacob"));	
	printf("Stan => %u\n", hash("Stan"));
	printf("Mike => %u\n", hash("Mike"));
	printf("Mary => %u\n", hash("Mary"));
*/
	return 0;
}
