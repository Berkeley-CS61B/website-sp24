---
layout: page
title: >-
  Homework 0A: Java Syntax
nav_order: 0
# nav_exclude: true
parent: Homework 0
grand_parent: Homeworks
has_children: true
has_toc: false
has_right_toc: true
description: >-
  Homework 0A spec.
released: true
---

## Language Constructs

Many Python fundamentals have a Java equivalent, such as loops and if
statements. This section shows a direct comparison of the syntax.

### Variable Declaration

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
    <tr>
<td markdown="block">

```python
i = 0
```

</td>
<td markdown="block">

```java
int i = 0;
```

</td>
</tr>
</table>

- Just like Python, Java variables have _types_. In Java, to declare a
  variable, we have to explicitly say what type it is. A variable's declared
  type can never change. Refer to Lecture 1 for more on "static typing."
- We also have to put a semi-colon at the end of the statement.

### Types

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD013 -->

| Python        | Java      | What?                                                                            |
| ------------- | --------- | -------------------------------------------------------------------------------- |
| `bool`        | `boolean` | Python uses `True` and `False`; Java uses `true` and `false`.                    |
| `int`         | `int`     | While Python `int`s are unbounded, Java `int`s have a (large) max and min value. |
| `float`       | `double`  | Decimal values. Java `doubles` are again bounded.                                |
| `str`         | `String`  | Java `String`s use double quotes (`"`), and can be any text.                     |
| no equivalent | `char`    | Java `char` represents a _single_ character, and uses single quotes (`'`).       |

<!-- markdownlint-restore -->

### Comments

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
# This is a single line comment.
```

</td>
<td markdown="block">

```java
// This is a single line comment.
```

</td>
</tr>
</table>

Java also has multi-line comments that are started by `/*` and ended by `*/`.

### `while` Loop

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
i = 0
while i < 10:
    print(i)
    i += 1

```

</td>
<td markdown="block">

```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}
```

</td>
</tr>
</table>

- The parentheses, `(` and `)` around the condition are required.
- In Java, `++` is often used instead of `+= 1`.
- We really do use `System.out.println` to print in Java. Sorry.
- Instead of indenting, we use curly braces, `{` and `}` to wrap the code that
  is part of the while loop. Java doesn't require indenting, but it's good
  style!

### `for` Loop (counting up)

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
for i in range(10):
    print(i)

```

</td>
<td markdown="block">
```java
for (int i = 0; i < 10; i ++) {
    System.out.println(i);
}
```

</td>
</tr>
</table>

In Java, the `for` loop has the syntax:

```java
for (initialization; termination; increment) {
    // loop body
}
```

This is roughly equivalent to the while loops:

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
initialization
while termination:
    # loop body
    increment

```

</td>
<td markdown="block">

```java
initialization
while (termination) {
    // loop body
    increment
}
```

</td>
</tr>
</table>

The `while` loops and the `for` loop exit when the termination condition is
false. The `for` loops in the comparison table go "until" `i = 10`.

### `for` Loop (counting down)

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
for i in range(9, -1, -1):
  print(i)

```

</td>
<td markdown="block">

```java
for (int i = 9; i >= 0; i --) {
  System.out.println(i);
}
```

</td>
</tr>
</table>

- Note the different "initialization", "termination", and "increment" blocks
  in the Java `for` loop.
- Similarly to `++`, `--` is often used instead of `-= 1`.
- The `for` loops in the comparison table go "until" `i < 0`.

### Conditionals

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
else:
    print(i)

```

</td>
<td markdown="block">

```java
if (i % 3 == 0 && i % 5 == 0) {
    System.out.println("FizzBuzz");
} else if (i % 3 == 0) {
    System.out.println("Fizz");
} else if (i % 5 == 0) {
    System.out.println("Buzz");
} else {
    System.out.println(i);
}
```

</td>
</tr>
</table>

The boolean operators are as follows:

| Python | Java |
| ------ | ---- |
| `and`  | `&&` |
| `or`   | `||` |
| `not`  | `!`  |
| `==`   | `==` |

- Note the difference between `elif` and `else if`.

### Exponentiation

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
x = 2**10
```

</td>
<td markdown="block">

```java
int x = Math.pow(2, 10);
```

</td>
</tr>
</table>

Note that `^` in Java is the "XOR" operator, not the exponentiation operation.
That is, `2 ^ 10` is valid code, but it will return `8`, not `1024`.

### Function Declaration and Usage

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
def greet(name):
    return "Hello, " + name

# Elsewhere...
print(greet("Josh"))
```

</td>
<td markdown="block">

```java
public static String greet(String name) {
    return "Hello, " + name;
}
// Elsewhere...
System.out.println(greet("Josh"));
```

</td>
</tr>
</table>

- In Java, functions have a specific return type that comes before the
  function name. Functions also specify their arguments' types.
  - When a function returns nothing, it has a return type of `void`.
- For now, all our functions will have `public static` in front. We'll learn
  what these mean later.
- Calling a function looks the same as in Python.

### Strings

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
s = "hello"
s += " world"
s += str(5)
s_length = len(s)
substr = s[1:5]
c = s[2]
if "hello" in s:
    print("\"hello\" in s")

for letter in s:
    print(letter)

```

</td>
<td markdown="block">

```java
String s = "hello";
s += " world";
s += 5;
int sLength = s.length();
String substr = s.substring(1, 5);
char c = s.charAt(2);
if (s.indexOf("hello") != -1) {
    System.out.println("\"hello\" in s");
}
for (int i = 0; i < s.length(); i++) {
    char letter = s.charAt(i);
    System.out.println(letter);
}
```

</td>
</tr>
</table>

- In Java, `String`s are not directly iterable. We either iterate over an
  index and use `charAt`, or we convert it to an array (coming soon).
- In Java, you can add anything to a `String`s, and it will be implicitly
  converted to a `String` without needing to explicitly cast.

## Programs

Now that we've covered individual language constructs, let's look at some Java
programs that use them. Here are some simple ones that you might find yourself
referring to if you forget how to do something.

### Hello World

<table>
    <thead>
        <th>Python</th>
        <th>Java</th>
    </thead>
<tr>
<td markdown="block">

```python
print("Hello World")
```

</td>
<td markdown="block">
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
</td>
</tr>
</table>

- All Java code must be in a **class**. We'll learn more about classes later.
- When a Java program is executed, it runs the
  **`public static void main(String[] args)`** method. This is different from
  Python, where code can be executed outside of a function.

<!-- TODO: conditional example. Loop example.
- Collatz sequence (if, while)
- something with for and Strings
-->