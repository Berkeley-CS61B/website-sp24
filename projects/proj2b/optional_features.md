---
layout: page # The HTML template to use to render this page.
title: "Project 2B Optional Features" # Title of page.
categories: proj
released: true # you have to also change this to true to release.
---

## Getting Started

The remainder of this assignment is optional, but strongly recommended.

This portion of the project combines the powers of `NGramMap` (project 2a) 
and `WordNet` (project 2b). To get started, copy `HistoryHandler`, 
`HistoryTextHandler`, `NGramMap`, and `TimeSeries` from project 2a into
project 2b. You should also adjust `Main.java` so that it registers all
three handlers.

## Adding New Buttons

Getting a list of hyponyms is cool, but what can sometimes be even cooler is plotting their relative frequencies. For
example, if the user enters the words "food, cake", startYear = 1900, endYear = 2020, k = 8 and clicks "Hypohist",
they'd be able to see the relative frequency of the 8 most popular words which were hyponyms of food and cake over the
time period between 1900 and 2020.

In this part, you'll edit three different types of files:

- HTML
- JavaScript
- Java

We assume that you have NO prior familiarity with HTML or JavaScript. It is very common in real-world projects to have
to modify code with which you are not familiar, even possibly in programming languages you have never seen.

### Adding the Hypohist Buttons

Open the `ngordnet.html` file. Locate the code that creates the existing buttons, e.g. `History` and `Hyponyms`. Using
your intuition, copy and paste the pieces of code that you think are necessary to create two new buttons that say
"Hypohist" and "Hypohist (text)".

When you're done, try clicking the Hypohist button, and nothing will happen.

### Creating a Hypohist Handler

Back in `Ngordnet.main.Main`, register a new Handler called `HypohistHandler`. It should be registered to the String
`hypohist`. This handler should simply return the text "hello i am hypohist". Run your Java server, and it is now ready
to listen for Hypohist clicks.

With your server running, try clicking the Hypohist button, and ... still nothing will happen!

### JavaScript Callbacks

Even though our server is listening for Hypohist clicks, and we are clicking the Hypohist button, nothing is happening!

That is, your browser isn't even trying to send the query over to your Java file. This is because HTML code is generally
dumb, i.e. basically doesn't do anything but specify what the website should look like.

The language typically used to describe how a page works is called JavaScript. Despite the name, it has literally
nothing to do with Java, and is widely believed to have been a marketing ploy (see
[this page](https://www.webucator.com/article/why-javascript-is-called-javascript/) or
[this video by JavaScript's creator Brendan Eich](https://www.youtube.com/watch?v=XOmhtfTrRxc&t=125s)) in the mid-1990s
when Java was new and cool, and JavaScript was just coming into existence.

Let's peer inside the dark universe of front-end JavaScript programming. Open "ngordnet.js". This is the code that acts
as the middleman between the beautiful (?) visual user interface in the browser and your Java code. Note that the HTML
and Javascript files for this project are not up to professional standards, and I honestly hacked them together pretty
quickly, keeping them as simple as possible so you would feel at least slightly comfortable playing around with them.

Your difficult task: Try modifying the code so that when you click the "Hypohist" button, you successfully get back the
text outputted by your `HypohistHandler`, which should be "hello i am hypohist" if you used my exact suggestion above.

The very old-school word for this process of just fumbling your way through a quick and dirty programming job is
"hacking", though the word has many competing meanings these days.

Tips:

- Pattern match carefully!
- Feel free to edit, test, and experiment. You're not going to break anything permanently.
- Use git checkout to get the original version of the JS file if you break something.
- Don't cheat by just asking someone what to do. This skill of editing and experimenting with code you don't understand
  is VERY important when prototyping and hacking together code.
- In the real world, production code should never ship that was created via this hacking process. However, it can be
  very useful for prototyping!

### Hypohist

Next, fill out the handler for the Hypohist button so that it behaves as expected, that is, this button should return a
plot of the relative frequency of the words returned by Hyponyms over the period stated.

That is, we'll do what we said above: For example, if the user enters the words `"food, cake"`, sets `startYear=1900`,
`endYear=2020`, and `k=8`, and clicks the "Hypohist" button, they'd be able to see the relative frequency of the 8 most
popular words which were hyponyms of food and cake over the time period between 1900 and 2020.

Note: Behavior is pretty straightforward if k > 0 for Hypohist. If k = 0, it's not clear what should happen. Maybe come
up with a cool idea.

<!--
### Optional: Hypohist with 0 K

If K is 0, instead of plotting the k most popular hyponyms, you should plot the total weight history of all words which
are hyponyms of the given words. For example, if the user enters "food, cake", startYear = 1900, endYear = 2020, k = 8,
then we'd see a plot of "cat" and "dog", where the cat represents the total weight of ALL hyponyms of cat, and "dog"
represents the total weight of ALL hyponyms of dog.

Note that the web front end sets k to zero if the value is missing.
-->

<!--
### Hypohist (text)

This is a bit less intresting, but you might find it interesting to return the

Lastly, modify the HTML, javascript, and Java code so that there is a new Hypohist (text) button. This button should
return a text display similar to History (text), but for the hypohists as described in the previous section.
-->

<!--
## Discovering Something Interesting

Lastly, once you've properly implemented all features of this assignment, you should use either the `history`,
`hyponyms`, or `hypohist` button to discover something interesting. When you've found something, submit your result
using this Google form (coming soon).

-->

## Adding Even More Features

Optionally, add even more features to your tool. Some possibilities:

- Adding additional buttons that use one or both datasets in some creative way. For example, you might plot the average
  length of all words in a given year. Or you might create a visualization of all of a words' hyponyms. Or you might
  have a feature that prints the shortest path between two words.
- The hyponyms search finds all hyponyms, no matter how distant from the source. For example, there are a huge number of
  hyponyms of "dog". Add a new field d, which finds only words that are at a distance of d or less from the given words.
- Have a ! operator, e.g. if someone enters "!person, leader", your code will find all leaders which are not a person.
