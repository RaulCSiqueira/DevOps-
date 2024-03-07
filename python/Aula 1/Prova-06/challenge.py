from random import randint


'''
    Requirements:

    Implement the missing magic methods from the Deity and Pantheon classes.

        Deity:

            Implement the __int__ method to return the health value.
            Implement the __bool__ method to return True if the health value is greater than zero.
            
        Pantheon:

            Implement the __bool__ method to return True if any available deities exist according to the available attribute.
'''

class Deity:

    def __init__(self, name, health=100):
        self.xp = 0
        self.name = name
        self.health = health
    
    def __str__(self):
        return f'{self.name} has {self.health} health remaining.'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.health})'
    
    def __int__(self):
        return self.health
    
    def __bool__(self):
        return self.health > 0

    def attack(self, other):
        other.health -= randint(0, 100)
        

class Pantheon:

    def __init__(self, *deities):
        self.deities = list(deities)
    
    @property
    def available(self):
        for deity in self.deities:
            if deity:
                yield deity
    
    def __bool__(self):
        return any(self.deities)
        
    

class Player:
    def __init__(self, name, pantheon):
        self.name = name
        self.pantheon = pantheon

    @property
    def has_remaining_deities(self):
        return bool(self.pantheon)
    

def play(player_a, player_b):
    # Remove cards without health
    attacker, defender = player_a, player_b

    while defender.has_remaining_deities:
        attackers_deity = next(attacker.pantheon.available)
        defenders_deity = next(defender.pantheon.available)
        
        attackers_deity.attack(defenders_deity)
        print(f'{attackers_deity.name}({attackers_deity.health}) attacks {defenders_deity.name}({defenders_deity.health})')

        if int(defenders_deity) <= 0:
            print(f'{defenders_deity.name} was defeated!')
        
        if not defender.has_remaining_deities:
            print(f'{attacker.name} wins!')
            break
        
        attacker, defender = defender, attacker
    

if __name__ == '__main__':

    
    player_a = Player(
        'Thunder', 
        Pantheon(
            Deity('Smasher'),
            Deity('Crasher'),
            Deity('Fireball'),
        )
    )
    player_b = Player(
        'Lightning', 
        Pantheon(
            Deity('Wolf'),
            Deity('Bear'),
            Deity('Orion'),
        )
    )
    

    play(player_a, player_b)

