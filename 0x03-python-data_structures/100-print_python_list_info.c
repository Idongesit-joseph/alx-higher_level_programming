#include <Python.h>

/**
 * print_python_list_info - aaaaaaa
 * @p: aaaa
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size= Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the python List = %d\n",size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = Pylist_Getitem(p, i);
		printf("%s\n, Py_TYPE(obj)->tp_name);
	}
}
