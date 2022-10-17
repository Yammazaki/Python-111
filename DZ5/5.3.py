from csv import excel
from traceback import clear_frames


print('Крестики нолики! ver 1.0')

table = list(range(1,10))

def game_field(table):
    print('—'*20)
    for i in range(3):
        print(' | ', table[0+i*3],' | ', table[1+i*3], ' | ', table[2+i*3], ' | ')
        print('—'*20)


def choice(tic_tac):
    valid = False
    while not valid:
        print("\n" * 3)
        pl_i = input('Ваш ход ==> ' + tic_tac + ' --> ')
        try:
            pl_i =int(pl_i)
        except:
            print('Что то не то)))')
            continue
        if pl_i >= 1 and pl_i <= 9:
            if(str(table[pl_i-1]) not in '❌⭕'):
                table[pl_i-1] = tic_tac
                valid = True
            else:
                print('Клетка занята')
        else:
            print('Попробуй ёще раз')

def victory_check(table):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if table[i[0]] == table[i[1]] == table[i[2]]:
            return table[i[0]]
    return False

def game(table):
    count =0
    vic = False
    while not vic:
        game_field(table)
        if count % 2 == 0:
            choice('❌')
        else:
            choice('⭕')
        count +=1
        if count > 4:
            tt_win = victory_check(table)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
            if count == 9:
                print('Ничья товарищи!)')
        game_field(table)
game(table)