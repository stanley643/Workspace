#include "main.h"

typedef struct
{
	char name[20];
	int age;
	char country[20];
}Students ;
int main()
{
	Students student1;
	Students student2;
	Students student3= {"Mary", 18, "Kenya"};

	strcpy(student1.name, "Stanley");
	student1.age = 23;
	strcpy(student1.country, "Kenya");

	strcpy(student2.name, "Michael");
        student2.age = 14;
        strcpy(student2.country, "Kenya");

	//printf("Student 1 name is %s and is %d years old from %s\n", student1.name, student1.age, student1.country);

	//printf("Student 2 name is %s and is %d years old from %s\n", student2.name, student2.age, student2.country);

	//printf("Student 3 name is %s and is %d years old from %s\n", student3.name, student3.age, student3.country);
	Students students[] = {student1, student2, student3};
	for (int i = 0; i < sizeof(students) / sizeof(students[0]); i++)
	{
		printf("%s\t", students[i].name);
		printf("%d\t", students[i].age);
		printf("%s\n", students[i].country);
	}
	return 0;
}
