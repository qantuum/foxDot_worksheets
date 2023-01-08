# Tuning is often taken for granted in music production because the tuning we all know and love is ET12
# also called 12-equal temperament, or division of the octave in 12 (12-EDO).
# it consists of 12 pitches, C, C, D, D#, E, F, G, G#, A, A#n and B, repeating over all the octaves
# A measurement unit represent pitches, it is called the cent. The cent is a logarithmic measure for intervals ratios.
# The interval ratio relative to octave is 2/1, and it is equal to 1200 cent.

print(Tuning.ET12)

# In FoxDot, a simplified version of cents is used, it divides the real cent value by 100.
# So when we use a scale, we really ask FoxDot to choose a specific note from our scale, that will pick a note in our tuning,
# then convert it to a frequency.

print(Scale.chromatic)
print(Scale.major)
print(Scale.default)
print(Root.default)

a1 >> pluck(degree=2)

# the degree attribute is used to call pitches. If it is placed first, it is implied.

a1 >> pluck(2)

a1 >> pluck(dur=1,2)

# what happened? The degree only is implied as attribute when it is placed first.

a1 >> pluck(2, dur=1)

# When I ask my player to play the pitch no. 2 of the  C major scale (current default),
# it will look for pitch no. 4 of my C chromatic scale, which corresponds to 400 cents, or E.

help(Tuning)

# Tuning is a very small FoxDot class with no methods of its own.
# You can observe it contains two other tunings, with different cent values.
# It is convenient that ET12 is just the list of integers from 0 to 11, but non-integers are valid too, as you can see.

# The player seems to be fetching the right pitch value certainly thanks to a scale operation. Examples:
    
a1 >> pluck([0,0.5], scale=Scale.major)

# 0 and 1 on the major scale are 0 and 2 on the chromatic scale.
# A distance between 0 and 1 on the major scale becomes a distance between 0 and 2 in the chromatic scale, so everything is multiplied by 2:

a1 >> pluck([0,1], scale=Scale.chromatic)

# So in our example, a pitch no. 0.5 on the major scale is simply the no.1 of the C chromatic scale: C#.

a1 >> pluck([0,0.25], scale=Scale.major)

a1 >> pluck([0,0.5],scale=Scale.chromatic)

# In the same manner, here we have a half-sharp C, also defined as 50 cent.

a1 >> pluck([0,0.3333333],scale=Scale.chromatic)

a1 >> pluck([0,0.25],scale=Scale.chromatic)

a1 >> pluck([0,0.125],scale=Scale.chromatic)

a1 >> pluck([0,0.06],scale=Scale.chromatic)

a1 >> pluck([0,0.02],scale=Scale.chromatic)

# In the same manner, we have built the intervals of 0 to 33.3333 cent, 25 cent, 12.5 cent, 6 cent and 2 cent.
# 6 cent is theorized to be the lowest threshold until human ear can detect a pitch difference.

a1 >> pluck((0,0.08),pan=(-1,1),amp=(1,0.8))

# We can also use slight de-tunings to add a texture to our sound.
# This is already a step in the sound design part of our FoxDot tutorials.

# As it is, our tuning list and chromatic scale list are the same:
    
print(Scale.chromatic)
print(Tuning.ET12)

# but you notice a letter P next to the list of chromatic pitches. This is called a Pattern in FoxDot and allows new operations on typical python lists. More on it later.

print(Scale.names())

# This is the list of all the scales loaded by default in the Scale class. Each of them have a list of pitches just as chromatic and major.
# You can recognize the pentatonic scales and the modes for example.

Scale.my_new_scale=ScalePattern([0,1,2,3,3.5,6,8,8.5], name="my_new_scale")
print(Scale.my_new_scale)
print(Scale.names())

# Edits to Scale only are added to your program, not to the default Scale class.
# The usual guideline in scales is to never go above the tuning (or chromatic)'s maximum, which in C chromatic is no.11 (B).
# Changing octaves is performed using higher degrees in your player, or by simply moving around the octave attribute.
# To display all the things scales, you can call:
    
help(Scale)

# You can generally call the help on any class, like Tuning and Scale. Other classes are Pattern and SynthDef.

a1 >> pluck([-7,0,8,15],scale=Scale.minor,tuning=Tuning.bohlen_pierce)

a2 >> pluck([-7,0,8,15],scale=Scale.minor,tuning=Tuning.ET12)

# Now for something a bit more technical, how is a tuning created in FoxDot?
# It might be harder to hear when the two players play together, but the Bohlen-Pierce tuning has a noticeable dissonance in octaves.
# That is because Bohlen-Pierce is built about the repetition of a tritave (octave+perfect 5th or perfect 12th or 3/1).
# The Scale class mentions this:
# bohlen_pierce = TuningType([i*12/13*math.log(3, 2) for i in range(14)])
# so it seems there is a class called TuningType that can input new Tunings.
# in this case we use the 2^logarithm of 3 with 13 pitches, because it divides the 3/1 interval in 13 pitches.
# The 2^ logarithm is crucial to the conversion in cents, if you want the full formule go there:
# http://hyperphysics.phy-astr.gsu.edu/hbase/Music/cents.html
# more info on Bohlen-Pierce there: https://en.xen.wiki/w/13edt

# Anyway, creating alternative tunings on FoxDot is not impossible but needs to create extra classes. It is one of my other projects.

# Summary:
#  beyond behind the Scale class
#  discovery of alternative tunings
#  microtonal notes
#  cents
