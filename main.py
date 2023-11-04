class monster():
    def __init__(gold, exp):
        self.gold = gold
        self.exp = exp
        self.level = 1

    def cleared(self):
        level+=1
    
    def get_gold(self):
        return gold[self.level]

    def get_exp(self):
        return exp[self.level]
#make classes for scuttle, krugs, mini-krugm, krug, raptor, mini-raptor, gromp, big wolf, mini-wolf, blue buff, red buff 
#that inherits from monster

class jungle_camp():
    camp_monsters = {}
    #big_monster and small_monster are of type monster
    def __init__(num_big_monster, big_monster, num_small_monster, small_monster):
        self.camp.big_monster = num_big_monster
        self.camp.small_monster = num_small_monster

    def get_gold():
        gold = 0
        for monster in camp_monsters:
            gold += monster.get_gold() * camp_monsters[monster]
        return gold
#make classes for CAMPS FORscuttle, krugs, mini-krugm, krug, raptor, mini-raptor, gromp, big wolf, mini-wolf, blue buff, 
#red buff that inherits from jungle camp

class jungle_state():
    camps = {}

    def __init__():
        camps_per_side = []
        camps_per_side.append(scuttle_camp())
        camps_per_side.append(gromp_camp())
        camps_per_side.append(blue_buff_camp())
        camps_per_side.append(wolf_camp())

        camps_per_side.append(raptor_camp())
        camps_per_side.append(red_buff_camp())
        camps_per_side.append(krug_camp())
        camps_per_side.append(scuttle_camp())
        
        camps["blue"] = camps_per_side
        camps["red"] = camps_per_side
        #figure if new objects are created with these sides, doubt it, figure a new way to creat red and blue side for visual

class champion():
    xp_to_next_level = 280

    def __init__():
        self.level = 1
        self.xp = 0
    
    #passes the monster obejct specially that existed with whatever level they currently have on the map
    def clear_monster(self, monster):
        self.xp += monster.get_exp()
        self.update_level()
    
    def update_level(self):
        if xp_to_next_level == self.xp:
            self.level += 1
            xp_to_next_level += 100


