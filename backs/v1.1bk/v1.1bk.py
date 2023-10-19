# pyinstaller -F -w -i D:\Project\Python\Calculator1999\xt.ico -n "伤害计算器v1" main.py
import math
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


# 面板攻击力 = 面板直接显示的攻击力
# 最终防御力 = 敌人防御力 * 防御力加成
# 最终伤害 = (面板攻击力-最终防御力) * (1 + 创伤加成 + 伤害加成 - 受创减免) * (1 + 术法威力 / 仪式威力) * 技能倍率 * 属性克制
def final_damage_calculation(total_attack, total_defense, damage_bonus, damage_increase, skill_ratio):
    return (total_attack - total_defense * (1 + damage_bonus + damage_increase - 0)) * skill_ratio


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
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('1999伤害期望计算器')
        self.setGeometry(300, 300, 400, 300)
        self.initUI()
    def initUI(self):

        self.layout = QVBoxLayout()

        self.attack_label = QLabel("攻击白值:")
        self.attack_input = QLineEdit()
        self.layout.addWidget(self.attack_label)
        self.layout.addWidget(self.attack_input)

        self.skill_ratio_label = QLabel("技能倍率(%):")
        self.skill_ratio_input = QLineEdit()
        self.layout.addWidget(self.skill_ratio_label)
        self.layout.addWidget(self.skill_ratio_input)
        self.skill_ratio_input.setPlaceholderText('输入百分号前的数字')

        self.damage_bonus_label = QLabel("创伤加成:")
        self.damage_bonus_input = QLineEdit()
        self.layout.addWidget(self.damage_bonus_label)
        self.layout.addWidget(self.damage_bonus_input)

        self.damage_increase_label = QLabel("伤害提升:")
        self.damage_increase_input = QLineEdit()
        self.layout.addWidget(self.damage_increase_label)
        self.layout.addWidget(self.damage_increase_input)

        self.total_defense_label = QLabel("敌方防御力:")
        self.total_defense_input = QLineEdit()
        self.layout.addWidget(self.total_defense_label)
        self.layout.addWidget(self.total_defense_input)
        self.total_defense_input.setPlaceholderText('不输入默认为555（天蛾人）')

        self.critical_strike_rate_label = QLabel("暴击率:")
        self.critical_strike_rate_input = QLineEdit()
        self.layout.addWidget(self.critical_strike_rate_label)
        self.layout.addWidget(self.critical_strike_rate_input)

        self.critical_strike_ratio_label = QLabel("暴击创伤:")
        self.critical_strike_ratio_input = QLineEdit()
        self.layout.addWidget(self.critical_strike_ratio_label)
        self.layout.addWidget(self.critical_strike_ratio_input)

        self.calculate_button = QPushButton("计算")
        self.calculate_button.clicked.connect(self.calculate_damage)
        self.layout.addWidget(self.calculate_button)

        self.result1_label = QLabel("未暴击伤害:")
        self.result1_output = QLabel()
        self.layout.addWidget(self.result1_label)
        self.layout.addWidget(self.result1_output)

        self.result2_label = QLabel("暴击伤害:")
        self.result2_output = QLabel()
        self.layout.addWidget(self.result2_label)
        self.layout.addWidget(self.result2_output)

        self.result3_label = QLabel("暴击期望:")
        self.result3_output = QLabel()
        self.layout.addWidget(self.result3_label)
        self.layout.addWidget(self.result3_output)

        self.setLayout(self.layout)



    def calculate_damage(self):
        total_attack = float(self.attack_input.text())  # 面板攻击力（角色页面显示的攻击力）
        total_defense = 555 if self.total_defense_input.text() == '' else float(self.total_defense_input.text())
        damage_bonus = 0 if self.damage_bonus_input.text() == '' else float(self.damage_bonus_input.text())  # 创伤加成
        damage_increase = 0 if self.damage_increase_input.text() == '' else float(
            self.damage_increase_input.text())  # 伤害提升
        skill_ratio = float(self.skill_ratio_input.text()) / 100  # 技能倍率

        critical_strike_rate = float(self.critical_strike_rate_input.text())  # 暴击创伤
        critical_strike_ratio = float(self.critical_strike_ratio_input.text())  # 暴击率

        # 计算最终伤害
        regular_theoretical_damage = final_damage_calculation(total_attack, total_defense, damage_bonus,
                                                              damage_increase,
                                                              skill_ratio)

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
