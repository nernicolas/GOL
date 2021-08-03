
def alive_cells_from_grid(grille):
    alive_cells=set()
    n = len(grille)
    for i in range(n):
        for j in range(n):
            if grille[i][j] == 1:
                alive_cells.add((i,j))
                alive_cells.add((i, j + 1))
                alive_cells.add((i, j - 1))
                alive_cells.add((i + 1, j + 1))
                alive_cells.add((i - 1, j + 1))
                alive_cells.add((i + 1, j - 1))
                alive_cells.add((i - 1, j - 1))
                alive_cells.add((i + 1, j))
                alive_cells.add((i - 1, j))
    return alive_cells

def count_alive_neighbours(grille,i,j):
    n=len(grille)
    cpt = 0
    cpt += grille[i][j + 1]
    cpt += grille[i][j - 1]
    cpt += grille[i + 1][j]
    cpt += grille[i - 1][j]
    cpt += grille[i + 1][j + 1]
    cpt += grille[i + 1][j - 1]
    cpt += grille[i - 1][j + 1]
    cpt += grille[i - 1][j - 1]
    return cpt

def next_gen(grille, alive_cells):
    n = len(grille)
    alive_cells_copy= alive_cells.copy()
    alive_cells=set()
    cpt= [[0 for i in range(n)] for j in range(n)]
    for i,j in alive_cells_copy:
        if i+1 > n-1 or j+1 > n-1 or i-1<0 or j-1<0:
            continue
        cpt[i][j] = count_alive_neighbours(grille,i,j)
    for i,j in alive_cells_copy:
        if i + 1 > n - 1 or j + 1 > n - 1 or i - 1 < 0 or j - 1 < 0:
            continue
        if grille[i][j] == 0 and cpt[i][j]== 3:
            grille[i][j] =1
            # alive at next so need to be checked
            alive_cells.add((i, j))
            # so are his neighbours
            alive_cells.add((i, j + 1))
            alive_cells.add((i, j - 1))
            alive_cells.add((i + 1, j + 1))
            alive_cells.add((i - 1, j + 1))
            alive_cells.add((i + 1, j - 1))
            alive_cells.add((i - 1, j - 1))
            alive_cells.add((i + 1, j))
            alive_cells.add((i - 1, j))
        elif grille[i][j] == 1 and (cpt[i][j]== 2 or cpt[i][j] == 3):
            # alive at next so need to be checked
            alive_cells.add((i, j))
            # so are his neighbours
            alive_cells.add((i, j + 1))
            alive_cells.add((i, j - 1))
            alive_cells.add((i + 1, j + 1))
            alive_cells.add((i - 1, j + 1))
            alive_cells.add((i + 1, j - 1))
            alive_cells.add((i - 1, j - 1))
            alive_cells.add((i + 1, j))
            alive_cells.add((i - 1, j))
            pass
        else:
            if grille[i][j] == 1:
                grille[i][j]=0
    return grille, alive_cells


def update(grille, alive_cells):
    el = next_gen(grille,alive_cells)
    return el[0],el[1]

