#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 *print_python_list - Prints basic info about python
 *@p: A PyObject
 *Return: Nothing
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t sizze, allocates, idx;
	const char *typ;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	sizze = var->ob_size;
	allocates = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", sizze);
	printf("[*] Allocated = %ld\n", allocates);

	for (idx = 0; idx < sizze; idx++)
	{
		typ = list->ob_item[idx]->ob_type->tp_name;
		printf("Element %ld: %s\n", idx, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(list->ob_item[idx]);
		else if (strcmp(typ, "float") == 0)
			print_python_float(list->ob_item[idx]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python
 * @p: A PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sizze, idx;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		sizze = 10;
	else
		sizze = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", sizze);
	for (idx = 0; idx < sizze; idx++)
	{
		printf("%02hhx", bytes->ob_sval[idx]);
		if (idx == (sizze - 1))
			printf("\n");
		else
			printf(" ");
	}
}
/**
 * print_python_float - Prints basic info about Python
 * @p: A PyObject
 * Return: Nothing
 */

void print_python_float(PyObject *p)
{
	char *buff = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;
	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}

