---
# layout: page
# title: "Coverage Tests - Project 1A: Linked List Deque"
# categories: proj
# released: true
# searchable: false

layout: page
title: "Coverage Tests - Project 1A: Linked List Deque 61B"
nav_order: 0
parent: >-
  Project 1A: LinkedListDeque61B
grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
  Project 1 Flags.
released: true
---

### Flags for add tests

- "add_first_from_empty": Check that `addFirst` works on an empty deque.
- "add_last_from_empty": Check that `addLast` works on an empty deque.
- "add_first_nonempty": Check that `addFirst` works on a non-empty deque.
- "add_last_nonempty": Check that `addLast` works on a non-empty deque.

### Flags for add after remove tests

- "add_first_after_remove_to_empty": Add some elements to a deque and remove them all, then check that `addFirst` still works.
- "add_last_after_remove_to_empty": Add some elements to a deque and remove them all, then check that `addLast` still works.

### Flags for remove tests

- "remove_first": Check that `removeFirst` works.
- "remove_last": Check that `removeLast` works.
- "remove_first_to_empty": Add some elements to a deque and remove almost all of them. Check that removing the last element with `removeFirst` works.
- "remove_last_to_empty": Add some elements to a deque and remove almost all of them. Check that removing the last element with `removeLast` works.
- "remove_first_to_one": Add some elements to a deque and remove almost all of them. Check that removing the second to last element with `removeFirst` works.
- "remove_last_to_one": Add some elements to a deque and remove almost all of them. Check that removing the second to last element with `removeLast` works.

### Flags for get tests

- "get_valid": Check that `get` works on a valid index.
- "get_oob_large": Check that `get` works on a large, out of bounds index.
- "get_oob_neg": Check that `get` works on a negative index.
- "get_recursive_valid": Check that `getRecursive` works on a valid index.
- "get_recursive_oob_large": Check that `getRecursive` works on a large, out of bounds index.
- "get_recursive_oob_neg": Check that `getRecursive` works on a negative index.

### Flags for size tests

- "size": Check that `size` works.
- "size_after_remove_to_empty": Add some elements to a deque and remove them all, then check that `size` still works.
- "size_after_remove_from_empty": Remove from an empty deque, then check that `size` still works.

### Flags for isEmpty tests

- "is_empty_true": Check that isEmpty works on an empty deque.
- "is_empty_false": Check that isEmpty works on a non-empty deque.

### Flags for toList tests

- "to_list_empty": Check that toList works with empty LinkedListDeque61B.
- "to_list_nonempty": Check that toList works with non-empty LinkedListDeque61B.
