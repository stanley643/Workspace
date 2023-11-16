#include "function_pointers.h"
/**
 * print_name - prints a given name
 * @name: name to be printed
 * @f:  pointer to fxn
 *
 * void *fn_ptr(char, void)
 * Return: void
 */

void print_name(char *name, void (*f)(char *))
{
	if (name == NULL || f == NULL)
		return;
	f(name);
}


