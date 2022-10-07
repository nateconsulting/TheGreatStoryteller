from nltk.corpus import names 
from nltk.corpus import wordnet as wn
import random 
import json

story_start = "Once upon a time, "

class NoWords:
    def __init__(self):
        self.all_adjectives = []
        self.adj_ant_dict = {}

        for i in wn.all_synsets():
            if i.pos() in ['a', 's']: # If synset is adj or satelite-adj.
                
                for j in i.lemmas(): # Iterating through lemmas for each synset.
                    self.all_adjectives.append(j.name())
                    if j.antonyms():
                        self.adj_ant_dict[j.name()] = j.antonyms()[0].name()

        self.all_char_desc = open('char_desc.txt').read().splitlines()


    def get_adjective(self):
        an_adjective = random.choice(self.all_adjectives)

        return an_adjective


    def get_adj_ant_list(self):
        an_adj, an_ant = random.choice(list(self.adj_ant_dict.items()))
        rand_adj_ant = [an_adj,an_ant]

        return rand_adj_ant


    def get_char_desc(self):
        a_char_desc = random.choice(self.all_char_desc)

        return a_char_desc


class NoName:
    def __init__(self):
        self.male_names = names.words('male.txt')
        self.female_names = names.words('female.txt')
        self.all_names = self.female_names + self.male_names

    def get_any_name(self):
        a_name = random.choice(self.all_names)

        return a_name
    
    def get_male_name(self):
        male_name = random.choice(self.male_names)

        return male_name


    def get_female_name(self):
        female_name = random.choice(self.female_names)

        return female_name


class NoWhere:
    def __init__(self):
        self.all_places = open('places.txt').read().splitlines()
        self.all_directions = open('directions.txt').read().splitlines()

        
    def get_place(self):
        a_place = random.choice(self.all_places)

        return a_place


    def get_direction(self):
        a_direction = random.choice(self.all_directions)

        return a_direction


class NoBody:
    def __init__(self):
        self.all_beings = open('beings.txt').read().splitlines()


    def get_being(self):
        a_being = random.choice(self.all_beings)

        return a_being


class NoAction:
    def __init__(self):
        self.all_actions = open('actioning.txt').read().splitlines()
        self.last_action = None


    def get_action(self):
        an_action = random.choice(self.all_actions)
        while self.last_action == an_action:
            an_action = random.choice(self.all_actions)

        self.last_action = an_action

        return an_action


class NoFeeling:
    def __init__(self):
        self.all_feelings = open('feelings.txt').read().splitlines()
        self.current_feeling = None

        with open('feeling_because.json') as json_file:
            self.feeling_because = json.load(json_file)


    def get_feeling(self):
        a_feeling = random.choice(self.all_feelings)
        while self.current_feeling == a_feeling:
            a_feeling = random.choice(self.all_feelings)

        self.current_feeling = a_feeling

        return a_feeling


if __name__ == '__main__':
    nn = NoName()
    nwh = NoWhere()
    nwo = NoWords()
    nb = NoBody()
    na = NoAction()
    nf = NoFeeling()

    story_start = "Once upon a time, "

    for i in range(25):
        main_char_name = nn.get_any_name()
        main_char_being = nb.get_being() 

        print('============================================')
        story_string =  story_start \
            + nwo.get_char_desc() \
            + " "+ main_char_being \
            + " named " \
            + main_char_name \
            + " was " \
            + na.get_action() \
            + " " + nwh.get_direction() \
            + " the " + nwh.get_place() \
            + ".  " \
            + main_char_name \
            + " was feeling " \
            + nf.get_feeling() \
            + " because " \
            + nf.feeling_because[nf.current_feeling][random.choice([0,1,2])] \
            + ".  "

        print('\n============================================\n')
        print(story_string)