#include <Python.h>

/**
  *print_python_list_info- Prints basic info about Python
  *@p: PyObject list
  *
  */

void print_python_list_info(PyObject *p)
{
	int size, allocates, j;
	PyObject *obj;

	size = Py_SIZE(p);
	allocates = ((PyListObject *)p)->allocated;
	
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocates);

	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);
		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
