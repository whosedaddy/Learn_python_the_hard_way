name ='Sun Ao'
age = 20#not a lie
height=74#inches
my_height=height*2.54#centimeter
weight=180#lbs
my_weight=weight*0.4535924#kilogram
eyes='black'
teeth='white'
hair='Brown'

print "Let's talk about %s."%name
print "He's %d inches tall,namely %g."%(height,my_height)
print "He's %d pounds heavy,namly %f."%(weight,my_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."%(eyes,hair)
print "His teeth are usually %s depending on the coffee."%teeth

# this line is trick,try to get it exactly right
print "If I add %d, %d,and %d I get %d."%(
    age,height,weight,age+height+weight)