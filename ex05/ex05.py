her_name = 'Jina'
her_age = 28 # not a lie
her_height_cm = 155.2
cm_to_inch = 1.0 / 2.54
her_height_inch = her_height_cm * cm_to_inch
her_weight_kg = 50
kg_to_pound = 1.0 / 0.453
her_weight_pound = her_weight_kg * kg_to_pound
her_eyes = 'Black'
her_teeth = 'White'
her_hair = 'Black'
# place holder
print "Let's talk about %s." % her_name
print "She's %g centimeters tall." % her_height_cm
print "She's %g inches tall." % her_height_inch
print "She's %d kilograms heavy." % her_weight_kg
print "She's %d pounds heavy." % her_weight_pound
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (her_eyes, her_hair)
print "Her teeth are usually %s depending on the coffee." % her_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (her_age, her_height_cm, her_weight_kg, her_age + her_height_cm + her_weight_kg)
