---
layout: page
title: >-
  Homework 0B: Data Structures
nav_order: 1
# nav_exclude: true
parent: Homework 0
grand_parent: Homeworks
has_children: true
has_toc: false
has_right_toc: true
description: >-
  Homework 0A spec.
released: false
---
## Language Constructs

### Types

In Java, there are two kinds of types: primitive types and reference types.
Primitive types are lowercase, and we named the ones that we care about in
[Part A](../hw0a/index.md#types): `boolean`, `int`, `char`, `double`.
Pretty much every other type is a reference type, such as `String`. If a type
starts with a capital letter, it is likely a reference type.

You will learn more about the distinction between primitive and reference types
in Lecture 4, but for this homework, you will need to know that each primitive
has a corresponding reference type (`Boolean`, `Integer`, `Character`,
`Double`). If you are using "generics" to declare a data structure, you _must_
use the reference type. You can seamlessly convert between a primitive type
and its reference type.

#### `null`

Java also has `null`, which is the approximate equivalent of `None` in Python.
Any reference type can be assigned a value of `null`. If we try to access an
instance member or call an instance method from a value of `null`, we will see
an error called a `NullPointerException`.

### Arrays (fixed-size)

Java arrays are a lot like Python lists. However, Java arrays are _fixed-size_,
so we can't add or remove elements (that is, no `append`, `remove`, etc.).

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
zeroedLst = [0, 0, 0]
lst = [4, 7, 10]
lst[0] = 5
print(lst[0])
print(lst)
print(len(lst))
```

</td>
<td markdown="block">

```java
int[] zeroedArray = new int[3];
int[] array = {4, 7, 10};
array[0] = 5;
System.out.println(array[0]);
System.out.println(Arrays.toString(array));
System.out.println(array.length);
```

</td>
</tr>
</table>

- In `new int[3]`, the `int` is the type in the array; and `3` is the length.
  With this syntax, all elements take on their "default value". For `int`,
  this is 0.
- Arrays do not print nicely, for reasons beyond the scope of HW 0. To print
  an array, you can call `Arrays.toString(array)`.
- Arrays do not have a length _method_. It is an _instance variable_, so
  it does not have parentheses.
- Java does not support _negative indexing_ or _slicing_.

### Foreach Loop

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
lst = [1, 2, 3]
for i in lst:
    print(i)

```

</td>
<td markdown="block">

```java
int[] array = {1, 2, 3};
for (int i : array) {
    System.out.println(i);
}
```

</td>
</tr>
</table>

- Notice the type declaration of the iterating variable, as well as the usage
  of `:` instead of `in`.
- We can also use this syntax on certain other types, such as `List`s and
  `Set`s.

### Lists (resizable)

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
lst = []
lst.append("zero")
lst.append("one")
lst[0] = "zed"
print(l[0])
print(len(l))
if "one" in lst:
    print("one in lst")

for elem in lst:
    print(elem)

```

</td>
<td markdown="block">

```java
List<String> lst = new ArrayList<>();
lst.add("zero");
lst.add("one");
lst.set(0, "zed");
System.out.println(lst.get(0));
System.out.println(lst.size());
if (lst.contains("one")) {
    System.out.println("one in lst");
}
for (String elem : lst) {
    System.out.println(elem);
}
```

</td>
</tr>
</table>

- Java has the `List` interface. We largely use the
  [`ArrayList`][`ArrayList`] implementation.
- The `List` interface is _parameterized_ by the type it holds, using the
  angle brackets `<` and `>`.
- `List`s, again, do not support slicing or negative indexing.

[`ArrayList`]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html

### Sets

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
s = set()
s.add(1)
s.add(1)
s.add(2)
s.remove(2)
print(len(s))
if 1 in s:
    print("1 in s")

for elem in s:
    print(elem)

```

</td>
<td markdown="block">

```java
Set<Integer> set = new HashSet<>();
set.add(1);
set.add(1);
set.add(2);
set.remove(2);
System.out.println(set.size());
if (set.contains(1)) {
    System.out.println("1 in set");
}
for (int elem : set) {
    System.out.println(elem);
}
```

</td>
</tr>
</table>

- Java has the `Set` interface. There are two main implementations:
  [`TreeSet`][], and [`HashSet`][]. `TreeSet` keeps its elements in "sorted"
  order, and is "fast." In contrast, `HashSet` does not have a defined
  "order", but is (usually) **really** "fast."
- A `Set` canot contain duplicate items. If we try to add a duplicate item, it
  simply does nothing.

[`TreeSet`]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html
[`HashSet`]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashSet.html

### Dictionaries / Maps

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
d = {}
d["hello"] = "hi"
d["hello"] = "goodbye"
print(d["hello"])
print(len(d))
if "hello" in d:
    print("\"hello\" in d")

for key in d.keys():
    print(key)

```

</td>
<td markdown="block">

```java
Map<String, String> map = new HashMap<>();
map.put("hello", "hi");
map.put("hello", "goodbye");
System.out.println(map.get("hello"));
System.out.println(map.size());
if (map.containsKey("hello")) {
    System.out.println("\"hello\" in map");
}
for (String key : map.keySet()) {
    System.out.println(key);
}
```

</td>
</tr>
</table>

- Java has the `Map` interface. There are two main implementations:
  [`TreeMap`][], and [`HashMap`][]. Similarly to sets, `TreeMap` keeps its
  keys sorted and is fast; `HashMap` has no defined order and is (usually)
  **really** fast.
- In the angled brackets, we have the "key type" first, followed by the
  "value type".
- `Map`s cannot directly be used with the `:` for loop. Typically, we call
  `keySet` to iterate over a set of the keys.

[`TreeMap`]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeMap.html
[`HashMap`]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html

### Classes

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
```

</td>
<td markdown="block">

```java
public class Point {
    public int x;
    public int y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public Point() {
        this(0, 0);
    }
    public double distanceTo(Point other) {
        return Math.sqrt(
            Math.pow(this.x - other.x, 2) +
            Math.pow(this.y - other.y, 2)
        )
    }
    public void translate(int dx, int dy) {
        this.x += dx;
        this.y += dy;
    }
}
```

</td>
</tr>
</table>

We can use these classes as follows:

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
p1 = Point(5, 9)
p2 = Point(-3, 3)
print(f"Point 1: ({p1.x}, {p1.y})")
print("Distance:", p1.distanceTo(p2))
p1.translate(2, 2)
print(f"Point 1: ({p1.x}, {p1.y})")
```

</td>
<td markdown="block">

```java
Point p1 = new Point(5, 9);
Point p2 = new Point(-3, 3);
System.out.println("Point 1: ( " + p1.x
    + ", " + p1.y + ")");
System.out.println("Distance: "
    + p1.distanceTo(p2));
p1.translate(2, 2);
System.out.println("Point 1: ( " + p1.x
    + ", " + p1.y + ")");
```

</td>
</tr>
</table>

## Programs

Let's look at some Java programs that use data structures and classes. Here
are some simple ones that you might find yourself referring to if you forget
how to do something.

### Index of Minimum of a List of Numbers

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
def min_index(numbers):
    # Assume len(numbers) >= 1
    m = numbers[0]
    idx = 0
    for i in range(len(numbers)):
        if numbers[i] < m:
            m = numbers[i]
            idx = i
    return idx
```

</td>
<td markdown="block">

```java
public static int minIndex(int[] numbers) {
    // Assume numbers.length >= 1
    int m = numbers[0];
    int idx = 0;
    for (int i = 0; i < numbers.length; i++) {
        if (numbers[i] < m) {
            m = numbers[i];
            idx = i;
        }
    }
    return idx;
}
```

</td>
</tr>
</table>

<!-- TODO:
- Additional example programs
- Programming exercise spec
-->

## Exceptions

Lastly, let's look at how we can throw exceptions in Java compared to Python with previous example.

<table>
    <thead>
        <th>Python</th>
    </thead>
<tr>
<td markdown="block">

```python
def minIndex(numbers):
    if len(numbers) == 0:
        raise Exception("There are no elements in the list!")
    m = numbers[0]
    idx = 0

    ...

    return m
```

</td>
</tr>
    
    
<thead> 
<th>Java</th>
</thead>
<tr>

<td markdown="block">

```java
public static int minIndex(int[] numbers) {
    if (numbers.length == 0) {
        throw new Exception("There are no elements in the array!");
    }
    int m = numbers[0];
    int idx = 0;

    ...

    return m;
}
```

</td>
</tr>
</table>


## Programming Exercise

In order to get you more familiar with Java syntax and testing, there are couple of exercises for you to solve! After you complete the functions, we have provided couple tests for you to test. Although we have provided tests, you are welcomed to write your own too! Writing tests is not only crucial for this class but it is one of the most important skills to have in general. It reinforces our understanding of what specific method is supposed to do and allows us to catch edge cases! You will have more exercises for testing but we want you to get exposed early on.
    
While completing the assignment, you may need to use different data structures like `ArrayList` and `TreeMap`. In order to import these classes, if you hover over wherever you are using the data structures, IntelliJ will give you option to import it or you can do it manually by adding:
    
```
import java.util.ArrayList;
import java.util.TreeMap;
```
    

### JavaExercises
    
`ListExercises.java` has 4 different methods for you to complete:
    
-   `makeDice`: This method takes returns a *new* `array` of integers `[1, 2, 3, 4, 5, 6]`.
-   `takeOrder`: This method takes a list `String` and returns a *new* array containing the orders of the customer. If the customer is `Ergun`, you should return array of Strings `["beyti", "pizza", "hamburger", "tea"]` in that order. If the customer is `Erik`, you should retunrn array of Strings `["sushi", "pasta", "avocado", "coffee"]`. In any other case, return an empty array of size 3.
-   `findMinMax`: This method takes array `int[] array` and returns the result of `max - min` of the integers in that array.
-   `hailstone`: This method takes a `int n` and returns the numbers in hailstone sequence. If the character does not occur in any of the words, it should return 0. The hailstonce sequence: Pick a positive integer n as the start.If n is even, divide n by 2. If n is odd, multiply n by 3 and add 1. Continue this process until n is 1.

For this part, you can import `List` and `ArrayList`.

### ListExercises
    
`ListExercises.java` has 4 different methods for you to complete:
    
-   `sum`: This method takes a list `List<Integer> L` and returns the total sum of the elements in that list. If the list is empty, it method should return 0.
-   `evens`: This method takes a list `List<Integer> L` and returns a *new* list containing the even numbers of the given list. If there are no even elements, it should return an empty list.
-   `common`: This method takes two lists `List<Integer> L1`, `List<Integer> L2` and returns a *new* list containing the common item of the two given lists. If there are no common items, it should return an empty list.
-   `countOccurrencesOfC`: This method takes a list and a character `List<String> words`, `char c` and returns the number of occurrences of the given character in a list of strings. If the character does not occur in any of the words, it should return 0.
    
For this part, you can import `ArrayList`.
    
### MapExercises
    
`MapExercises.java` has 3 different methods for you to complete:
    
-   `letterToNum`: This method returns a map from every lower case letter to the number corresponding to that letter starting with 'a' is 1.
-   `squares`: This method takes a list `List<Integer> nums` and returns a map from the integers in the list to their squares. If the given list is empty, it should return an empty map.
-   `countWords`: This method takes a list `List<String> words` and returns a map of the counts of all words that appear in a list of words. If the given list is empty, it should return an empty map.
    
For this part, you can import `TreeMap`. 

### Dessert
    
    
-   TODO FILL THIS 
    
    
## Deliverables
    
- `ListExercises.java`
- `MapExercises.java`
- `JavaExercises.java`
- `Dessert.java`
    
For this assignment, you need to complete the methods in `JavaExercises.java`, `ListExerises`, `MapExercises`. You also need to create a new class `Dessert.java` and complete it accordingly. Make sure you test before you submit it to Gradescope. Although we do not have a submission limit for this specific assignment, in the future it is encouraged to use existing tests and write your own tests to see if your methods work before submitting your code to the autograder.