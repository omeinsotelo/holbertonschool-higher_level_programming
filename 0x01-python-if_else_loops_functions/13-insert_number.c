#include "lists.h"
/**
 * insert_node - function a new node
 * @head: poiter to a poiter head
 * @number: number to insert
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tail, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	tail = *head;
	for (; tail->next != NULL; tail = tail->next)
	if (tail->next->n > number)
		break;
	new->next = tail->next;
	tail->next = new;
	return (new);
}
