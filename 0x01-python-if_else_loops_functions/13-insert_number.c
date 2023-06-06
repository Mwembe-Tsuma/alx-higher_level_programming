#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  *insert_node - Insert a number into a linked list
  *@head: Pointer to the head node
  *@number: The number to be inserted
  *
  *Return: Null if fails or pointer to the new node
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nod = *head;
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (nod == NULL || nod->n >= number)
	{
		newNode->next = nod;
		*head = newNode;
		return (newNode);
	}
	while (nod && nod->next && nod->next->n < number)
		nod = nod->next;
	newNode->next = nod->next;
	nod->next = newNode;

	return (newNode);
}
