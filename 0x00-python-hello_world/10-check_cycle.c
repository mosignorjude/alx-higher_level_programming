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
	listint_t *trav_ptr; /*traversing pointer*/
	listint_t *current;  /*pointer to the current node*/

	trav_ptr = list;
	current = list;

	if (list == NULL)
		return (0);
	while (trav_ptr != NULL && trav_ptr->next != NULL)
	{
		current = current->next;
		trav_ptr = trav_ptr->next->next;
		if (current == trav_ptr)
			return (1);
	}
	return (0);
}

