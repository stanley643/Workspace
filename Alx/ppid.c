#include<stdio.h>
#include<stdlib.h>
#include<unistsd.h>

int main()
{
	pid_t my_ppid;
	my_ppid = get_ppid; 

	print("ppid is: %d\n", my_ppid);
	return 0;
}
