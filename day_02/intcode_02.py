from intcode_01 import opcode, data

def find_noun_verb(l):
    result = opcode(l)
    counter = 0
    while result[0] != 19690720:
        counter += 1
        if counter % 2 == 0:
            l[2] +=1
        else:
            l[1] += 1
        result = opcode(l)
    print(f'The noun is {l[1]} and verb is {l[2]}')

find_noun_verb(data)