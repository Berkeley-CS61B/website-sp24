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
- NOTE: In Java, `==` is used for identity, and `.equals()` is used for equality. For primitive types, this means the same thing, but for reference types, it may be different. For this assignment, you do not need to know the difference; we'll learn more about this later.

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


## Exercises

UW has a large collection of introductory Java exercises that we will be
borrowing. For HW 0, create an account on
[Practice-It](https://practiceit.cs.washington.edu), and complete the
following:

- [Self-Check 1.26: Confusing][]
- [Exercise 2.5: `starTriangle`][]
- [Self-Check 2.25: `numberTotal`][]
- [Exercise 3.23: `printIndexed`][] or [Exercise 4.17: `stutter`][]
- [Self-Check 4.5: `ifElseMystery1`][]
- [Exercise 4.19: `quadrant`][]

Make sure to follow the directions on the exercise page, especially for
printing versus returning!

If you run into trouble with the exercises, one strategy could be solving in
Python first, then translating that to Java. If you're having trouble with
solving in Python, that's fine, and not the point of this exercise. If you'd
like to reference Python solutions, see the dropdowns below.

<details markdown="block">
<summary markdown="block">

`starTriangle`

</summary>

```python
for i in range(5):
    line = ""
    for j in range(i + 1):
        line += "*"
    print(line)
```

</details>

<details markdown="block">
<summary markdown="block">

`printIndexed`

</summary>

```python
def printIndexed(s):
    output = ""
    for i in range(len(s)):
        output += s[i]
        output += str(len(s) - 1 - i)
    print(output)
```

</details>

<details markdown="block">
<summary markdown="block">

`stutter`

</summary>

```python
def stutter(s):
    output = ""
    for i in range(len(s)):
        output += s[i]
        output += s[i]
    return output
```

</details>

<details markdown="block">
<summary markdown="block">

`quadrant`

</summary>

```python
def quadrant(x, y):
    if x == 0 or y == 0:
        return 0
    elif y > 0 and x > 0:
        return 1
    elif y > 0 and x < 0:
        return 2
    elif y < 0 and x < 0:
        return 3
    else:
        return 4
```

</details>

[Self-Check 1.26: Confusing]: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter1/s26%2DConfusing
[Self-Check 2.25: `numberTotal`]: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter2/s25%2DnumberTotal
[Self-Check 4.5: `ifElseMystery1`]: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter4/s5%2DifElseMystery1
[Exercise 2.5: `starTriangle`]: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter2/e5%2DstarTriangle
[Exercise 3.23: `printIndexed`]: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter3/e23%2DprintIndexed
[Exercise 4.17: `stutter`]: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter4/e17%2Dstutter
[Exercise 4.19: `quadrant`]: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter4/e19%2Dquadrant

Once you've completed the 6 exercises, go to your list of
[solved problems](https://practiceit.cs.washington.edu/user/problems-solved),
take a screenshot of the table, and submit the screenshot to HW 0A on
Gradescope.

**NOTE**: If you are having trouble getting your screenshot into the PDF
format required by Gradescope, try using [this converter](https://png2pdf.com/).

Congratulations! You're prepared for the next few lectures, and have completed
HW 0. After Lecture 2, you'll be ready to read HW0B, but you can get a head
start now if you'd like.

A programming language is not too different from a spoken language -- in
particular, you will get better the more code you write. The PracticeIt site
has **many** problems available, and you should feel free to attempt more.
(Their progression doesn't exactly match ours, though -- if you see a `Scanner`
or need to generate a random number, you can skip that problem.)

We also recommend <https://codingbat.com/java/AP-1>, which has more advanced
Java problems.