#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main()
{
	pid_t my_ppid;
	my_ppid = get_ppid; 

	printf("ppid is: %d\n", my_ppid);
	return 0;
}
