# 最终伤害=(面板攻击力-最终防御力)*（1+创伤加成+伤害加成-受创减免）*（1+术法威力/仪式威力）*技能倍率*属性克制

# 面板攻击力 = 面板直接显示的攻击力
# 最终防御力 = 敌人防御力 * 防御力加成
# 最终伤害 = (面板攻击力-最终防御力) * (1 + 创伤加成 + 伤害加成 - 受创减免) * 技能倍率 * (1 + 术法威力 / 仪式威力) * 属性克制


def final_damage_calculation(total_attack, total_defense, damage_bonus, damage_increase, injury_relief, skill_ratio,
                             ritual_power,
                             magic_power, match_up_value):
    return (total_attack - total_defense) * (1 + damage_bonus + damage_increase - injury_relief) * skill_ratio * (
            1 + ritual_power) * (1 + magic_power) * (1 + match_up_value)


# 暴击伤害 = 最终伤害 * 暴击创伤
def crit_damage_calculation(regular_theoretical_damage, critical_strike_ratio, crit_defense):
    return regular_theoretical_damage * (critical_strike_ratio - crit_defense)


# 暴击期望伤害 = 最终伤害*暴伤*暴击率+最终伤害*（1-暴击率）
def critical_strike_expected_damage_calculation(regular_theoretical_damage, critical_strike_rate,
                                                critical_strike_ratio, crit_defense):
    return regular_theoretical_damage * (
                critical_strike_ratio - crit_defense) * critical_strike_rate + regular_theoretical_damage * (
            1 - critical_strike_rate)
