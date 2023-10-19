# pyinstaller -F -w -i D:\Project\Python\Calculator1999\images\logo.ico -n "伤害计算器v1.2" main.py
import math
import os
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit

from heart import *
from enemy import *


def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# 面板攻击力 = 面板直接显示的攻击力
# 最终防御力 = 敌人防御力 * 防御力加成
# 最终伤害 = (面板攻击力-最终防御力) * (1 + 创伤加成 + 伤害加成 - 受创减免) * 技能倍率 * (1 + 术法威力 / 仪式威力) * 属性克制
def final_damage_calculation(total_attack, total_defense, damage_bonus, damage_increase, injury_relief, skill_ratio,
                             ritual_power,
                             magic_power, match_up_value):
    return (total_attack - total_defense) * (1 + damage_bonus + damage_increase - injury_relief) * skill_ratio * (
            1 + ritual_power) * (1 + magic_power) * (1 + match_up_value)


# 暴击伤害 = 最终伤害 * 暴击创伤
def crit_damage_calculation(regular_theoretical_damage, critical_strike_ratio):
    return regular_theoretical_damage * critical_strike_ratio


# 暴击期望伤害 = 最终伤害*暴伤*暴击率+最终伤害*（1-暴击率）
def critical_strike_expected_damage_calculation(regular_theoretical_damage, critical_strike_rate,
                                                critical_strike_ratio):
    return regular_theoretical_damage * critical_strike_rate * critical_strike_ratio + regular_theoretical_damage * (
            1 - critical_strike_rate)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(get_resource_path('./images/logo_yellow.png')))
        self.setWindowTitle('暴雨科算计算器')
        self.setGeometry(300, 300, 400, 300)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # 攻击力输入框
        self.attack_label = QLabel("攻击力:")
        self.attack_input = QLineEdit()
        self.attack_input.setPlaceholderText('输入角色面板的显示值')
        self.layout.addWidget(self.attack_label)
        self.layout.addWidget(self.attack_input)

        # 技能倍率输入框
        self.skill_ratio_label = QLabel("技能倍率(%):")
        self.skill_ratio_input = QLineEdit()
        self.layout.addWidget(self.skill_ratio_label)
        self.layout.addWidget(self.skill_ratio_input)
        self.skill_ratio_input.setPlaceholderText('例：160%倍率请输入160')

        # 伤害提升输入框
        self.damage_increase_label = QLabel("伤害提升:")
        self.damage_increase_input = QLineEdit()
        self.layout.addWidget(self.damage_increase_label)
        self.layout.addWidget(self.damage_increase_input)
        self.damage_increase_input.setPlaceholderText('不输入默认为0')

        # 伤害类型选择框
        self.damage_choice_label = QLabel("伤害类型:")
        self.damage_choice_combobox = QComboBox()
        self.damage_choice_combobox.addItem('现实伤害')
        self.damage_choice_combobox.addItem("精神伤害")
        self.layout.addWidget(self.damage_choice_label)
        self.layout.addWidget(self.damage_choice_combobox)

        # 属性克制选择框
        self.matchup_choice_label = QLabel("是否属性克制:")
        self.matchup_choice_combobox = QComboBox()
        self.matchup_choice_combobox.addItem('克制')
        self.matchup_choice_combobox.addItem("非克制")
        self.layout.addWidget(self.matchup_choice_label)
        self.layout.addWidget(self.matchup_choice_combobox)

        # 敌人选择框
        self.enemy_choice_label = QLabel("敌人选择:")
        self.enemy_choice_combobox = QComboBox()
        self.enemy_choice_combobox.addItem('凶兆·天蛾人')
        self.enemy_choice_combobox.addItem("厄兆·天蛾人")
        self.enemy_choice_combobox.addItem("无防御测试怪")
        self.enemy_choice_combobox.currentIndexChanged.connect(self.update_enemy)
        self.layout.addWidget(self.enemy_choice_label)
        self.layout.addWidget(self.enemy_choice_combobox)

        # 敌人信息显示框
        self.enemy_info_text = QTextEdit()
        self.enemy_info_text.setReadOnly(True)
        self.layout.addWidget(self.enemy_info_text)

        # 暴击率输入框
        self.critical_strike_rate_label = QLabel("暴击率:")
        self.critical_strike_rate_input = QLineEdit()
        self.layout.addWidget(self.critical_strike_rate_label)
        self.layout.addWidget(self.critical_strike_rate_input)

        # 暴击创伤输入框
        self.critical_strike_ratio_label = QLabel("暴击创伤:")
        self.critical_strike_ratio_input = QLineEdit()
        self.layout.addWidget(self.critical_strike_ratio_label)
        self.layout.addWidget(self.critical_strike_ratio_input)

        # 心相选择框
        self.heart_choice_label = QLabel("心相选择:")
        self.heart_choice_combobox = QComboBox()
        self.heart_choice_combobox.setIconSize(QSize(70, 70))
        self.heart_choice_combobox.addItem(QIcon('./images/1.png'), '美丽新世界')
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/2.png')), "跳房子游戏")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/3.png')), "第二次生命")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/4.png')), "夜色亵渎者")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/5.png')), "掌声如雷鸣")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/6.png')), "好奇心宝贝")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/7.png')), "大娱乐至上")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/8.png')), "必要的记录")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/9.png')), "在仙境之外")
        self.heart_choice_combobox.addItem(QIcon(get_resource_path('./images/10.png')), "可度量之心")
        self.heart_choice_combobox.currentIndexChanged.connect(self.update_heart)
        self.layout.addWidget(self.heart_choice_label)
        self.layout.addWidget(self.heart_choice_combobox)

        # 心相信息显示框
        self.heart_info_text = QTextEdit()
        self.heart_info_text.setReadOnly(True)
        self.layout.addWidget(self.heart_info_text)

        # 计算按钮
        self.calculate_button = QPushButton("计算")
        self.calculate_button.clicked.connect(self.calculate_damage)
        self.layout.addWidget(self.calculate_button)

        # 未暴击伤害显示框
        self.result1_label = QLabel("未暴击伤害:")
        self.result1_output = QLabel()
        self.layout.addWidget(self.result1_label)
        self.layout.addWidget(self.result1_output)

        # 暴击伤害显示框
        self.result2_label = QLabel("暴击伤害:")
        self.result2_output = QLabel()
        self.layout.addWidget(self.result2_label)
        self.layout.addWidget(self.result2_output)

        # 暴击期望显示框
        self.result3_label = QLabel("暴击期望:")
        self.result3_output = QLabel()
        self.layout.addWidget(self.result3_label)
        self.layout.addWidget(self.result3_output)

        self.setLayout(self.layout)

    def update_enemy(self, index):
        enemy = choice_enemy(index)

        if enemy:
            data = f"现实防御：{enemy.realistic_defense}\n精神防御：{enemy.mental_defense}\n受创减免：{enemy.injury_relief * 100}%"
            self.enemy_info_text.setPlainText(data)

    def update_heart(self, index):
        heart = choice_heart(index)

        if heart:
            data = f"心相攻击力：{heart.heart_attack}\n仪式加成：{heart.ritual_power * 100}%\n术法加成：{heart.magic_power * 100}%\n创伤加成：{heart.damage_bonus * 100}%\n增幅：{heart.amplify}"
            self.heart_info_text.setPlainText(data)

    def calculate_damage(self):
        heart = choice_heart(self.heart_choice_combobox.currentIndex())
        enemy = choice_enemy(self.enemy_choice_combobox.currentIndex())

        damage = self.damage_choice_combobox.currentIndex()

        if damage == 0:
            total_defense = enemy.realistic_defense
        elif damage == 1:
            total_defense = enemy.mental_defense

        match_up = self.matchup_choice_combobox.currentIndex()

        if match_up == 0:
            match_up_value = 0.3
        else:
            match_up_value = 0

        total_attack = float(self.attack_input.text())  # 面板攻击力（角色页面显示的攻击力）

        damage_increase = 0 if self.damage_increase_input.text() == '' else float(
            self.damage_increase_input.text())  # 伤害提升

        skill_ratio = float(self.skill_ratio_input.text()) / 100  # 技能倍率

        critical_strike_rate = float(self.critical_strike_rate_input.text()) / 100  # 暴击创伤
        critical_strike_ratio = float(self.critical_strike_ratio_input.text()) / 100  # 暴击率

        # 计算最终伤害
        regular_theoretical_damage = final_damage_calculation(total_attack, total_defense, heart.damage_bonus,
                                                              damage_increase, enemy.injury_relief,
                                                              skill_ratio, heart.ritual_power, heart.magic_power,
                                                              match_up_value)

        # 计算暴击伤害
        crit_damage = crit_damage_calculation(regular_theoretical_damage, critical_strike_ratio)

        # 计算暴击期望伤害
        critical_strike_expected_damage = critical_strike_expected_damage_calculation(regular_theoretical_damage,
                                                                                      critical_strike_rate,
                                                                                      critical_strike_ratio)

        self.result1_output.setText(str(math.floor(regular_theoretical_damage)))
        self.result2_output.setText(str(math.floor(crit_damage)))
        self.result3_output.setText(str(math.floor(critical_strike_expected_damage)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()

    sys.exit(app.exec_())
