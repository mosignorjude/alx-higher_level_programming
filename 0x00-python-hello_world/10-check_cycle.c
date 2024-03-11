#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list is a cycle
 * @list: pointer to the list
 *
 * Return: 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	current = list;
	temp = current;

	while (current != NULL)
	{
		current = current->next;
		if (current == temp)
			return (1);
	}
	return (0);
}

