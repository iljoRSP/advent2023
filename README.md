# advent2023
my disgusting code for advent of code 2023
<br><br><br>

some comments:
 - tl;dr i can't be bothered to optimise unless i suddenly feel like it
 - ill use regex when i feel like getting annoyed by regex specifically
 - im using python because its easy and comfortable
 - where i can get away with it, i won't use any insane data structures because i can't be bothered
   - not to mention any data structure i come up with will probably be terrible anyway

<br>
<br>

---

<br>
Adding on overall thoughts for each day:

### <u>Day 1</u>
> Part 1 was pretty straight forward, and so I decided to optimise it a tiny bit by scanning outward in. Also just multiplying directly instead of appending strings before parsing, etc. Part 2 is where I scratched my head a bit - I initially was going to replace all the words into digits, before running it through the Part 1 solution... obviously did not proceed with that. I basically gave up and gave in to using regex (lol)

### <u>Day 2</u>
> Very very straight forward, just a bit of string parsing. I considered throwing everything into a (4D?) numpy array and doing "column"-wise operations to do things super fast... but then decided that that would be a pain. So I just used the text to index into a dictionary, works good enough for me!

### <u>Day 3</u>
> Hoo boy. This one was tough - so much so that I feel like I missed a crucial trick of sorts. The biggest hurdle was finding a way to parse the multi-digit numbers - I went through a number of ideas, the most promising being some sort of graph representation - but I ultimately settled on this (overly complicated?) object representation. Storing coordinates using Python's set and just looking for intersections was a tremendous help in rounding this out. This worked pretty well for Part 1, but not as elegantly for Part 2. Wonder what I missed.

### <u>Day 4</u>
> Part 1 is extremely straight forward, and I may have cheated a bit by parsing it with fixed distance instead of delims. "If it works then it's not stupid". Part 2 was hardest in understanding how the chaining worked, but once you get that down, it too is very straight forward. I particularly like how it forces you into dynamic programming - in the sense that if you didn't know what DP was, you might just reach the same implementation anyway. Some may see it as forced, but I choose to see it as 'organic'.

### <u>Day 5</u>
> Day 5 was tough. I'll put it out there. I started part 1 knowing that my approach was an exhaustive search, and that it wasn't going to hold for a larger search space... and boom, part 2 hit me. Thankfully, implementing part 1 already had me reframing the maps as piecewise functions, so I very soon reached my part 2 solution. That said, I chose not to implement it due to burn out from part 1 (somehow), so I kept to proving that the approach would work.

### <u>Day 6</u>
> Comically easy. Working out the mathematics behind this made me feel almost nostalgic for my IGCSE add maths classes (lol). My biggest fear was the possibility of part 2 introducing deceleration, or 2D vectoring - which was thankfully not the case.

### <u>Day 7</u>
> Knowing about python's Counter and sort behaviour, this was pretty easy - it became a problem of just reframing the problem into Counter terms. That said, my approach leaves a lot of room for optimisation. Not much to say about this one.
