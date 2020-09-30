#include "holberton.h"
/**
* rev_string - prints a string in reverse
* @s: takes in an char array
* Return: none
*/
void rev_string(char *s)
{
	int i, count = 0;
	char temp;

	while (s[count] != '\0')
		count++;
	count--;

	for (i = 0; i < count; count--, i++)
	{
		temp = s[i];
		s[i] = s[count];
		s[count] = temp;
	}
}
