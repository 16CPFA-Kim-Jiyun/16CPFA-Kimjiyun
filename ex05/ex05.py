her_name = 'Jina'
her_age = 28 # not a lie
her_height_cm = 155
her_weight_kg = 50
her_eyes = 'Black'
her_teeth = 'White'
her_hair = 'Black'

print "Let's talk about %s." % her_name
print "She's %d centimeters tall." % her_height_cm
print "She's %d kilograms heavy." % her_weight_kg
print "Actuallythat's not too heavy."
print "She's got %s eyes and %s hair." % (her_eyes, her_hair)
print "Her teeth are usually %s depending on the coffee." % her_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (her_age, her_height_cm, her_weight_kg, her_age + her_height_cm + her_weight_kg)
