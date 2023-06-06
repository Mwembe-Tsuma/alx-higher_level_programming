#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: The integer
 * @next: points to the next node in linked list
 *
 * Description: singly linked list node struct
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
