string = '1234567890：；;:%.·面板攻击力技能倍率暴击创伤害提升属性克制类型心相选择敌人仪式术法创伤加成美丽新世界跳房子游戏第二次生命夜色亵渎者掌声如雷鸣好奇心宝贝大娱乐至上必要的记录在仙境之外可度量之心凶兆天蛾人厄无防御测试怪现实防御精神受创减免暴击防御未期望计算'
unique_chars = list(set(string))
unique_chars.sort()
re = ''.join(unique_chars)
print(re)