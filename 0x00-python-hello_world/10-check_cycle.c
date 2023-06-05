#include "lists.h"

/**
  *check_cycle - Checks if there is a cycle in a linked list
  *@list: The list to check
  *
  *Return: 1 if cycle exist or 0 if not
  *
  */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
			return (1);
	}
	return (0);
}
