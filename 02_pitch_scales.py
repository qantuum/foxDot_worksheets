# most FoxDot documentation directly jumps to music composition, but does not explain its pitch concept

print(Scale.default)
print(Scale.major)
print(Root.default)

# by default, FoxDot loads the major scale with the degree "0", which is the C5

a1 >> pluck()

# This simple "SynthDef" (more on this later) plays a C5.
# C5 actually is a piano C3. FoxDot octaves are written 2 octaves higher than the usual notation we know.
# The default note duration of SynthDefs (excl. play) is 1 (=1 beat).
# We will keep practicing on the pluck synth, and show some "attributes" relevant to pitch.

Clock.clear()
Scale.default.set("chromatic")

# before using the major scale, let's see how the chromatic scale is built.

print(Scale.default)

# It will return a "list". A list is a python object presenting ordered items.
# The list has items from left to right, separated by commas, inside brackets.
# Here, it shows all the pitches from 0 to 11.
# Since our root is the C3, 0 is C and 11 is B.
# This list of pitches comes from our "tuning", the division of the octave (2/1 interval) in 12. More on this later.

Clock.meter=(12,4)
a1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],start=nextbar).after(12,"stop")

# Now I want to raise the possibility of writing decimal numbers.
# You'll end up with notes "in-between" right? Already enough to change a sound completely.
# Also related to tunings, so keep that in mind.
# Don't mind the extra instructions here, they are here to make it play once, start to end.

Clock.meter=(7,4)
a1 >> pluck([0, 0.5, 0.9, 1.2, 1.5, 2, 2.2],start=nextbar).after(7,"stop")

# Just a sweet little curiosity.
# What we learn here, is the chromatic scale is the biggest set of our tuning, each interval we know and love has an assigned index.
# Unison is 0, minor 2nd is 1, major 2nd is 2, minor 3rd is 3, major 3rd is 4, perfect 4th is 5, and so on.
# But notes in-between can still be played with decimals, and this quirk will come to help us later!

Clock.clear()
Scale.default.set("major")
print(Scale.major)

# Now, the pattern that we see for major: [0, 2, 4, 5, 7, 9, 11]
# let's hear it!

Clock.meter=(8,4)
a1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7],start=nextbar).after(8,"stop")

# B... But! Why don't we use the 0, 2, 4, 5...?
# That's because the ajor is a subset of chromatic. We select the nth item of the chromatic scale as to only get major.

# From now on, every pitch that plays will fit in this major scale!
# 0, 2, 4 = whole note, 5, 7, 9, 11 = whole tone, 4, 5 = semi-tone, 11, 0 = semi-tone.

Clock.meter=(9,4)
a1 >> pluck([0, 1, 2, 3, 4, 4.5, 5, 6, 7], start=nextbar).after(9,"stop")

# That's right. By using the decimal that falls in the middle of 4 and 5, we retrieve the note that had index no. 8 in the chromatic, ie. our minor 6th.
# So, it is possible to figure out the right decimal number that can produce a chromatic note while still being in a specific scale.
# It can come in handy for any modal modulation you would want.

Clock.meter=(9,4)
a1 >> pluck([0, 1, 2, 3, 4, 4.25, 5, 6, 7], start=nextbar).after(9,"stop")

# You can also come the same exotic values as before. Here 4.25 means our minor 6th is flattened (again!) by a quarter-tone.

a1 >> pluck (freq=1000)

Clock.meter=(4,4)
Scale.default.set("major")
Root.default.set(0)
print(Root.default)

# You also can set your default root to another degree, here we set it to C (0).

a1 >> pluck([0,1,2,3],dur=1)
a2 >> pluck([0,1,2,3],root=-3,scale=Scale.minor)

# Here, we asked the second player to play in A minor, the relative minor of C major.

a1 >> pluck([0,1,2,3])
a2 >> pluck([0,1,2,3],root=9,oct=4,scale=Scale.minor)

# We can inform an octave attribute, too. Here, a root of -3, and a root of 9 with a lowered octave, both mean it's going tro be an A4.

Clock.clear()
a1 >> pluck((0,5,7),dur=4)

# congratulations, you just have played your first chord! The syntax for chords is just separate numbers between parentheses.

# That's about it for now.
# Pitch construction in FoxDot can be really fun because it has a lot of tools to move in different directions.

# Summary:
#  Scale.default
#  Root.default
#  The chromatic scale.
#  The pitches "in between" the chromatic scale.
#  How scales are subsets from the chromatic scale.
#  How to pull chromatic notes from a given scale. hint: it's decimal numbers.
#  How to play with different scales.
#  The octave attribute.
#  How to write chords.

# exercise: now try to figure out which scale degree equals which pitch.
