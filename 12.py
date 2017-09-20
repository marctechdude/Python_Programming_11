

story = '''
Hold it {}!
{}. But! {} only if ye be {} of valor!
For {} is guarded by a {} so {}, so {}, that no {} yet has {} with it... and {}!
'''

def main():
    command = input("Enter a command (e.g. Sleep): ")
    plural_noun = input("Enter a plural noun (e.g. trees): ")
    animal = input("Enter an animal (e.g. cow): ")
    location = input("Enter a location (e.g. Surrey OR the playground: ")
    # YOU DIDNT USE singular_noun 
    singular_noun = input("Enter a singular noun (e.g. tree): ")
    person_name = input("Enter the name of a person.")
    # NICE! HOW YOU SIMPLIFIED - NO APPEND 
    adjectives = [input("Enter an adjective (e.g. big): "), input("Enter another adjective: ")]
    adverb = input("Enter an adverb (e.g. slowly): ")
    past_participle = [input("Enter a past participle (e.g. played): "), input("Enter another past participle: ")]

    mad_lib = story.format(person_name,
                           command,
                           command,
                           plural_noun,
                           location,
                           animal,
                           adjectives[0],
                           adjectives[1],
                           adverb,
                           past_participle[0],
                           past_participle[1])
    print(mad_lib)

main()
