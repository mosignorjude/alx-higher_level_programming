#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to the head of the linked list
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *temp, *nextNode;

	if (*head == NULL)
		return (NULL);

	temp = *head;
	*head = 0;
	while (temp != NULL)
	{
		nextNode = temp->next;
		temp->next = *head;
		*head = temp;
		temp = nextNode;
	}
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *new;

	if (*head == NULL)
		return (1);
	new = *head;
	if (reverse_listint(head) == NULL)
		return (1);
	while ((*head != NULL) && (new != NULL))
	{
		if ((*head)->n != new->n)
			return (0);
		*head = (*head)->next;
		new = new->next;
	}
	return (1);
}
