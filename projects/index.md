---
layout: page
title: Projects
nav_order: 5
nav_exclude: false
has_children: true
has_toc: false
has_right_toc: false
---

# The Pac-Man Projects

<img style="display:block;margin-left:auto;margin-right:auto" src="{{ "/assets/images/pacman_game.gif" | relative_url }}">

{:.no_toc}

## Overview

The Pac-Man projects were developed for CS 188. They apply an array of AI techniques to playing Pac-Man. However, these projects don’t focus on building AI for video games. Instead, they teach foundational AI concepts, such as informed state-space search, probabilistic inference, and reinforcement learning. These concepts underly real-world application areas such as natural language processing, computer vision, and robotics.

We designed these projects with three goals in mind. The projects allow you to visualize the results of the techniques you implement. They also contain code examples and clear directions, but do not force you to wade through undue amounts of scaffolding. Finally, Pac-Man provides a challenging problem environment that demands creative solutions; real-world AI problems are challenging, and Pac-Man is too.

## Projects Overview

### Project 0: Python, Setup, & Autograder Tutorial

This short tutorial introduces students to setup examples, the [Python](http://www.python.org/) programming language, and the autograder system.

### Project 1: Search

Students implement depth-first, breadth-first, uniform cost, and A\* search algorithms. These algorithms are used to solve navigation and traveling salesman problems in the Pacman world.

### Project 2: Logic

Pacman world is represented with booleans, and logical inference is used to solve planning tasks as well as localization, mapping, and SLAM.

### Project 3: Multiagent Search

Classic Pacman is modeled as both an adversarial and a stochastic search problem. Students implement multiagent minimax and expectimax algorithms, as well as designing evaluation functions.

### Project 4: Reinforcement Learning

Students implement Value Function, Q learning, and Approximate Q learning to help pacman and crawler agents learn rational policies.

### Project 5: Bayes Nets and HMMs

Pacman uses probabilistic inference on Bayes Nets and the forward algorithm and particle sampling in a Hidden Markov Model to find ghosts given noisy readings of distances to them.

### Project 6: Machine Learning

Students implement the perceptron algorithm, neural network, and recurrent nn models, and apply the models to several tasks including digit classification and language identification.

## Technical Notes

The Pac-Man projects are written in pure Python 3.6+ and do not depend on any packages external to a standard Python distribution, except the Logic and ML projects.

## Support

This project was supported by the National Science foundation under CAREER grant 0643742. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation (NSF).

## Credits

The projects were developed by John DeNero, Dan Klein, Pieter Abbeel, and many others.
