from dokusan import generators
import numpy as np


def generate():
    arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))
    int_array = arr.astype(int)
    reshaped_array = int_array.reshape(9, 9)
    return reshaped_array.tolist()
