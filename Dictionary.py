#Create a dictionary that contains a list of people and one interesting fact about each of them. 
# Display each person and their interesting fact to the screen. Next, change a fact about one of the people. 
# Also add an additional person and corresponding fact. 
# Display the new list of people and facts. Run the program multiple times and notice if the order changes.
# Jeff: Is afraid of clowns. 
#David: Plays the piano. 
#Jason: Can fly an airplane.  

#Jeff: Is afraid of heights. 
#David: Plays the piano. 
#Jason: Can fly an airplane. 
#Jill: Can hula dance.

people={'Jeff':'clowns','David':'piano','Jason':'airplane'}

for index,(name,feature) in enumerate(people.items()):
    
    if index==0:
        print('{} is afraid of {}'.format(name,feature))
    if index==1:
        print('{} Plays the {}'.format(name,feature))
    if index==2:
        print('{} Can fly an {}'.format(name,feature))
        
    
people['Jeff']='height'
people['Jill']='dance'
print()

for index,(name,feature) in enumerate(people.items()):
    if index==0:
        print('{} is afraid of {}'.format(name,feature))
    if index==1:
        print('{} Plays the {}'.format(name,feature))
    if index==2:
        print('{} Can fly an {}'.format(name,feature))
    if index==3:
        print('{} Can hula {}'.format(name,feature)) 
        
print()

#The other way can write the code is
        
def display_facts(facts):
    """Displays facts"""

    for fact in facts:
        print("{}: {}".format(fact, facts[fact]))

    print()

facts = {
    'Jason': 'Can fly an airplane.',
    'Jeff': 'Is afraid of clowns.',
    'David': 'Plays the piano.'
}

display_facts(facts)

facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'

display_facts(facts)