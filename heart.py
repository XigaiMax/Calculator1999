class heart:
    def __init__(self, heart_attack, ritual_power, magic_power, damage_bonus, amplify):  # 心相攻击力、仪式威力、术法威力、创伤加成、增幅描述
        self.heart_attack = heart_attack
        self.ritual_power = ritual_power
        self.magic_power = magic_power
        self.damage_bonus = damage_bonus
        self.amplify = amplify


brave_new_world = heart(292, 0.16, 0, 0, '记忆者释放至终的仪式后，下次普通咒语的术法威力提升20%')

hopscotch_game = heart(292, 0, 0.16, 0, '记忆者每击败1个敌方目标，自身仪式威力提升4%，该效果最多叠加4层')

second_life = heart(276, 0, 0, 0, '记忆者释放群体至终的仪式后，我方全体回复记忆者攻击*32%的生命值')
night_blasphemer = heart(284, 0, 0.16, 0, '记忆者攻击时，若目标携带至少2个[状态异常]，则对其造成伤害提升12%')
applause_is_like_thunder = heart(260, 0, 0, 0, '记忆者单体攻击暴击时，暴击创伤提升16%')
curiosity_baby = heart(
    284, 0, 0, 0, '记忆者使用减益类普通咒语后，使生命百分比最低的友方回复自身攻击*24%的生命值（每回合最多触发1次）')
great_entertainment_comes_first = heart(300, 0.16, 0, 0,
                                        '记忆者释放单体至终的仪式后，自身造成伤害提升5%，该效果最多叠加3层')
necessary_records = heart(323, 0, 0, 0.1, '记忆者每击败1个敌方目标，回复自身攻击*60%的生命值')
beyond_wonderland = heart(276, 0, 0, 0,
                          '记忆者使用减益类普通咒语后，自身治疗率提升3%，该效果最多叠加4层；记忆者暴击率提升7%')
measureable_heart = heart(268, 0, 0, 0,
                          '回合结束时，若记忆者本回合获得至少3点激情，下次释放至终的仪式时仪式威力提升8%；若记忆者本回合获得至少4点激情，该效果提升至12%')


def choice_heart(index):

    if index == 0:
        heart = brave_new_world
    elif index == 1:
        heart = hopscotch_game
    elif index == 2:
        heart = second_life
    elif index == 3:
        heart = night_blasphemer
    elif index == 4:
        heart = applause_is_like_thunder
    elif index == 5:
        heart = curiosity_baby
    elif index == 6:
        heart = great_entertainment_comes_first
    elif index == 7:
        heart = necessary_records
    elif index == 8:
        heart = beyond_wonderland
    elif index == 9:
        heart = measureable_heart

    return heart
