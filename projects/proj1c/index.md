---
# layout: page # The HTML template to use to render this page.
# title: "Project 1C: Deque Enhancements" # Title of page.
# categories: proj
# released: true # you have to also change this to true to release.
# toc:
#   h_max: 4

layout: page
title: "Project 1C: Deque61B Enhancements"
nav_order: 3
parent: Projects
has_children: true
has_toc: false
has_right_toc: true
description: >-
  Project 1C.
released: true
---

## Due: September 25th

{: .no_toc}

{: .warning}
This site is still under construction.

## [FAQ](faq.md)

Each assignment will have an FAQ linked at the top. You can also access it by adding "/faq" to the end of the URL. The
FAQ for Project 1C is located
[here](faq.md).

## Introduction

In Project 1A, we built `LinkedListDeque61B` and in Project 1B, we built `ArrayDeque61B`. Now we'll see a different
implementation: `MaxArrayDeque61B`! This part of the project will provide some enhancements to your
previous `ArrayDeque61B` and `LinkedListDeque61B`, and also bring everything together into an application of your newly-built data structure.

By the end of Project 1C, you will complete the following:

- Write the `iterator()`, `equals()`, and `toString()` methods for `LinkedListDeque61B.java` and `ArrayDeque61B.java`.
- Implement `MaxArrayDeque61B.java`.
- Finish the `GuitarHero` tasks.

{: .warning}
>This section assumes you have watched and fully digested the lectures up till
>the Iterators, Object Methods lecture, Lecture 11.

### Style

As in Project 1B, **we will be enforcing style**. You must follow the
[style guide](../../guides/style/index.md), or you will be penalized on the
autograder.

You can and should check your style locally with the CS 61B plugin. **We will
not remove the velocity limit for failing to check style.**

### Getting the Skeleton Files

