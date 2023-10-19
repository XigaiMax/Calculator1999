class enemy:
    def __init__(self, realistic_defense, mental_defense, injury_relief, crit_defense):  # 现实防御、精神防御、受创减免
        self.realistic_defense = realistic_defense
        self.mental_defense = mental_defense
        self.injury_relief = injury_relief
        self.crit_defense = crit_defense


moth1 = enemy(553, 513, 0.14, 0.164)
moth2 = enemy(515, 555, 0.087, 0.164)
noob = enemy(0, 0, 0, 0)


def choice_enemy(index):

    if index == 0:
        enemy = moth1
    elif index == 1:
        enemy = moth2
    elif index == 2:
        enemy = noob

    return enemy
