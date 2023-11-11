#include "main.h"

void free_dog(dog_t *d)
{
	if (d != NULL)
	{
		free(d);
		d = NULL;
	}

}
