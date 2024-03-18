#include <stdio.h>
#include <stdlib.h>
#include <stdnoreturn.h>
#include "lists.h"

/**
 * add_nodeint - adds a new node at the beginning of a linked list
 * @head: pointer to a pointer to the first node
 * @n: value of the integer in the node
 *
 * Return: address of the new node or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		new->next = current;
		current = new;
	}
	return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	listint_t *current

	if (*head == NULL)
		return (1);
    current = *head;
	while (current != NULL)
	{
		temp = add_nodeint(current, current->n);
		current = current->next;
	}

}
