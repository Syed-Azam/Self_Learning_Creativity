## When is “i += x” different from “i = i + x” in Python?

This depends entirely on the object `i`.

`+=` calls the [`__iadd__` method](http://docs.python.org/2/reference/datamodel.html#object.__iadd__) (if it exists -- falling back on `__add__` if it doesn't exist) whereas `+`calls the [`__add__` method](http://docs.python.org/2/reference/datamodel.html#object.__add__)1 or the [`__radd__` method in a few cases](http://docs.python.org/2/reference/datamodel.html#object.__radd__)2.

From an API perspective, `__iadd__` is supposed to be used for modifying mutable objects *in place*(returning the object which was mutated) whereas `__add__` should return a *new instance* of something. For *immutable* objects, both methods return a new instance, but `__iadd__` will put the new instance in the current namespace with the same name that the old instance had. This is why

```py
i = 1
i += 1
```

seems to increment `i`. In reality, you get a new integer and assign it "on top of" `i` -- losing one reference to the old integer. In this case, `i += 1` is exactly the same as `i = i + 1`. But, with most mutable objects, it's a different story:

As a concrete example:

```py
a = [1, 2, 3]
b = a
b += [1, 2, 3]
print a  #[1, 2, 3, 1, 2, 3]
print b  #[1, 2, 3, 1, 2, 3]
```

compared to:

```py
a = [1, 2, 3]
b = a
b = b + [1, 2, 3]
print a #[1, 2, 3]
print b #[1, 2, 3, 1, 2, 3]
```

notice how in the first example, since `b` and `a` reference the same object, when I use `+=` on `b`, it actually changes `b` (and `a` sees that change too -- After all, it's referencing the same list). In the second case however, when I do `b = b + [1, 2, 3]`, this takes the list that `b` is referencing and concatenates it with a new list `[1, 2, 3]`. It then stores the concatenated list in the current namespace as `b` -- With no regard for what `b` was the line before.

