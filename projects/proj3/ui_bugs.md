---
layout: page
title: "Common UI Bugs - Project 3: BYOW"
nav_order: 2
parent: >-
   Project 3: BYOW
grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
   Project 3 Common UI Bugs.
released: false
---

## Invisible Text

Getting text to show up on screen can be somewhat tricky. Several things need to
go right:
 - the font color needs to be set to something visible (i.e. white)
 - the location of the text needs to be in bounds
 - you need to call `StdDraw.show()` after the text is drawn so it shows up
   on screen
 - you need to make sure that your text does not get drawn over or cleared right
   after it is drawn (for example, `TERenderer.renderTiles` clears the entire
   screen)

Here's some code that should correctly draw text:
```java
TERenderer ter = new TERenderer();
ter.initialize(80, 40, 0, 0);
StdDraw.setPenColor(Color.WHITE);
StdDraw.text(40, 30, "I like cheese");
StdDraw.show();
```


## Strange Tiles

### The Problem

One common glitch is that after implementing other parts of the UI, the tile
characters will suddenly misbehave. [Here's a program](./FlowerWorld.txt)
that demonstrates the problem; paste this in your `core` folder if you want to
follow along.

You'll notice that the flowers no longer look like flowers anymore. This is
because the font size is much too large, so the characters for each tile are
spilling into the other tiles.

### The Solution

The problem is that the tiles are being drawn with too large a font size, so
we'll create a method that resets the font size. Create this method in your
TERenderer class:

```java
/** Sets the font to the correct font for drawing tiles */
public void resetFont() {
    Font font = new Font("Monaco", Font.BOLD, TILE_SIZE - 2);
    StdDraw.setFont(font);
}
```

Then, call the method before you draw the tiles:

<table>
    <thead>
        <th>Before</th>
        <th>After</th>
    </thead>
<tr>
<td markdown="block">

```java
// render frame
ter.renderFrame(tiles);
```
</td>
<td markdown="block">

```java
// render frame
ter.resetFont();
ter.renderFrame(tiles);
```
</td>
</tr>
</table>

Now, when you run `FlowerWorld` the tiles should be drawn correctly.


## Flickering UI

### The Problem

One common glitch is a flickering UI. [Here's a program](./WaterWorld.txt)
that demonstrates the problem; paste this in your `core` folder if you want to
follow along.

You'll notice the text "HUD goes here" should flicker. The reason why is because
there are multiple `StdDraw.show()` calls per frame - one inside the `renderFrame`
call, and one on line 31. This means that there are actually two frames being
drawn on screen every loop: one without the text, and one with the text. It's
somewhat random which frame you see, which is why the UI flickers between the
two.

### The Solution

The problem is that there's an extra `StdDraw.show()` call inside `renderFrame`,
so we'll create a version of that method without it. Create this method in
your `TERenderer` class:

```java
    /**
     * Like renderFrame, but does not clear the screen or show the tiles
     */
    public void drawTiles(TETile[][] world) {
        for (int x = 0; x < world.length; x += 1) {
            for (int y = 0; y < world[x].length; y += 1) {
                world[x][y].draw(x + xOffset, y + yOffset);
            }
        }
    }
```

Then, replace the `renderFrame` call in the main game loop:


<table>
    <thead>
        <th>Before</th>
        <th>After</th>
    </thead>
<tr>
<td markdown="block">

```java
// main game loop
while (true) {
    ter.renderFrame(tiles);
    ...
}
```
</td>
<td markdown="block">

```java
// main game loop
while (true) {
    StdDraw.clear(Color.BLACK);
    ter.drawTiles(tiles);
    ...
}
```
</td>
</tr>
</table>

Now, when you run `WaterWorld` the text should no longer flicker.
