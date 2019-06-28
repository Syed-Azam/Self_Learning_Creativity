<u>**Python's variable passing style**</u>:

Objects are allocated on the heap and pointers to them can be passed around anywhere.

- When you make an assignment such as `x = 1000`, a dictionary entry is created that maps the string "x" in the current name space to a pointer to the integer object containing one thousand.
- When you update "x" with `x = 2000`, a new integer object is created and the dictionary is updated to point at the new object. The old one thousand object is unchanged (and may or may not be alive depending on whether anything else refers to the object).
- When you do a new assignment such as `y = x`, a new dictionary entry "y" is created that points to the same object as the entry for "x".
- Objects like strings and integers are *immutable*. This simply means that there are no methods that can change the object after it has been created. For example, once the integer object one-thousand is created, it will never change. Math is done by creating new integer objects.
- Objects like lists are *mutable*. This means that the contents of the object can be changed by anything pointing to the object. For example, `x = []; y = x; x.append(10); print y` will print `[10]`. The empty list was created. Both "x" and "y" point to the same list. The *append* method mutates (updates) the list object (like adding a record to a database) and the result is visible to both "x" and "y" (just as a database update would be visible to every connection to that database).