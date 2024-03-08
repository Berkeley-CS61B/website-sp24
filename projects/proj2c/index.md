---
layout: page
title: "Project 2C: Ngordnet Enhancements"
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

## Checkpoint & Design Doc Due 03/13/2024
## Coding Due 04/01/2024



In this project, you'll complete your implementation of the NGordnet for `k!=0` and `commonAncestors` case.

As this is a quite new project, there may be occasional bugs or confusion with the spec. If you notice anything of this sort, please post on Ed.

{: .danger}
**PLEASE READ THROUGH 2B SPEC BEFORE STARTING 2C. YOU CAN FIND IT [HERE](../proj2b/index.md)**


## Project Setup

{: .danger}
**THE SETUP FOR THIS PROJECT IS DIFFERENT THAN THE OTHER LABS / PROJECTS. PLEASE DO NOT SKIP THIS STEP!**

### Skeleton Setup

1. Similar to other assignments in this class, run `git pull skeleton main` to get the skeleton code for this project.
   1. NOTE: You'll notice that this skeleton is (almost) the exact same as the Project 2B skeleton. 
2. Download the `data` files for this project
   using [this link](https://drive.google.com/file/d/160iHOqwR4FAghGshbnSNMwd0idrjZxTR/view?usp=sharing)
   and move them into your `proj2c` folder on the same level as `src`.
3. You will need your implementation from 2A for `TimeSeries` and `NGramMap` as well as your implementation from 2B since `k!=0` & `commonAncestors` will depend on your implementation from 2A and 2B.

Once you are done, your `proj2c` directory should look like this:

```sh
proj2c
├── data
│   ├── ngrams
│   └── wordnet
├── src
│   ├── <2B helper files>
│   ├── browser
│   ├── main
│   ├── ngrams
│   │   ├── <2A implementation>
│   └── plotting
├── static
├── tests
```

{: .info}
>The k != 0 portion of this project uses the `NGramMap` class from Project 2A. You will need to copy your `NGramMap` and `TimeSeries` from Project 2A into this project, as well as any possible helper classes from 2B.
>
>While you can design for 2C in advance, we suggest only starting coding after you get a full score on project 2B just in case your implementation has any subtle bugs in it.
>
>Once you are done with Project 2B, please copy all necessary changes that you made in 2B to 2C folder. You should build your 2C on your 2B implementation.

## Getting Started

{: .warning}
**IMPORTANT NOTE:** You should *really* complete **Project 2B/C: [Checkpoint](https://www.gradescope.com/courses/708063/assignments/4133684)** first before starting coding, or even designing your project. We think this would be helpful for your understanding of the project. We will also require to submit a [design document](https://docs.google.com/document/d/1Vx7QAz4HFN0rEFFEt5rocY2X5AWVcIFFpRmD8vhegOM/edit?usp=sharing) to the gradescope. More details about design document can be found in [Deliverable and Scoring.](#deliverables-and-scoring).

{: .warning}
**IMPORTANT NOTE:** We recommend that you should complete Project 2B and get a full score from the autograder before you start coding.

This part of the project is designed for you to come up with efficient and correct design for your implementation. The design you come up with will be very important to handle these cases. Please read the 2B & 2C spec carefully before starting your design document.

[//]: # (Course staff has provided a higher overview of this part of the project. This might seem like an insufficient resource for now compared to previous parts and projects but we really want you to ideate and come up with your own design and implementation! Nevertheless, if you still want to watch it, you can find it [here]&#40;www.google.com&#41;.)

We've created two wonderful tools that you can (and should!) use to explore the dataset, see how the staff solution
behaves for specific inputs, and get expected outputs for your unit tests (see [Testing Your Code](#testing-your-code)).
We'll link them here, as well as in other relevant parts of the spec.

- [Wordnet Visualizer](https://www.qxbytes.com/wordnet/): Useful for visually understanding how synsets and hyponyms work and testing
  different words/lists of words for potential test case inputs. Click on the "?" bubbles to learn how to use the various
  features of this tool!
- [Staff Solution Webpage](https://ngordnet.datastructur.es/): Useful for generating expected outputs for different test
  case inputs. Use this to write your unit tests!

{: .task}
>Read through entire 2B/C spec and complete **Project 2B/C: [Checkpoint](https://www.gradescope.com/courses/708063/assignments/4133684)**
>
>Read through entire 2B/C spec and complete **[Design Document](https://www.gradescope.com/courses/708063/assignments/4187810)**

## Handling `k != 0`

In Project 2B, we handled the situation where `k == 0`, which is the default value when the user does not enter a `k` value.

Your required task is to handle the case where the user enters `k`. `k` represents the maximum number of hyponyms
that we want in our output. For example, if someone enters the word "dog", and then enters `k = 5`, your code would
return at most 5 words.

To choose the 5 hyponyms, you should return the `k` words which occurred the most times in the time range requested. For
example, if someone entered `words = ["food", "cake"]`, `startYear = 1950`, `endYear = 1990`, and `k = 5`, then you would
find the 5 most popular words in that time period that are hyponyms of both food and cake. Here, the popularity is
defined as the total number of times the word appears over the entire time period requested. The words should then be returned in
alphabetical order. In this case, the answer is `[cake, cookie, kiss, snap, wafer]` if we're
using `top_14377_words.csv`, `total_counts.csv`,
`synsets.txt`, and `hyponyms.txt`.

{: .danger}
Be sure you are getting the words that appear with the highest *counts*, not the highest *weights*. Otherwise, you will run into issues that are very difficult to debug!

Note that if the frontend doesn't supply a year, default values of startYear = 1900 and endYear = 2020 are provided by
`NGordnetQueryHandler.readQueryMap`.

It might be hard to figure out the hyponyms of the words with `k != 0` so we are providing data that is easier to visualize! Below, you'll see a modified version for EECS class requirements, inspired by [HKN](https://hkn.eecs.berkeley.edu/courseguides). We have also provided the data that represents the graph below (`frequency-EECS.csv`, `hyponyms-EECS.txt`, `synsets-EECS.txt`). If someone entered `words = ["CS61A"]`, `startYear = 2010`, `endYear = 2020`, and `k = 4`, you should receive `"[CS170, CS61A, CS61B, CS61C]"`. This `frequency-EECS.csv` is a bit different from the previous one since it has values with the same frequencies. We highly recommend you to take a look at `frequency-EECS.csv`. Also, while you are designing your implementation, bear this in mind that we can give you words with the same frequencies.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FFw2oz5FIMrFRhh9yL8Ylun%2F2C%3Ftype%3Ddesign%26node-id%3D0%253A1%26mode%3Ddesign%26t%3Dn6fDDOrwY4Lb9Gbi-1" allowfullscreen></iframe>


If a word never occurs in the time frame specified, i.e. the count is zero, it should not be returned. In other words,
if `k > 0`, we should not show any words that do not appear in the `ngrams` dataset.
If there are no words that have non-zero counts, you should return an empty list, i.e. `[]`.
If there are fewer than `k` words with non-zero counts, return only those words. For example if you enter the word
`"potato"` and enter `k = 15`, but only 7 hyponyms of `"potato"` have non-zero counts, you'd return only 7 words.

This task will be a little trickier since you'll need to figure out how to pass information around so that the `HyponymsHandler` knows how to access a useful `NGramMap`.

{: .task}
>Modify your `HyponymsHandler` and the rest of your implementation to deal with the `k != 0` case.


{: .warning}
EECS-course guide is not available on the interactive web staff solution so it won't return anything if you give the input `CS61A`.

{: .danger}
>**DO NOT MAKE A STATIC NGRAMMAP FOR THIS TASK!** It might be tempting to simply make some sort of
>`public static NGramMap` that can be accessed from anywhere in your code. This is called a \"global variable\".
>
>We strongly discourage this way of thinking about programming, and instead suggest that you should be passing an
>NGramMap to either constructors or methods. We'll come back to talking about this during the software engineering
lectures.

### Tips

- Until you use the autograder, you'll need to construct your own test cases. We provided one
  in the previous section: `words = ["food", "cake"]`
  , `startYear = 1950`, `endYear = 1990`, `k = 5`.
- When constructing your own test cases, consider making your own input files. Using the large input files we provide is
  extremely tedious.

## Finding Common Ancestors

Up until now, we have only been concerned with finding the common hyponyms of words. For the last part of this project, your task is to find the common *ancestors*.

That is, given a set of words, what words contain the given set of words as hyponyms?

For example, consider `synsets16.txt` and `hyponyms16.txt` from 2B:

![commonAncestors-1](./img/commonAncestors-1.svg)

If we find the ancestors of `"adjustment"`, we should get `"[adjustment, alteration, event, happening, modification, natural_event, occurrence, occurrent]"`, as shown in the graph below.

![commonAncestors-2](./img/commonAncestors-2.svg)

This also should apply to words in multiple contexts, as seen with `"change"`:

![commonAncestors-3](./img/commonAncestors-3.svg)

The ancestors of `"change"` should be `"[act, action, alteration, change, event, happening, human_action, human_activity, modification, natural_event, occurrence, occurrent]"`.

We can also ask for the *common ancestors* of sets of words, which can reveal some neat relationships!

![commonAncestors-4](./img/commonAncestors-4.svg)

Here, we find the common ancestors of the `words = ["change", "adjustment"]`. The result should be `"[event, happening, natural_event, occurrence, occurrent]"`, which are all the words in the graph that contain both `"change"` and `"adjustment"` as hyponyms.

Note that the outputs are in alphabetical order, and keep in mind that `k != 0` can also apply to this task.

**Note**: Be sure to take a *word intersection* rather than a *node intersection* just as in 2B, so the common ancestors of `["test_subject", "math"]` in the following graph should return `"[subject]"`, as `"subject"` contains both `"test_subject"` and `"math"` as hyponyms.

![Common ancestors word intersection](./img/commonAncestors-5.png)

Your query handling needs to remain efficient for common ancestors (i.e., the timeouts applied to 2B still apply here). This means that going through every single word and checking if it contains all the words in the query as hyponyms will be too slow on the larger datasets!

{: .task}

### `NgordnetQueryType`

You will need to modify your `HyponymsHandler` class to account for the *type* of query, i.e., hyponyms or common ancestors. This should look similar to how you found `startYear`, `endYear`, or `k`, and this will be specified for you with `NgordnetQueryType.HYPONYMS` or `NgordnetQueryType.ANCESTORS`, respectively.

{: .task}
>Modify your `HyponymsHandler` and the rest of your implementation to handle common ancestor queries in addition to hyponym queries.

### Design Notes

When designing your project, think about this task in advance. Planning ahead will ensure you don't need to rewrite all of your code when you get to this point.

If you find yourself copy-pasting or repeating a lot of the same code you've already written, there is probably an opportunity to reuse it directly, or slightly modify it so you don't have to repeat yourself as often.

## Deliverables and Scoring

For Project 2C, the only required deliverable is the `HyponymsHandler.java` file, in addition to any helper classes.
However, we will not be directly grading these classes, since they can vary from student to student.

Project 2C will be worth 40 points. The points will be split as follows:

- [Project 2B/C: Checkpoint](https://www.gradescope.com/courses/708063/assignments/4133684): 10 points - Due March 13th
- [Project 2B/C: Design Document](https://www.gradescope.com/courses/708063/assignments/4187810): 5 points - Due March 18th
- Project 2C Coding: 35 points - Due April 1st
   - `HyponymsHandler` popularity-hardcoded: 20%, k != 0
   - `HyponymsHandler` popularity-randomized: 30%, k != 0
   - `HyponymsHandler` common-ancestors: 50%

In addition to Project 2C, you will also have to turn in your design document. The design document's main purpose is to serve as a foundation for your project. It is important to think and ideate before coding.
What we are looking for in the design document:
  - Identify the data structures we have learned in the class that you will be using in your implementation.
  - Pseudocode / general overview of your algorithm for your implementation.

Please make a copy of [this template](https://docs.google.com/document/d/1Vx7QAz4HFN0rEFFEt5rocY2X5AWVcIFFpRmD8vhegOM/edit?usp=sharing) and submit to [Gradescope](https://www.gradescope.com/courses/708063/assignments/4187810).

Don't worry if you decide to change your design document after. You are free to do so! We want you to think about the implementation before coding therefore we require you to submit your design as the part of the project.

The token limiting policy for this project will be as follows: You will start with 8 tokens, each of which has a 24-hour refresh time.

## Testing Your Code

We've provided you with two short unit test files for this project in the `proj2c/tests` directory:

- `TestOneWordKNot0Hyponyms.java`
- `TestCommonAncestors.java`

**These test files are not comprehensive**; in fact, they each only contain one sanity check test. You should fill
each file with more unit tests, and also use them as a template to create two new test files for the respective cases.

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
`proj2c_testing.AutograderBuddy` class that provides a handler that can deal with hyponyms requests.

When you ran `git pull skeleton main` at the start of this spec, you should have received a file called `AutograderBuddy.java`

Just like 2B, open `AutograderBuddy.java` and fill in the `getHyponymHandler` method such that it returns a `HyponymsHandler`
that uses the four given files. Your code here should be quite similar to your code in `Main.java`.

Now that you've created `proj2c_testing.AutograderBuddy`, you can submit to the
autograder. If you fail any tests, you should be able to replicate them locally as JUnit tests by building on the test
files above. If any additional datafiles are needed, they will be added to this section as links.

## Optional Extra Features

If you'd like to go above and beyond in this project (and even explore some front-end development), read through the
[Optional Features](optional_features.md) spec!

## Acknowledgements

The WordNet part of this assignment is loosely adapted from Alina Ene and Kevin Wayne's
[Wordnet assignment](http://www.cs.princeton.edu/courses/archive/fall14/cos226/assignments/wordnet.html) at Princeton
University.
