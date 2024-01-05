---
layout: page
title: "Lab 1: Caesar Cipher (Old)"
released: false
nav_exclude: true
---

This lab was replaced due to a restructuring in the first couple weeks. The
spec is preserved here.

### IntelliJ Test

To test if everything is working correctly, run the `CaesarCipher` class, as
shown below:

![caesar main](img/run_main.png){: style="max-height: 300;" }

You should see a console pop up, prompting you to "Type text to encrypt":

![caesar prompt](img/caesar_prompt.png){: style="max-height: 300;" }

You can click the red square to terminate the program.

<!-- TODO: What if it didn't work? -->

## Programming Exercise: `CaesarCipher`

{: .info}
This exercise relies on some material from HW 0. If you have not written Java
before, we strongly recommend reading HW 0 before this part. We encourage
you to ask for help on HW 0 concepts during lab.

### Background

A **cipher** is an _algorithm_ for encrypting or decrypting text. Generally, we
call the unencrypted text "plain text" and encrypted version "cipher text".

Here is an example of text that uses a Caesar cipher (which you will implement
in this lab):

{: style="text-align: center; width: fit-content;" }
| Plain Text | Shift | Cipher Text |
| ------------ | ----- | ------------- |
| `java is fun` | +8 | `sjej rb odw` |

Notably, the original text is readable, but the encrypted version is not.

A Caesar cipher is computed by "shifting" each letter of the text some number
of spaces forward in the English alphabet, wrapping around at the end, as though
it was written in a circle. For example, the following "ring" represents a
mapping for a Caesar cipher with each outside letter shifted forward by 4 to
get the inside letter.

![caesar cipher circle](img/circle.png){: style="max-height: 325;" }

In this lab, you'll be editing the `CaesarCipher.java` file, which has
empty methods for you to fill in. We will provide you Python code for these
methods. You might find HW 0, which compares Python and java syntax, to be
helpful. We recommend completing HW 0 before working on this part of the lab.

Our goal is to be able to take in a piece of text, the number of letters to
shift forward by, and output the encrypted text. We've provided a small `main`
method that will take input from the console. You don't have to understand how
it works, however.

{: .info}
In Python, there is only one way to represent strings of length one; however,
in Java, there are two. First, we can represent them as a `String`, similar to
Python `str`. Second, there is a separate type called `char`. The reason for
this distinction is that, because we require types in Java, it is useful to be
able to specify that we’re working with a single letter. Unlike in Python,
`String`s in Java must use double quotes (`\"`) and `char`s must use single
quotes (`'`).

### Methods to Implement

The first function you should implement is `findIndexInAlphabet`.

{: .function-info.block}
`public static int findIndexInAlphabet(char c)`

<div markdown="block">

You should loop through the valid indices of `ALPHABET` and return the index
equal to the input character `c` if one exists. If no such index exists, you
should return `-1`.

---

In Python, this method might approximately look like:

```python
def findIndexInAlphabet(c):
    for i in range(len(ALPHABET)):
        if ALPHABET[i] == c:
            return i
    return -1
```

</div>

In Python, you can't have two methods named the same thing. However, in Java,
we can! This is called **method overloading**, and works because the **types of
the arguments** are different. Next, you will implement two versions of the
`rotate` method: one for if we want to rotate a `char` (character), then another
for rotating a String.

{: .function-info.block}
`public static int rotate(char c, int amount)`

<div markdown="block">

Convert the input character into a number. Then, add the rotation amount to
that number, making sure to wrap the number around so it is between `0` and
`25`, the valid indices for the alphabet. Then, convert it back to a character.
If the character doesn't appear in the alphabet, return the character directly.

---

In Python, this method would approximately look like:

```python
def rot(c, amount):
    idx = findIndexInAlphabet(c)
    if idx == -1:
        return c
    newIdx = (idx + amount) % len(ALPHABET)
    return ALPHABET[newIdx]
```

</div>

The `String` version is the one that we call in `main`.

{: .function-info.block}
`public static int rotate(String line, int amount)`

<div markdown="block">

Rotate each character by the rotation `amount`, and return a new `String` made
up of the rotated characters.

---

In Python, this method would approximately look like:

```python
def rot(line, amount):
    output = ""
    for c in line:
        output += rot(c, n)
    return output
```

</div>

### Testing Your Code

While we could run the `CaesarCipher` file again and again to check that our
code works correctly, it would take a lot of time to type into the program each
time, and manually check that the output is correct. Instead, we use **tests**.

Open `CaesarCipherTests.java`, and click the green triangle next to the
`public class CaesarCipherTests`:

![caesar run rests](img/caesar_run_tests.png){: style="max-height: 200;" }

This will run the tests that we have provided in this assignment. If you have
correctly implemented the functions, all the tests will pass with a green
checkmark:

![caesar passed tests](img/caesar_tests_passed.png){: style="max-height: 200;" }

If you don't pass some tests, you'll see either a red exclamation point or a
yellow `x`:

![caesar failed tests](img/caesar_tests_failed.png){: style="max-height: 200;" }

To debug, click the dropdowns to see the output from a specific failing test.
Then, read the error to figure out why the bug might have occurred!
