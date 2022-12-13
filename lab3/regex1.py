import re

# Вариант 002
smile = r':-O'
reg = re.compile(smile)
tests = ['asdasdafd:-Oakdma:- O-0-O:-Oda   sokd', 'eafad:-Oijaf:-:-O:-O:-Oefwo3-Ovd:-O', ':-0',
         'ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ:-O:-O:-OЫЫЫЫЫЫЫ', ':-OOOOOOOOOOOOOOOOOOOOO']
for test in tests:
    match = reg.findall(test)
    print(f'{len(match)} смайлика(ов) в \"{test}\"')

# Ответы: 3, 5, 0, 3, 1
