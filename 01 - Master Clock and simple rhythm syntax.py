# this worksheet aims to cover how the master Clock works, and to acknowledge some percussive rhythm syntax possibilities on FoxDot.
# In a word, this is a starter class for rhythms in FoxDot.
# what's a FoxDot: https://github.com/Qirky/FoxDot
# --------------------------------------------
# Please evaluate these lines using Ctrl+Enter

print(Clock.bpm)

# shows current bpm, default is 120

print(Clock.meter)

# shows current meter, default is (4,4)

print(Clock.bar_length())

# shows the length of one bar, in beats. If the meter is (4,4), then it is 4, if it is (3,4), it is 3, etc.
# Irrational meters like (8,12) will return irrational bar lengths because the bar length calculation depends exclusively on the number of 1/4th notes (beats) in one bar.

Clock.bpm = 110

Clock.meter = (4, 4)

# If you want to change your tempo and time signature, it is here.
# Spaces only add better reading but they can be removed.
# The time signature does not affect your note durations. All the durations for note are based on the 1/4th note (=1 beat).

a1 >> play("x---")

# the ">>" represents a line of code that will emit sound.
# "play" or the player, is the dedicated sampler of FoxDot, it fetches wav files according the the input characters.
# x is a kick drum, - is a closed hat. A cheatsheet is found at: http://lesporteslogiques.net/wiki/_media/ressource/logiciel/foxdot_troop/foxdot_cheat_sheet.pdf.
# you can also see all the Samples by printing the sample list to your log.
# all the characters are placed between quotation marks.
# player has a default duration of 1/2 beat.

Clock.clear()
print(Samples)

# Clock.clear() stops all players in the stack.
# You can visualize your beats on the clock by ticking "toggle beat counter" in the Edit menu.
# Clock.clear can be triggered by the shortcut Ctrl+. (yes, the dot character)

a1 >> play("x---")

# evaluate the following line after a while:

a2 >> play("o:::")

# This is where the time signature is important. If you evaluate a line while others are being played,
# the app waits for the relevant bar to be completed before adding the new player to the stack.
# In this case, the o (snare drum) will fall in line with the kick because both patterns have the same duration.
# Since the default duration of player is 1/2, the pattern "x---" only spans 2 beats. The complete bar in (4,4) is 4 beats.

Clock.clear()

# Did you use the shortcut? Very good.

a1 >> play("x o ")

# you can use dots or spaces to do placeholder. Doing so makes it your kick and snare will hit on beats 1 and 2, rather than 1 and "and".
# I came to prefer a dot for better readability.

a1 >> play("x.o.")

# you also can update your duration "attribute", it is called "dur". It defaults to 1/2, we will take it to 1. More on attributes in later worksheets.

a1 >> play("xo", dur=1)

# All three lines produced the same output.
# If you want, you can update your player duration so it returns to 1/2:

a1.pitch = "x.o."
a1.dur = 1/2

# pitch is also an attribute. Now we are using it to update phrases oustide of the play statement, but there's more to it later.

Clock.clear()
Clock.set_time(0)

# This will also put the clock back to 0, it is useful when you run a clear and a new player on the same block.

a1 >> play("x.o.")
a2 >> play("----")

# Did you notice? If you use Ctrl+Enter on lines with no separation, they are ran together.
# You can also evaluate single lines using Alt+Enter.

Clock.clear()
Clock.set_time(0)
a1 >> play("<x.o.><---->")

# You can use the angle brackets to layer to distinct phrases in one player.
# Plays the same as before with a1 and a2.

Clock.clear()
Clock.set_time(0)
a1 >> play("x.[oo].")

# You can use the brackets to divide your rhytm in the number of characters present.
# Here it is [oo], 2 characters, so it will play two 16th notes.

a1.pitch = "x.[ooo]."

# now it will play 8th triplets.

Clock.bpm=158
Clock.clear
Clock.set_time(0)
a1 >> play("(x.)(.x)o.", dur=1/2)

# Isn't this the basic rhythm of drum'n'bass?
# Well you've just used the parentheses to "lace" your samples.
# What it does is distributing the different parenthesed patterns one-by-one with the remainder of the pattern.
# In this case, it starts with "x.o." and ends with ".xo.", added together it makes "x.o..xo."
# You can chain lacing from left to right or from right to left:

Clock.bpm=110
Clock.clear
Clock.set_time(0)
a1 >> play("---(-=)")

# This lacing can also be used to shorten the writing of an otherwise longer pattern.
# For example here, the pattern goes "---" and then "---" and then "-=", for a total of "-------=" (1 bar)

Clock.clear()
Clock.set_time(0)
a1 >> play("x.{ox}.")

# The curly brace works more like a selector, it selects at random the characters you've fed it.

a1 >> play("x.{o[oo]}.")

# It can also circle through either normal characters or characters in brackets.

a1 >> play("<x.o.><s..s..>")

# This is how simple it is to run polymeters in FoxDot.
# The two patterns have different lengths and eventually will catch up on beat no. 6 (= 4 x 1/2 x 6 x 1/2).
# Do you remember the angle brackets? Good.

a1 >> play("<x.o.><->")

# You can also use this property to remove unneeded info.
# In this example from before, now I just place a "-" rather than 4, because I know they will be looped anyway.

a1 >> play("<xo><[---]>", dur=1)

# you can also play polyrhythms just as easy.

# That's what we get for now, try re-creating your favourite rhythms!
# Summary:
#  Clock.bpm
#  Clock.meter
#  print(Samples)
#  default note length in the player: 1/2 (= 1/8th note)
#  a1 >> play("x"), the sample symbols always are between quotation marks.
#  a1 >> play("<x.o.><->"), you can layer multiple patterns using angled brackets.
#  a1 >> play("x.[oo]."), the brackets allow to divide note length by how many characters there are in there.
#  a1 >> play("(x.)(.x)o."), the parentheses allow to lace patterns.
#  a1 >> play("x.{ox}."), the curly braces act as a selector between different characters, selects them at random for variety.
#  you can use all these brackets and separators interchangeably to experiment and maybe find the next rhytm to recreate on your DAW.
#  polymeters and polyrhythms also are simple to program with these tools.

# Examples of elaborate rhythms possible with FoxDot syntax, all taken from Tutorial 03, found in the Tutorials menu:

a1 >> play("x-o[--------------]")

a1 >> play("x-o{-=[--][-o]}")

a1 >> play("(x[--])xu[--]")

a1 >> play("<X.x.><.-..><..#.><...V>")
