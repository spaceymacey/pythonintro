# madlibs:

# 1. create a few variables that get certain bits of info from the user

# 2. print out a string with a short story using the info gathered

name = raw_input("name? >> ")
pronoun = raw_input("he or she? >>")
pronoun2 = raw_input("him or her? >>")
place = raw_input("name a room >>")
feeling = raw_input("how are you feeling? >>")
place2 = raw_input("place? >>")
adj = raw_input("adjective >>")
saying = raw_input("favorite phrase? >>")
story = "once upon a time, there was a person called %s. one day, in the %s, %s felt %s. so, %s went to the %s. but, %s %s friend was blocking %s path. %s said: %s " % (name, place, pronoun, feeling, pronoun, place2, pronoun2, adj, pronoun2, name, saying)

print story