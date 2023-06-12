#include <Python.h>

/**
  *print_python_list_info- Prints basic info about Python
  *@p: PyObject list
  *
  */

void print_python_list_info(PyObject *p)
{
	int size, j, allocate;
	PyObject *obj1;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;
	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (j = 0; j < size; j++)
	{
		printf("Element %d:", j);
		obj1 = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj1)->tp_name);
	}
}
