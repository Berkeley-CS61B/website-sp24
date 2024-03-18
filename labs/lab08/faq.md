---
layout: page
title: >-
  FAQ - Lab08 
parent: >-
  Lab 08: Hashmaps
grand_parent: Labs
has_right_toc: true
released: true
---

### I'm getting a "Generic array creation" error.

Be sure to instantiate your buckets table with `new Collection[size]` or `(Collection<Node>[]) new Object[size]`!

### Failing edge cases

The `Bee` class has some strange `equals` and `hashCode` implementations. If you're stuck on this test, use the debugger to see what values are expected from the reference map, which is Java's built-in HashMap. Walking through the expected behavior by hand may help as well.

Some things to think about:

The reference map has some (maybe) unexpected behaviors. _Why_ does the reference map behave the way it does (remember `equals` and `hashCode`!)?
Does your map behave the same way?

### I'm running into issues with resizing and getting expected to be greater than this value, but was this value.

For example, you might be seeing this error message:

```shell
expected to be greater than: 16
but was                    : 16
```

If you're running into this issue, a common problem is how the load factor is being calculated. The load
factor can be found by dividing the total number of elements in the hashmap divided by the total number
of buckets - both values are commonly stored as integers, but remember, the load factor is a double.
How might integer division cause an error?
