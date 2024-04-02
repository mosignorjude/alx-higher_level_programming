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
	listint_t *current, *nextNode;
	listint_t *prev = NULL;

	if (*head == NULL)
		return (NULL);

	current = *head;
	while (current != NULL)
	{
		nextNode = current->next;/* temporarily store next node */
		current->next = prev;/* changes the next value to the previous value */
		prev = current;/* replace previous with current value */
		/*successfully swapped next to become prev and prev to become current*/
		current = nextNode;/* move to the next node*/
	}
	*head = prev;
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

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	new = *head;
	reverse_listint(&new);
	print_listint(new);
	while ((*head != NULL) && (new != NULL))
	{
		if ((*head)->n != new->n)
			return (0);
		*head = (*head)->next;
		new = new->next;
	}
	return (1);
}
