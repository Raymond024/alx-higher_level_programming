#include "lists.h"
/**
 * check_cycle - function checks for cycle in list
 * @list: pointer to the linked list
 * Return: 0 if no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *p;
	listint_t *before;

	p = list;
	before = list;
	while (list && p && p->next)
	{
		list = list->next;
		p = p->next->next;

		if (list == p)
		{
			list = before;
			before =  p;
			while (1)
			{
				p = before;
				while (p->next != list && p->next != before)
				{
					p = p->next;
				}
				if (p->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