Follow the instructions in the
[Assignment Workflow guide](../../guides/assignment-workflow/index.md/#assignment-workflow)
to get the skeleton code and open it in IntelliJ. For this project, we will be
working in the **`proj1c`** directory.

You see a `proj1c` directory appear in your repo with the following structure:

```sh
 proj1c
├── src
│   ├── deque
│   │   ├── ArrayDeque61B.java
│   │   ├── Deque61B.java
│   │   └── LinkedListDeque61B.java
│   └──gh2
│       ├── GuitarHeroLite.java
│       ├── GuitarPlayer.java
│       ├── GuitarString.java
│       └── TTFAF.java
│
└── tests
    ├── MaxArrayDeque61BTest.java
    └── TestGuitarString.java
```


{: .danger}
>If you get some sort of error, STOP and either figure it out by carefully
>reading the [git WTFs](../../guides/git/wtfs/index.md) or seek help at OH
>or Ed. You'll potentially save yourself a lot of trouble vs. guess-and-check
>with git commands. If you find yourself trying to use commands recommended by
>Google like `force push`,
>[don't](https://twitter.com/heathercmiller/status/526770571728531456).
>
>**Don't use force push, even if a post you found on Stack Overflow says to do it!**

You can also watch Professor Hug's [demo](https://www.youtube.com/watch?v=tABtNcN5y0A)
about how to get started and this [video](https://www.youtube.com/watch?v=Squ8TmG5mX0)
if you encounter some git issues.

### Object Methods

**If you'd like, you can follow the steps in this short [video guide](https://youtu.be/j0dk9zozYwA) to help you get
set up for Project 1C!**

In order to implement the following methods, you should start by copying and pasting your Project 1A and Project 1B
implementations of `LinkedListDeque61B` and `ArrayDeque61B` into the relevant files in your `proj1c` directory. 

{: .warning}
Please keep `package deque;` at the top of both files. Otherwise, your code will not compile.


#### `iterator()`

One shortcoming of our `Deque61B` interface is that it can not be iterated over. That is, the code below fails to compile with the error "foreach not applicable to type".

```java
  Deque61B<String> lld1 = new LinkedListDeque61B<>();

  lld1.addLast("front");
  lld1.addLast("middle");
  lld1.addLast("back");
  for (String s : lld1) {
      System.out.println(s);
  }
```

Similarly, if we try to write a test that our `Deque61B` contains a specific set of items, we'll also get a compile error, in this case: "Cannot resolve method containsExactly in Subject".

```java
public void addLastTestBasicWithoutToList() {
    Deque61B<String> lld1 = new LinkedListDeque61B<>();

    lld1.addLast("front"); // after this call we expect: ["front"]
    lld1.addLast("middle"); // after this call we expect: ["front", "middle"]
    lld1.addLast("back"); // after this call we expect: ["front", "middle", "back"]
    assertThat(lld1).containsExactly("front", "middle", "back");
}
```

Again the issue is that our item cannot be iterated over. The `Truth` library works by iterating over our object (as in the first example), but our `LinkedListDeque61B` does not support iteration.

To fix this, you should first modify the `Deque61B` interface so that the declaration reads:

```java
public interface Deque61B<T> extends Iterable<T> {
```

Next, implement the `iterator()` method using the techniques described in lecture 11.

{: .task}
>**Task**: Implement the `iterator()` method in both `LinkedListDeque61B` and
>`ArrayDeque61B` according to lecture.

{: .danger}
You are not allowed to call `toList` here.

#### `equals()`

Consider the following code:

```java
    @Test
    public void testEqualDeques61B() {
        Deque61B<String> lld1 = new LinkedListDeque61B<>();
        Deque61B<String> lld2 = new LinkedListDeque61B<>();

        lld1.addLast("front");
        lld1.addLast("middle");
        lld1.addLast("back");

        lld2.addLast("front");
        lld2.addLast("middle");
        lld2.addLast("back");

        assertThat(lld1).isEqualTo(lld2);
    }
```

If we run this code, we see that we fail the test, with the following message:

```
expected: [front, middle, back]
but was : (non-equal instance of same class with same string representation)
```

The issue is that the `Truth` library is using the `equals` method of the `LinkedListDeque61B` class. The default implementation is given by the [code below](https://github.com/openjdk/jdk17/blob/master/src/java.base/share/classes/java/lang/Object.java#L162):

```java
    public boolean equals(Object obj) {
        return (this == obj);
    }
```

That is, the equals method simply checks to see if the addresses of the two objects are the same.

Override the equals method in the `ArrayDeque61B` and `LinkedListDeque61B` classes. For guidance on writing an `equals` method, see the [lecture slides](https://docs.google.com/presentation/d/1lIR4--P9NrBqRL9xqP_RQYyK1WJBrBEbriLVpatrRqk/edit#slide=id.g4f922fa56b_2_47) or the [lecture code repository](https://github.com/Berkeley-CS61B/lectureCode-sp23/blob/main/lec12_inheritance4/ArraySet.java).

{: .task}
**Task**: Override the `equals()` method in the `LinkedListDeque61B` and `ArrayDeque61B` classes.

{: .warning}
>Important: You should not use `getClass`, and there's no need to do any casting in your `equals` method. That is, you shouldn't be doing `(ArrayDeque61B) o`. Such `equals` methods are old fashioned and overly complex. Use `instanceof` instead.
>
>Note: The `instanceof` operator behaves a little strangely with generic types, for reasons beyond the scope of this course. For example, if you want to check if `lst` is an instance of a `List<Integer>`, you should use `lst instanceof List<?>` rather than `lst instanceof List<Integer>`. Unfortunately, this is not able to check the types of the elements, but it's the best we can do.

{: .danger}

{: .warning}
Important: Make sure you use the `@Override` tag when overriding methods. A common mistake in student code is to try to override `equals(ArrayList<T> other)` rather than `equals(Object other)`. Using the optional `@Override` tag will prevent your code from compiling if you make this mistake. `@Override` is  a great safety net.

{: .danger}
You are not allowed to call `toList` here.

#### `toString()`

Consider the code below, which prints out a `LinkedListDeque61B`.

```java
Deque61B<String> lld1 = new LinkedListDeque61B<>();

lld1.addLast("front");
lld1.addLast("middle");
lld1.addLast("back");

System.out.println(lld1);
```

This code outputs something like `deque.proj1a.LinkedListDeque61B@1a04f701`. This is because the print statement implicitly calls the `LinkedListDeque61B` `toString` method. Since you didn't override this method, it uses the default, which is given by the code below (you don't need to understand how this code works).

```java
    public String toString() {
        return getClass().getName() + "@" + Integer.toHexString(hashCode());
    }
```

In turn the `hashCode` method, which you have also not overridden, simply returns the address of the object, which in the example above was `1a04f701`.

{: .task}
**Task**: Override the `toString()` method in the `LinkedListDeque61B` and `ArrayDeque61B` classes, such that the code above prints out `[front, middle, back]`.

{: .warning}
>Hint: Java's implementation of the `List` interface has a `toString` method.
>
>Hint: There is a one line solution (see hint 1).
>
>Hint: Your implementation for `LinkedListDeque61B` and `ArrayDeque61B` should be exactly the same.

{: .info}
>Note: You might ask why we're implementing the same method in two classes rather than providing a `default` method in
>the `Deque61B` interface. Interfaces are not allowed to provide `default` methods that override `Object` methods. For more
>see [https://stackoverflow.com/questions/24595266/why-is-it-not-allowed-add-tostring-to-interface-as-default-method](https://stackoverflow.com/questions/24595266/why-is-it-not-allowed-add-tostring-to-interface-as-default-method).
>
>---
>
>One workaround for this is to provide a `default`, non-`Object` helper method in the `Deque61B` interface and have the implementing classes call it.

#### Testing The Object Methods

We haven't provided you with test files for these three object methods; however, we strongly encourage you to use the
techniques you learned from projects 1A and 1B to write your own tests. You can structure these tests however you'd like,
since we won't be testing them. One possible (and suggested) structure is to create two new files in the `tests` directory
called `LinkedListDeque61BTest` and `ArrayDeque61BTest`, similar to the ones we gave you in 1A and 1B.

## MaxArrayDeque61B

After you've fully implemented your `ArrayDeque61B` and tested its correctness, you will now build the `MaxArrayDeque61B`.
**A `MaxArrayDeque61B` has all the methods that an `ArrayDeque61B` has**, but it also has 2 additional methods and a new
constructor:

- `public MaxArrayDeque61B(Comparator<T> c)`: creates a `MaxArrayDeque61B` with the given `Comparator`.
- `public T max()`: returns the maximum element in the deque as governed by the previously given `Comparator`. If
  the `MaxArrayDeque61B` is empty, simply return
  `null`.
- `public T max(Comparator<T> c)`: returns the maximum element in the deque as governed by the parameter `Comparator c`.
  If the `MaxArrayDeque61B` is empty, simply return `null`.

The `MaxArrayDeque61B` can either tell you the max element in itself by using the
`Comparator<T>` given to it in the constructor, or an arbitrary `Comparator<T>`
that is different from the one given in the constructor.

We do not care about the `equals(Object o)` method of this class, so feel free to define it however you think is most
appropriate. We will not test this method.

{: .warning}
>If you find yourself starting off by copying your entire `ArrayDeque61B`
>implementation in a `MaxArrayDeque61B` file, then you're doing it wrong. This is an exercise in clean code, and redundancy
>is one our worst enemies when battling complexity! For a hint, re-read the second sentence of this section above.

{: .task}
**Task**: Fill out the `MaxArrayDeque61B.java` file according to the API above.

There are no runtime requirements on these additional methods, we only care about the correctness of your answer.
Sometimes, there might be multiple elements in the `MaxArrayDeque61B` that are all equal and hence all the max: in in this
case, you can return any of them and they will be considered correct.

You should write tests for this part as well! You'll
likely be creating multiple `Comparator<T>` classes to test your code:
this is the point! To get practice using `Comparator` objects to do something useful (find the maximum element) and to
get practice writing your own
`Comparator` classes. You will not be turning in these tests, but we still highly suggest making them for your sake.

You will not use the `MaxArrayDeque61B` you made for the next part; it'll be in an isolated exercise.

## Guitar Hero

In this part of the project, we will create another package for generating synthesized musical instruments using
the `deque` package we just made. We'll get the opportunity to use our data structure for implementing an algorithm that
allows us to simulate the plucking of a guitar string.

### The GH2 Package

The `gh2` package has just one primary component that you will edit:

- `GuitarString`, a class which uses an `Deque61B<Double>` to implement the
  [Karplus-Strong algorithm](http://en.wikipedia.org/wiki/Karplus%E2%80%93Strong_string_synthesis)
  to synthesize a guitar string sound.

We've provided you with skeleton code for `GuitarString` which is where you will use your `deque` package that you made
in the first part of this project.

### `GuitarString`

We want to finish the `GuitarString` file, which should use the `deque` package to replicate the sound of a plucked
string. We'll be using the Karplus-Strong algorithm, which is quite easy to implement with a `Deque61B`.

The Karplus-Algorithm is simply the following three steps:

1. Replace every item in a `Deque61B` with random noise (`double` values between -0.5 and 0.5).
2. Remove the front double in the `Deque61B` and average it with the next double in the `Deque61B` (hint: use `removeFirst)`
   and `get()`) multiplied by an energy decay factor of 0.996 (we'll call this entire quantity
   `newDouble`). Then, add `newDouble` to the back of the `Deque61B`.
3. Play the `double` (`newDouble`) that you dequeued in step 2. Go back to step 2 (and repeat forever).

Or visually, if the `Deque61B` is as shown on the top, we'd remove the 0.2, combine it with the 0.4 to form 0.2988, add the
0.2988, and play the 0.2.

![karplus-strong](karplus-strong.png)

You can play a `double` value with the `StdAudio.play` method. For example
`StdAudio.play(0.333)` will tell the diaphragm of your speaker to extend itself to 1/3rd of its total
reach, `StdAudio.play(-0.9)` will tell it to stretch its little heart backwards almost as far as it can reach. Movement
of the speaker diaphragm displaces air, and if you displace air in nice patterns, these disruptions will be interpreted
by your consciousness as pleasing thanks to billions of years of evolution.
See [this page](http://electronics.howstuffworks.com/speaker6.htm) for more. If you simply do `StdAudio.play(0.9)` and
never play anything again, the diaphragm shown in the image would just be sitting still 9/10ths of the way forwards.

Complete `GuitarString.java` so that it implements steps 1 and 2 of the Karplus-Strong algorithm. Note that you will
have to fill your `Deque61B` buffer with zeros in the `GuitarString` constructor. Step 3 will be done by the client of the
`GuitarString` class.

{: .danger}
>Do not call `StdAudio.play` in `GuitarString.java`. This will cause the
>autograder to break. `GuitarPlayer.java` does this for you already.

{: .info}
Make sure to add the libraries, as usual, otherwise IntelliJ won't be able to find `StdAudio`.

For example, the provided `TestGuitarString` class provides a sample test
`testPluckTheAString` that attempts to play an A-note on a guitar string. If you run the test should hear an A-note when
you run this test. If you don't, you should try the
`testTic` method and debug from there. Consider adding a `print` or `toString`
method to `GuitarString.java` that will help you see what's going on between tics.

Note: we've said `Deque61B` here, but not specified which `Deque61B` implementation to use. That is because we only need those
operations `addLast`, `removeFirst`, and `get` and we know that classes that implement `Deque61B` have them. So you are
free to choose either the `LinkedListDeque61B` for the actual implementation, or the `ArrayDeque61B`. For an optional (but
highly suggested) exercise, think about the tradeoffs with using one vs the other and discuss with your friends what you
think the better choice is, or if they're both equally fine choices.

### Why It Works

The two primary components that make the Karplus-Strong algorithm work are the ring buffer feedback mechanism and the
averaging operation.

- **The ring buffer feedback mechanism**. The ring buffer models the medium (a string tied down at both ends) in which
  the energy travels back and forth. The length of the ring buffer determines the fundamental frequency of the resulting
  sound. Sonically, the feedback mechanism reinforces only the fundamental frequency and its harmonics (frequencies at
  integer multiples of the fundamental). The energy decay factor (.996 in this case) models the slight dissipation in
  energy as the wave makes a round trip through the string.
- **The averaging operation**. The averaging operation serves as a gentle low-pass filter (which removes higher
  frequencies while allowing lower frequencies to pass, hence the name). Because it is in the path of the feedback, this
  has the effect of gradually attenuating the higher harmonics while keeping the lower ones, which corresponds closely
  with how a plucked guitar string sounds.

### `GuitarHeroLite`

You should now also be able to use the `GuitarHeroLite` class. Running it will provide a graphical interface, allowing
the user (you!) to interactively play sounds using the `gh2` package's `GuitarString` class.


### Submission

To submit the project, add and commit your files, then push to your remote repository. Then, go to the relevant
assignment on Gradescope and submit there.

The autograder for this assignment will have the following velocity limiting scheme:

- From the release of the project to 10:00PM on 09/15/2023, you will have 6 tokens; each of
  these tokens will refresh every 24 hours.
- From 10:00PM to 11:59PM on 09/26/2023 (the last 2 hours before the deadline), you will get 6 tokens; each of these tokens will refresh every 15 minutes.

### Scoring

This project, similar to Project 0, is divided into individual components, each
of which you must implement _completely correctly_ to receive credit.

1. **`LinkedListDeque61B` Object Methods (20%)**: Correctly implement `iterator`, `equals`, and `toString` in `LinkedListDeque61B`.
2. **`ArrayDeque61B` Object Methods (20%)**: Correctly implement `iterator`, `equals`, and `toString` in `ArrayDeque61B`.
3. **`MaxArrayDeque61B` Functionality (5%)**: Ensure your `MaxArrayDeque61B` correctly runs all the methods in the `Deque61B` interface.
4. **`MaxArrayDeque61B` Max (35%)**: Correctly implement `max` in `MaxArrayDeque61B`.
5. **`GuitarString` (20%)**: Correctly implement the `GuitarString` client class.

In total, Project 1c is worth 10 points.

### Credits

- Ring buffer figures from [Wikipedia](http://en.wikipedia.org/wiki/Circular_buffer).
- This assignment adapted from
  [Kevin Wayne's Guitar Heroine](http://nifty.stanford.edu/2012/wayne-guitar-heroine/) assignment.
