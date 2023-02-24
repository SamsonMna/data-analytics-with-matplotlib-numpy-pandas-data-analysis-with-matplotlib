my_name = 'Zed A. Shaw'
my_age = 24 # Not a lie
my_height = 74 # Inches
my_weight = 180 # Pounds
my_eyes = 'Red'
my_teeth = 'Cream'
my_hair = 'Black'

print("let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("He's teeth are usually %s depending on the coffee.\n" % my_teeth)

# This line is a little bit tricky, try one's best to get it right.
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

x = ("There are %d types of people." % 10)
binary = ("binary")
do_not = ("don\'t")
y = ("Those who know %s and those who %s." % (binary, do_not))

print(x, y)
print ("I said: %r." % x)
print ("I also said: \'%s\'." % y)


