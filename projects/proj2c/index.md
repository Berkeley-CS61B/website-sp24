---
layout: page
title: "Project 2C: Ngordnet Enhancemenets"
nav_order: 5
parent: Projects
has_children: true
has_toc: false
has_right_toc: true
description: >-
  Project 2C spec.
released: true
---

{: .warning}
This page is not officially released yet. All information here is subject to change.

## [FAQ](faq.md)

Each assignment will have an FAQ linked at the top. You can also access it by adding "/faq" to the end of the URL. The
FAQ for Project 2C is located
[here](faq.md).

## Project 2C Checkpoint Due XX/XX/XXXX - Design Doc Due XX/XX/XXXX - Coding Due XX/XX/XXXX

In this project, you'll complete your implementation of the NGordnet for `k!=0` and `commonAncestor` case.

As this is a quite new project, there may be occasional bugs or confusion with the spec. If you notice anything of this sort, please post on Ed.

{: .danger}
**PLEASE READ THROUGH 2B SPEC BEFORE STARTING 2C. YOU CAN FIND IT [HERE](../proj2b/index.md)**


## Project Setup

{: .danger}
**THE SETUP FOR THIS PROJECT IS DIFFERENT THAN THE OTHER LABS / PROJECTS. PLEASE DO NOT SKIP THIS STEP!**

### Skeleton Setup

1. Similar to other assignments in this class, run `git pull skeleton main` to get the skeleton code for this project.
   1. NOTE: You'll notice that this skeleton is (almost) the exact same as the Project 2A skeleton. We have provided placeholder implementations for `TimeSeries`, `NGramMap` from project 2a. This includes a working implementation of `countHistory` method using a new
   library from in `library-sp24` (see next step).
   2. The placeholder implementations throw `UnsupportedOperationException`s for some methods. You will not need these methods.
2. To get the new library, `cd` into your `library-sp24` directory and run `git pull`. Then,
   import all the libraries from `library-sp24` into this project like you normally would.
   1. Now that you've pulled and imported the libraries, you'll notice that the code in `NgramMap.java` should no longer be red.
3. Download the `data` files for this project
   using [this link](www.google.com)
   and move them into your `proj2c` folder on the same level as `src`.
4. You will need your implementation from 2B to get hyponyms of the word since `k!=0` & `commonAncestor` will depend on your implementation from 2B.

Once you are done, your `proj2c` directory should look like this:

```sh
proj2C
├── data
│   ├── ngrams
│   └── wordnet
├── src
├── static
├── tests
```

{: .info}
>The k != 0 portion of this project uses the `NGramMap` class from Project 2A, which is why we have provided placeholder implementations for `NGramMap` and `TimeSeries`. The placeholder implementations are sufficient to complete project 2b.
>
>If you want to copy in your own `NGramMap` and `TimeSeries` from Project 2B, you can. However, we suggest only doing so after you get a full score on project 2B just in case your implementation has any subtle bugs in it.
>
>Once you are done with Project 2B, please copy all necessary changes that you made in 2B to 2C folder. You should build your 2C on your 2B implementation.

{: .warning}
If you are getting errors in `NGramMap`, make sure you did step 2 (updating `library-sp24`).


## Getting Started

