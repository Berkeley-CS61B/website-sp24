---
layout: page
title: >-
  FAQ
parent: >-
  Lab 06: BSTMap
grand_parent: Labs
has_right_toc: true
released: true
---

### Error relating to iterator

If you get this error:

```
java: bstmap.BSTMap is not abstract and does not override abstract method iterator() in java.lang.Iterable
```

You need to put the following method in your BSTMap:

```
public Iterator<K> iterator() {
    throw new UnsupportedOperationException();
}
```

Why does the BSTMap need this? It's because the `Map61B` interface extends `Iterable`, which means that anything that implements `Map61B` must have the `Iterable` methods as well.

### Wrong size in treeTest

If you're erroring on this line in `treeTest`:

```
assertThat(b.size()).isEqualTo(5)
```

Keep in mind that `put` doesn't always add a new value to the tree. If `put` is called with an existing key, it should just update the value, which shouldn't change the size.
