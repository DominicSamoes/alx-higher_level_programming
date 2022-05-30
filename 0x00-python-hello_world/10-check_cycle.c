#include "lists.h"

/**
 * check_cycle - Checks for cycle in a singly-linked list.
 * @list: pointer to singly-linked list
 * Return: 0 if there is no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *pn;
	listint_t *pnn;

	if (list == NULL || list->next == NULL)
		return (0);

	pn = list->next;
	pnn = list->next->next;

	do {
		if (pn == pnn)
			return (1);

		pn = pn->next;
		pnn = pnn->next->next;
	} while (pn && pnn && pnn->next);

	return (0);
}
