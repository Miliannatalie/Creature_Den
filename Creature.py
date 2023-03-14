import os
from random import randint, sample
import logging
from mongoengine import *
from filler_creatures import creatures, abilities

logging.basicConfig(level=logging.DEBUG)

# Ojala mi internet fuera asi

class Ability(Document):
    name = StringField(required=True, unique=True)
    effect_stat = IntField()
    effect_status = StringField()

    description = StringField()

    meta = {'strict': False}


class Creature(Document):
    name = StringField(required=True, unique=True)
    image = StringField()

    hp = IntField(default=50, required=True)
    attack = IntField(required=True)
    defense = IntField(required=True)
    speed = IntField(required=True)
    ability = ReferenceField(Ability)
    description = StringField()
    lore = StringField()

    meta = {'strict': False}

    def __repr__(self):
        ability_name = self.ability.name if self.ability else "No Ability yet"
        return f"<Creature {self.name} - Atk {self.attack}: {ability_name}>"


if os.getenv("USE_LOCAL"):
    connect("Creatures")
    logging.debug("Running in the cloud.")
else:
    connect(host=os.getenv("CREATURE_DEN_DATABASE_URL"))

Creature.drop_collection()
Ability.drop_collection()

# Your code goes here
a = Ability(name="Eyes that kill", description="Stare into its eyes and your retinas are burnt.")
a.save()

c = Creature(name="Beadeye;", hp=3920, image="8", speed=35, defense=80,attack=85,
             description="It's primary habitat is the river but it can also live in jungle biomes.")

a.save()
c.ability = a
c.save()

a = Ability(name= "Strong bite", description="It'll destroy anything near it with its drill like mouth")
a.save()

c = Creature(name="Aplex;", hp=3920, image="22", speed=20, defense=50,attack=50,
             description="Born from a tree, these creatures have evolved to have "
                         "a killer mouth for those who try to snack on it.")
c.ability = a
c.save()


a = Ability(name= "Pound", description="Its hands may be small but rapidly deadly")
a.save()

c = Creature(name="Punseol;", hp=3920, image="43", speed=65, defense=90,attack=95,
             description="It's colorful splendor may be deceaving but those black paws are powerfull. "
                         "Mostly used for rapid punches or nerve striking to temporarily paralyze and enemy ")
c.ability = a
c.save()

a = Ability(name= "Electric shock", description="With its rubbery body it will pulsate a "
                                                "electric charge by its negative charges.")
a.save()

c = Creature(name="Bluma;", hp=3920, image="104", speed=45, defense=30,attack=45,
             description="This creature is not so organic, the Bluma was man made as a police weapon.")
c.ability = a
c.save()

a = Ability(name="Scratch", description="His knife-like claws it will swipe at its enemy.")
a.save()

c = Creature(name="Muonic;", hp=3920, image="187", speed=80, defense=50,attack=87,
             description="Normally found in the artic, Muonics are little cat like"
                         " creatures that dont have fur but have blubber to keep them warm.")
c.ability = a
c.save()

a = Ability(name="Hypnotize", description=" Their dance hypnotize their enemy as a distraction.")
a.save()

c = Creature(name="Marbo twins;", hp=3920, image="260", speed=50, defense=70,attack=50,
             description="Often seen in pairs, these creatures are found in the most humid of forests. "
                         "It is very rare to find they wandering alone because they use their abilities with a partner.")
c.ability = a
c.save()

a = Ability(name="Flareball", description=" Its body rolls up into a ball to ignite its flames"
                                          "to them act as a conon and launches itself toward their enemy")
a.save()

c = Creature(name="Polire;", hp=3920, image="502", speed=60, defense=80,attack=40,
             description="The Polire's main habitat is underground but could also make a home of a hollow tree."
                         "Normally peacefully, these creatures try their best to avoid confrontation "
                         "but if startled enough,you could find yourself in trouble.")
c.ability = a
c.save()

a = Ability(name="Water wip", description=" A water strike delivering a powerful blow that causes significant damage")
a.save()

c = Creature(name="Lotleli;", hp=3920, image="538", speed=70, defense=50,attack=90,
             description=" The Lotleli are strongest around water because that's where their "
                         "draw most of their abilities. Vigorous, these creatures are to be feared. ")
c.ability = a
c.save()

a = Ability(name="Squeel", description=" A loud piercing sound that temporarily deafens ita target as a distraction")
a.save()

c = Creature(name="Sork;", hp=3920, image="582", speed=30, defense=70,attack=68,
             description=" They're are squishy and adorable but their loud screech makes them terrible pets.")
c.ability = a
c.save()

a = Ability(name="Swipe", description=" A fast scratch with its long sharp claws")
a.save()

c = Creature(name="Bamba;", hp=3920, image="767", speed=80, defense=76,attack=95,
             description=" One of the most friendly creatures to have. Very loyal to the ones they love "
                         "and will defend at any cause. These are found in bamboo forests.")
c.ability = a
c.save()




#find already used pictures

pics_already_used = Creature.objects().distinct("image")

all_pics = [str(n)for n in range(1,829)]

unused_pics = list(set(all_pics).difference(pics_already_used))

for each_filler_creature, each_ability in zip (creatures, abilities):
    creature_name = each_filler_creature
    ability_name = each_ability

    creature_description = creatures[creature_name]["description"]
    creature_lore = creatures[creature_name]["lore"]
    ability_description = abilities[ability_name]

    hp = randint(1, 100)
    attack = randint(1, 100)
    defense = randint(1, 100)
    speed = randint(1, 100)
    image = sample(unused_pics, 1)[0]


    c = Creature(name=creature_name, description=creature_description,
                 hp=hp, attack=attack, defense= defense, speed=speed, lore=creature_lore, image = image)
    a = Ability(name=ability_name, description=ability_description)

    a.save()
    c.ability = a
    c.save()

    pass

pass

