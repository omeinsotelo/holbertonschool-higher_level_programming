#include "lists.h"
/**
 * check_cycle- checks if a singly linked list has a cycle in it
 * @list: the pointer to list
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *list1, *list2;

	list1 = list;
	list2 = list;
	while (list1 != NULL && list2 != NULL && list1->next != NULL)
	{
		list1 = list1->next;
		list2 = list2->next->next;
		if (list1 == list2)
			return (1);
	}
	return (0);
}
