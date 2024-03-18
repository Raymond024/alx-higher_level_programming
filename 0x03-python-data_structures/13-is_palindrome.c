#include "lists.h"

/**
 * rev_listint - function reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void rev_listint(listint_t **head)
{
	listint_t *before = NULL;
	listint_t *after = *head;
	listint_t *next = NULL;

	while (before)
	{
		next = after->next;
		after->next = before;
		before = after;
		after = next;
	}

	*head = before;
}

/**
 * is_palindrome - function checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	rev_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
