# Stop Motion Snake Game in Python
import random 

# "o" Spawns Randomly in the Grid
# The Snake also spawns randomly in the Grid
# The Snake moves each frame, after you say one of the commands of "wasd"

grid_width = 10
grid_height = 5


tabela = []
vazios = ' '

# Gerar tabela inicial (9x9)
for i in range(0, grid_height, 3):
    for j in range(3):
        tabela.append([vazios for k in range(grid_width)])

random_comida = random.randrange(len(tabela))
rcomida = random.randrange(len(tabela[random_comida]))
tabela[random_comida][rcomida] = 'o'

rtabela = random.randrange(len(tabela))
rpos = random.randrange(len(tabela[rtabela]))
tabela[rtabela][rpos] = '#'

def imprimir():
    for i in tabela:
        print(i)

tamanho = 1

buffer_y = []
buffer_x = []

count = 0

while True:
    imprimir()
    move = input('(W, A, S, D): ').lower()
    if not (move == 'w' or move == 'a' or move == 's' or move == 'd'):
        print('Invalid Option')
        break

    # W | up
    if move == 'w':
        if rtabela < 0:
            rtabela = rtabela + len(tabela)

        if tabela[rtabela-1][rpos] == 'o':
            tamanho += 1
            print('+1')

        tabela[rtabela-1][rpos] = '#'
        rtabela -= 1
        
        
        if len(buffer_y) > tamanho:
            buffer_y.pop(0)

        if tamanho > 1:
            print('Tamanho maior, buffer: ', buffer_y)
            buffer_y.append(rtabela)
            tabela[buffer_y[0]+1][rpos] = ' '
        else:
            tabela[rtabela+1][rpos] = ' '
    
    # S | down
    if move == 's':
        
        if rtabela+1 >= len(tabela):
            rtabela = -1

        print(rtabela)
        if tabela[rtabela+1][rpos] == 'o':
            tamanho += 1
            print('+1')
            
        tabela[rtabela+1][rpos] = '#'
        rtabela += 1

        if len(buffer_y) > tamanho:
            buffer_y.pop(0)

        if tamanho > 1:
            buffer_y.append(rtabela)
            tabela[buffer_y[0]-1][rpos] = ' '
        else:
            tabela[rtabela-1][rpos] = ' '

    
        
    # A | left
    if move == 'a':
        if rpos < 0:
            rpos += len(tabela[rtabela])
        print(rpos)
        if tabela[rtabela][rpos-1] == 'o':
            tamanho += 1
            print('+1')
            
        tabela[rtabela][rpos-1] = '#'
        rpos -= 1

        if len(buffer_x) > tamanho:
            buffer_x.pop(0)

        if tamanho > 1:
            buffer_x.append(rpos)
            tabela[rtabela][buffer_x[0]+1] = ' '
        else:
            
            tabela[rtabela][rpos+1] = ' '
        
        
    # D | right
    if move == 'd':
        if rpos+1 >= len(tabela[rtabela]):
            rpos -= len(tabela[rtabela])
        print(rpos)
        if tabela[rtabela][rpos+1] == 'o':
            tamanho += 1
            print('+1')

        tabela[rtabela][rpos+1] = '#'
        rpos += 1
       
        if len(buffer_x) > tamanho:
            buffer_x.pop(0)

        if tamanho > 1:
            buffer_x.append(rpos)
            tabela[rtabela][buffer_x[0]-1] = ' '
        else:
            tabela[rtabela][rpos-1] = ' '
        
        
    
