#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: node of the list
 * @number: value to be insert_node
 *
 * Return: address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	int i = 0;

	if (*head == NULL)
		return (NULL);
}
