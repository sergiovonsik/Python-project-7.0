import numpy as np


def serch_prox_candy(candy, actual_candy):
    for i in candy:
        original_candy_len = len(candy)

        x_up, x_down, y_left, y_right = 0, 0, 0, 0

        if i[0] - 1 > 0:
            x_up = i[0] - 1

        if i[0] + 1 > 0:
            x_down = i[0] + 1

        if i[1] - 1 > 0:
            y_left = i[1] - 1

        if i[1] + 1 > 0:
            y_right = i[1] + 1

        try:
            if matrix[x_up, i[1]] == actual_candy:  # UP
                matrix[x_up, i[1]] = "N"
                candy.append([x_up, i[1]])
        except IndexError:
            pass

        try:
            if matrix[x_down, i[1]] == actual_candy:  # DOWN
                matrix[x_down, i[1]] = "N"
                candy.append([x_down, i[1]])
        except IndexError:
            pass

        try:
            if matrix[i[0], y_left] == actual_candy:  # LEFT
                matrix[i[0], y_left] = "N"
                candy.append([i[0], y_left])
        except IndexError:
            pass

        try:
            if matrix[i[0], y_right] == actual_candy:  # RIGHT
                matrix[i[0], y_right] = "N"
                candy.append([i[0], y_right])
        except IndexError:
            pass


def candy_crush():
    actual_candy = ""
    vector_number = -1
    for vector in matrix:  # BUSCADOR HORIZONTAL DE ELEMENTOS
        vector_number += 1
        element_number = -1
        candy_count = []
        for i in vector:
            element_number += 1
            if actual_candy == i:  # si el elemento del vector que se analiza coincide con
                # el que se estaba trabajando se suma el index de este nuevo a la lista
                candy_count.append([vector_number, element_number])
                if len(candy_count) == 3:
                    serch_prox_candy(candy_count, actual_candy)


            elif actual_candy != i:  # el nuevo elemento analizado no coincide, ahora revisamos la lista que trabajamos antes
                # cumple con las condiciones o no.

                if len(candy_count) == 3:  # funcion donde se cambia el '#' por un 'N' de cumplir con que sean mas que 3
                    serch_prox_candy(candy_count, actual_candy)
                    candy_count = []
                    actual_candy = i
                    if actual_candy == 'N':
                        actual_candy = ''


                else:  # de no cumplir se limpian los datos y se sigue revisando si es que hay mas coincidencias.
                    actual_candy = i
                    candy_count = [[vector_number, element_number]]
                    if actual_candy == 'N':
                        actual_candy = ''

    # ==============================================================================================
    for element in range(len(matrix[0])):  # BUSCADOR VERTICAL DE ELEMENTOS
        candy_count = {}  # Total de elementos en una columna
        coincidence_list = []  # Coincidencia encontradas en la columna analizada
        actual_column_candy = ""

        for column in range(len(matrix)):  # se procesa los elementos que van a estar en la lista de "candy_count"
            character_element = matrix[column, element]
            candy_count[f'{column} {element}'] = character_element

        for i in candy_count.items():
            if i[1] == actual_column_candy:
                coincidence_list.append(i[0])
            elif i[1] != actual_column_candy:
                coincidence_list = [i[0]]
                actual_column_candy = f'{i[1]}'
                if actual_column_candy == 'N':
                    actual_column_candy = ''

            if len(coincidence_list) == 3:
                coincidence_list = return_organiced(coincidence_list)
                serch_prox_candy(coincidence_list, actual_column_candy)
            else:
                pass


def return_organiced(x):
    result_list = []
    for i in x:
        x, y = i.split()
        x = int(x)
        y = int(y)
        result_list.append([x, y])
    return result_list


def drop_the_candies():
    for row in range(len(matrix[0])):
        for column in range(len(matrix)):
            try:
                if matrix[column + 1, row] == "N":
                    matrix[column + 1, row] = matrix[column, row]
                    matrix[column, row] = "  "
            except IndexError:
                pass

    for row in range(len(matrix[0])):
        for column in range(len(matrix)):
            try:
                if matrix[column + 1, row] == " ":
                    matrix[column + 1, row] = matrix[column, row]
                    matrix[column, row] = " "
            except IndexError:
                pass
    for row in range(len(matrix[0])):
        for column in range(len(matrix)):
            try:
                if matrix[column, row] == "N":
                    matrix[column, row] = " "
            except IndexError:
                pass


old_counter = 0



def change_candies():
    col, row, direction = input('Insert: Column Row {left, right, up or down}').split()
    col = int(col)
    row = int(row)
    old_matrix = matrix
    if direction == "up":
        if row - 1 < 0:
            print("IndexError, try once more")
            change_candies()
        else:
            change_1 = matrix[row, col]
            change_2 = matrix[row - 1, col]
            matrix[row, col] = change_2
            matrix[row - 1, col] = change_1

    elif direction == "down":
        if row + 1 > 4:
            print("IndexError, try once more")
            change_candies()
        else:
            change_1 = matrix[row, col]
            change_2 = matrix[row + 1, col]
            matrix[row, col] = change_2
            matrix[row + 1, col] = change_1

    elif direction == "left":
        if col - 1 < 0:
            print("IndexError, try once more")
            change_candies()
        else:
            change_1 = matrix[row, col]
            change_2 = matrix[row, col - 1]
            matrix[row, col] = change_2
            matrix[row, col - 1] = change_1

    elif direction == "right":
        if col + 1 > 9:
            print("IndexError, try once more")
            change_candies()
        else:
            change_1 = matrix[row, col]
            change_2 = matrix[row, col + 1]
            matrix[row, col] = change_2
            matrix[row, col + 1] = change_1

    candy_crush()  # verifica si hay algun caracter para eliminar
    drop_the_candies()
    drop_the_candies()
    print(f'\n\n{matrix}\n\n', )

    change_candies()  # volver a loop de preguntar coordenadas


#   End of Defs-----------------------------------------------------------------------------------------

if __name__ == '__main__':
    print('PyCharm')
    matrix = np.array([['!', '*', '#', '#', '%', '@', '%', '@', '@', '*'],
                       ['!', '@', '*', '!', '#', '%', '*', '#', '*', '@'],
                       ['#', '@', '@', '#', '*', '@', '%', '*', '@', '*'],
                       ['!', '#', '@', '@', '#', '@', '@', '%', '@', '#'],
                       ['#', '@', '!', '*', '@', '%', '%', '*', '#', '@']])
    print(matrix, "\n\n")

    candy_crush()
    drop_the_candies()
    drop_the_candies()
    change_candies()
