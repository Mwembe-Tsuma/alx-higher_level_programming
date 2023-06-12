#include "lists.h"

listint_t *rev_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
  *rev_listint - Reverse a linked list
  *@head: Pointer to head node
  *
  *Return: A pointer to reversed list
  */

listint_t *rev_listint(listint_t **head)
{
	listint_t *newnode = *head, *next, *prevnode = NULL;

	while (newnode)
	{
		next = newnode->next;
		newnode->next = prevnode;
		prevnode = newnode;
		newnode = next;
	}
	*head = prevnode;
	return (*head);
}
/**
  *is_palindrome- Check for palindrome
  *@head: Pointer to head node
  *
  *Return: 1 if palindrome or 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reversed, *midnode;
	size_t size = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (j = 0; j < (size / 2) - 1; j++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	reversed = rev_listint(&temp);
	midnode = reversed;
	temp = *head;

	while (reversed)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	rev_listint(&midnode);
	return (1);
}