{: .warning}
**IMPORTANT NOTE:** You should *really* complete **Project 2C: [Checkpoint](www.google.com)** first before starting coding, or even designing your project. We think this would be helpful for your understanding of the project. We will also require to submit a design document to the gradescope. More details about design document can be found in [Deliverable and Scoring.](#deliverables-and-scoring).

{: .warning}
**IMPORTANT NOTE:** We recommend that you should complete Project 2B and get full score from grader before you are starting coding.

{: .task}
Complete **Project 2C: [Checkpoint](www.google.com)**
Complete **[Design Document](www.google.com)**

This part of the project is designed for you to come up with efficient and correct design for your implementation. The design you come up with will be very important to handle these cases. Please read 2B & 2C spec carefully before starting your design document.

The course staff has provided a higher overview of this part of the project. This might seem like not sufficient resource for now compared to previous parts and projects but we really want you ideate to come up with your own design and implementation! Nevertheless, if you still want to watch it, you can find it [here](www.google.com).

We've also created two wonderful tools that you can (and should!) use to explore the dataset, see how the staff solution
behaves for specific inputs, and get expected outputs for your unit tests (see [Testing Your Code](#testing-your-code)).
We'll link them here, as well as in other relevant parts of the spec.

- [Wordnet Visualizer](https://www.qxbytes.com/wordnet/): Useful for visually understanding how synsets and hyponyms work and testing
  different words/lists of words for potential test case inputs. Click on the "?" bubbles to learn how to use the various
  features of this tool!
- [Staff Solution Webpage](https://ngordnet.datastructur.es/): Useful for generating expected outputs for different test
  case inputs. Use this to write your unit tests!

## Handling `k != 0`

Above, we handled the situation where `k = 0`, which is the default value when the user does not enter a `k` value.

Your final required task is to handle the case where the user enters `k`. `k` represents the maximum number of hyponyms
that we want in our output. For example, if someone enters the word "dog", and then enters `k = 5`, your code would
return exactly 5 words.

To choose the 5 hyponyms, you should return the `k` words which occurred the most times in the time range requested. For
example, if someone entered `words = ["food", "cake"]`, `startYear = 1950`, `endYear = 1990`, and `k = 5`, then you would
find the 5 most popular words in that time period that are hyponyms of both food and cake. Here, the popularity is
defined as the total number of times the word appears over the entire time period. The words should then be returned in
alphabetical order. In this case, the answer is `[cake, cookie, kiss, snap, wafer]` if we're
using `top_14377_words.csv`,
`synsets.txt`, and `hyponyms.txt`.

Note that if the front end doesn't supply a year, default values of startYear = 1900 and endYear = 2020 are provided by
`NGordnetQueryHandler.readQueryMap`.

Now fun part.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FFw2oz5FIMrFRhh9yL8Ylun%2F2C%3Ftype%3Ddesign%26node-id%3D0%253A1%26mode%3Ddesign%26t%3Dn6fDDOrwY4Lb9Gbi-1" allowfullscreen></iframe>

{: .info}
>If `k = 0`, or the user does not enter `k` (which results in a default value of zero), then the `startYear`
>and `endYear` should be totally ignored.

>If a word never occurs in the time frame specified, i.e. the count is zero, it should not be returned. In other words,
>if `k > 0`, we should not show any words that do not appear in the `ngrams` dataset.

>If there are no words that have non-zero counts, you should return an empty list, i.e. `[]`.

>If there are fewer than `k` words with non-zero counts, return only those words. For example if you enter the word
"potato" and enter "k = 15", but only 7 hyponyms of potato have non-zero counts, you'd return only 7 words.

{: .task}
Modify your `HyponymsHandler` and the rest of your implementation to deal with the `k != 0` case.

{: .warning}
>This task will be a little trickier since you'll need to figure out how to pass information around so that the
>`HyponymsHandler` knows how to access a useful `NGramMap`.

{: .warning}
EECS-course gide is not available on web staff solution so it won't return anything if you give input `CS61A`.

{: .warning}
The `TimeSeries` class we provide in the skeleton code does not support `.data()`. You can use `.values()` instead.

{: .danger}
>**DO NOT MAKE A STATIC NGRAMMAP FOR THIS TASK!** It might be tempting to simply make some sort of
>`public static NGramMap` that can be accessed from anywhere in your code. This is called a \"global variable\".
>
>We strongly discourage this way of thinking about programming, and instead suggest that you should be passing an
>NGramMap to either constructors or methods. We'll come back to talking about this during the software engineering
lectures.

#### Tips

- Until you use the autograder, you'll need to construct your own test cases. We provide one
  above: `words = ["food", "cake"]`
  , `startYear = 1950`, `endYear = 1990`, `k = 5`.
- When constructing your own test cases, consider making your own input files. Using the large input files we provide is
  extremely tedious.
- In the coming sections of this spec, we'll tell you how to set up your code for submission to the autograder, and how
  to write your own JUnit tests to mimic the test cases provided by the grader.

## Deliverables and Scoring

For Project 2C, the only required deliverable is the `HyponymsHandler.java` file, in addition to any helper classes.
However, we will not be directly grading these classes, since they can vary from student to student.

Project 2C will be worth 35 points. The points will be split as follows:

- [Project 2C Checkpoint](www.google.com): 5 points - Due March 18th
- Project 2C Coding: 30 points - Due April 1st
   - `HyponymHandler` popularity: 50%, k != 0
   - `HyponymHandler` common-ancestor: 50%

In addition to Project 2C, you will also have to turn in your design document.


Due March 20th

The token limiting policy for this project will be as follows: You will start with 8 tokens, each of which has a 24-hour refresh time.


## Testing Your Code

We've provided you with two short unit test files for this project in the `proj2b_testing` directory:

- `proj2b_testing/TestOneWordK0Hyponyms.java`
- `proj2b_testing/TestMultiWordK0Hyponyms.java`

The two provided test files correspond to the first two cases that you solved in this project, that is:

- Finding hyponyms of a single word where k = 0.
- Finding hyponyms of multiple words where k = 0 (e.g. `gallery, bowl`).

**These test files are not comprehensive**; in fact, they each only contain one sanity check test. You should fill
each file with more unit tests, and also use them as a template to create two new test files for the respective cases
where `k != 0`.

{: .task}
Fill out the provided unit test files for the `k = 0` cases, and then write similar tests for the
`k != 0` case.

If you need help figuring out what the expected outputs of your tests should be, you should use the two tools that we
linked in the [Getting Started](#getting-started) section.

## Debugging Tips

- Use the small files while testing! This decreases the startup time to run `Main.java` and makes it easier to reason about the code. If you're running `Main.java`, these files are set in the first few lines of the `main` method. For unit tests, the file names are passed into the `getHyponymHandler` method.
- You can run `Main.java` with the debugger to debug different inputs quickly. After clicking the “Hyponyms” button, your code will execute with the debugger - breakpoints will be triggered, you can use the variables window, etc.
- There are a lot of moving parts to this project. Don’t start by debugging line-by-line. Instead, narrow down which function/region of your code is not working correctly then search more closely in those lines.
- Check the [FAQ](faq.md) for common issues and questions.

## Submitting Your Code

Throughout this assignment, we've had you use your front end to test your code. Our grader is not sophisticated enough
to pretend to be a web browser and call your code. Instead, we'll need you to provide a method in the
`proj2b_testing.AutograderBuddy` class that provides a handler that can deal with hyponyms requests.

When you ran `git pull skeleton main` at the start of this spec, you should have received a file called `AutograderBuddy.java`

Open `AutograderBuddy.java` and fill in the `getHyponymHandler` method such that it returns a `HyponymsHandler`
that uses the four given files. Your code here should be quite similar to your code in `Main.java`.

Now that you've created `proj2b_testing.AutograderBuddy`, you can submit to the
autograder. If you fail any tests, you should be able to replicate them locally as JUnit tests by building on the test
files above. If any additional datafiles are needed, they will be added to this section as links.

## Optional Extra Features

If you'd like to go above and beyond in this project (and even explore some front-end development), read through the
[Optional Features](optional_features.md) spec!

## Acknowledgements

The WordNet part of this assignment is loosely adapted from Alina Ene and Kevin Wayne's
[Wordnet assignment](http://www.cs.princeton.edu/courses/archive/fall14/cos226/assignments/wordnet.html) at Princeton
University.

<!---
Some sort of design doc would be nice.

Dominic suggested instead a "pipeline". Basically some sort of visual depiction about how their whole system works.

Have both types of solution (with a node class, without a node class) in staff guide and solution.

Add an empty HyponymHandler file that is empty to have the name right.

-->
