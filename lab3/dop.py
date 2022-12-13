import re

str = 'ываыва "уттыты ы- 0"   ы    ""'
print(re.findall(r'"(.*?)"', str))
print(re.findall(r'(?<=").*?(?=")', str))
