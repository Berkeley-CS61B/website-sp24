---
layout: page
title: >-
  FAQ
parent: >-
  Lab 07: LLRBs
grand_parent: Labs
has_right_toc: true
released: true
---

### Why does the root of an LLRB tree always need to be black (note: this only applies if we use colored nodes as our representation instead of links)?

Check out the [LLRB Properties](index.md#llrb-tree-properties) section in the
spec. The root node could technically be colored red and considered to be a
special case, but for consistency with the other nodes and LLRB tree
properties, we choose to require that it is colored black.
