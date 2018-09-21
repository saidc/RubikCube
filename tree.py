import copy
import time
import random
import numpy as np
import os

"""
face1 = np.zeros((3, 3))
face2 = np.zeros((3, 3))
face3 = np.zeros((3, 3))
face4 = np.zeros((3, 3))
face5 = np.zeros((3, 3))
face6 = np.zeros((3, 3))
"""


class Node(object):
    def __init__(self, cube_pos, value, padre, rubik):
        self.cube_pos = cube_pos
        self.value = value
        self.rubik = rubik
        self.children = []
        self.padre = padre
    def add_child(self, obj):
        self.children.append(obj)


class Rubik(object):
    def __init__(self):
        self.face1 = None
        self.face2 = None
        self.face3 = None
        self.face4 = None
        self.face5 = None
        self.face6 = None
    def face_1(self, flag):
        if flag:
            self.face1 = np.rot90(self.face1, 3)
            temp = copy.deepcopy(self.face3[:, 0])  # This saves the first column thatt is being updated
            self.face3[:, 0] = self.face2[2, :]
            temp2 = copy.deepcopy(self.face5[0, :])
            self.face5[0, :] = np.flip(temp, -1)
            temp = copy.deepcopy(self.face6[:, 2])
            self.face6[:, 2] = temp2
            self.face2[2, :] = np.flip(temp, -1)

        else:
            self.face1 = np.rot90(self.face1)
            # Update face1 and face2
            temp = copy.deepcopy(self.face3[:, 0])  # This saves the first column that is being updated
            self.face3[:, 0] = np.flip(self.face5[0, :], -1)
            temp2 = copy.deepcopy(self.face2[2, :])
            self.face2[2, :] = temp
            temp = copy.deepcopy(self.face6[:, 2])
            self.face6[:, 2] = np.flip(temp2, -1)
            self.face5[0, :] = temp
        # return face1, face2, face3, face5, face6
    def face_2(self, flag):
        if flag:
            self.face2 = np.rot90(self.face2, 3)
            temp = copy.deepcopy(self.face3[0, :])  # This saves the first column thatt is being updated
            self.face3[0, :] = self.face4[:, 2]
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face6[:, 0])
            self.face6[:, 0] = temp2
            self.face4[:, 2] = temp

        else:
            self.face2 = np.rot90(self.face2)
            temp = copy.deepcopy(self.face6[0, :])  # This saves the first column that is being updated
            self.face6[0, :] = np.flip(self.face4[2, :], -1)
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face3[0, :])
            self.face3[0, :] = temp2
            self.face4[2, :] = np.flip(temp, -1)
        # return face1, face2, face3, face4, face6
    def face_3(self, flag):
        if flag:
            self.face3 = np.rot90(self.face3, 3)
            # Update face1 and face2
            temp = copy.deepcopy(self.face4[:, 2])  # This saves the first column thatt is being updated
            self.face4[:, 2] = copy.deepcopy(self.face2[:, 2])
            temp2 = copy.deepcopy(self.face5[:, 2])
            self.face5[:, 2] = temp
            temp = copy.deepcopy(self.face1[:, 2])
            self.face2[:, 2] = temp
            self.face1[:, 2] = temp2

        else:
            self.face3 = np.rot90(self.face3)
            temp = copy.deepcopy(self.face1[:, 2])
            temp2 = copy.deepcopy(self.face2[:, 2])
            temp3 = copy.deepcopy(self.face4[:, 2])
            temp4 = copy.deepcopy(self.face5[:, 2])
            self.face4[:, 2] = temp4
            self.face5[:, 2] = temp
            self.face1[:, 2] = temp2
            self.face2[:, 2] = temp3

        # return face1, face2, face3, face4, face5
    def face_4(self, flag):
        if flag:
            self.face4 = np.rot90(self.face4, 3)
            temp = copy.deepcopy(self.face5[2, :])
            temp2 = copy.deepcopy(self.face3[:, 2])
            temp3 = copy.deepcopy(self.face2[0, :])
            temp4 = copy.deepcopy(self.face6[:, 0])
            self.face5[2, :] = temp4
            self.face3[:, 2] = np.flip(temp, -1)
            self.face2[0, :] = temp2
            self.face6[:, 0] = np.flip(temp3, -1)

        else:
            self.face4 = np.rot90(self.face4)
            temp = copy.deepcopy(self.face5[2, :])
            temp2 = copy.deepcopy(self.face3[:, 2])
            temp3 = copy.deepcopy(self.face2[0, :])
            temp4 = copy.deepcopy(self.face6[:, 0])
            self.face5[2, :] = np.flip(temp2, -1)
            self.face3[:, 2] = temp3
            self.face2[0, :] = np.flip(temp4, -1)
            self.face6[:, 0] = temp
    def face_5(self, flag):
        if flag:
            self.face5 = np.rot90(self.face5, 3)
            temp = copy.deepcopy(self.face3[:, 0])  # This saves the first column thatt is being updated
            self.face3[:, 0] = self.face1[:, 0]
            temp2 = copy.deepcopy(self.face4[:, 0])
            self.face4[:, 0] = temp
            temp = copy.deepcopy(self.face6[:, 0])
            self.face6[:, 0] = temp2
            self.face1[:, 0] = temp

        else:
            self.face5 = np.rot90(self.face5)
            # Update face1 and face2
            temp = copy.deepcopy(self.face3[2, :])  # This saves the first column that is being updated
            self.face3[2, :] = np.flip(self.face4[0, :],-1)
            temp2 = copy.deepcopy(self.face1[2, :])
            self.face1[2, :] = temp
            temp = copy.deepcopy(self.face6[2, :])
            self.face6[2, :] = temp2
            self.face4[0, :] = np.flip(temp,-1)
        # return face1, face3, face4, face5, face6
    def face_6(self, flag):
        if flag:
            self.face6 = np.rot90(self.face6, 3)
            temp = copy.deepcopy(self.face1[:, 0])  # This saves the first column thatt is being updated
            self.face1[:, 0] = self.face2[:, 0]
            temp2 = copy.deepcopy(self.face5[:, 0])
            self.face5[:, 0] = temp
            temp = copy.deepcopy(self.face4[:, 0])
            self.face4[:, 0] = temp2
            self.face2[:, 0] = temp

        else:
            self.face6 = np.rot90(self.face6)
            temp = copy.deepcopy(self.face5[:, 0])  # This saves the first column that is being updated
            self.face5[:, 0] = self.face4[:, 0]
            temp2 = copy.deepcopy(self.face1[:, 0])
            self.face1[:, 0] = temp
            temp = copy.deepcopy(self.face2[:, 0])
            self.face2[:, 0] = temp2
            self.face4[:, 0] = temp
        # return face1, face2, face4, face5, face6
    def show(self):
        print("Cara1: ")
        print(self.face1)
        print("Cara2: ")
        print(self.face2)
        print("Cara3: ")
        print(self.face3)
        print("Cara4: ")
        print(self.face4)
        print("Cara5: ")
        print(self.face5)
        print("Cara6: ")
        print(self.face6)

    def heuristic(self):
        counter = 0
        counter += (self.face1 == np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]).reshape((3, 3))).sum()
        counter += (self.face2 == np.array([21, 22, 23, 24, 25, 26, 27, 28, 29]).reshape((3, 3))).sum()
        counter += (self.face3 == np.array([31, 32, 33, 34, 35, 36, 37, 38, 39]).reshape((3, 3))).sum()
        counter += (self.face4 == np.array([41, 42, 43, 44, 45, 46, 47, 48, 49]).reshape((3, 3))).sum()
        counter += (self.face5 == np.array([51, 52, 53, 54, 55, 56, 57, 58, 59]).reshape((3, 3))).sum()
        counter += (self.face6 == np.array([61, 62, 63, 64, 65, 66, 67, 68, 69]).reshape((3, 3))).sum()
        return counter

    def heuristic2(self):
        counter = 0
        if np.count_nonzero(self.face1 == 1) == 9:
            counter += 1
        if np.count_nonzero(self.face2 == 2) == 9:
            counter += 1
        if np.count_nonzero(self.face3 == 3) == 9:
            counter += 1
        if np.count_nonzero(self.face4 == 4) == 9:
            counter += 1
        if np.count_nonzero(self.face5 == 5) == 9:
            counter += 1
        if np.count_nonzero(self.face6 == 6) == 9:
            counter += 1
        return counter

    def random_cube(self):
        random_cube2(2)

    def random_cube2(self, num_steps):
        for i in range(1, num_steps):
            r = random.randint(1, 6)

            r2 = random.choice([True, False])

            if r == 1:
                self.face_1(r2)
            if r == 2:
                self.face_2(r2)
            if r == 3:
                self.face_3(r2)
            if r == 4:
                self.face_4(r2)
            if r == 5:
                self.face_5(r2)
            if r == 6:
                self.face_6(r2)
    
    def backtracking(self, sneaky):
        #sneaky.append([r, r2])
        rev_sneaky = sneaky[4:]
        rev_sneaky = rev_sneaky[::-1]
        for each in rev_sneaky:
            initT()
            r = each[0]
            r2 = each[1]
            if r2 == 1:
                print("Se giro la cara: ", r, " Hacia la derecha")
            else:
                print("Se giro la cara: ", r, " Hacia la izquierda")
            if r2 == 1:
                r2 = False
            else:
                r2 = True

            if r == 1:
                self.face_1(r2)
            if r == 2:
                self.face_2(r2)
            if r == 3:
                self.face_3(r2)
            if r == 4:
                self.face_4(r2)
            if r == 5:
                self.face_5(r2)
            if r == 6:
                self.face_6(r2)

    def initial(self):
        self.face1 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]).reshape((3, 3))
        self.face2 = np.array([21, 22, 23, 24, 25, 26, 27, 28, 29]).reshape((3, 3))
        self.face3 = np.array([31, 32, 33, 34, 35, 36, 37, 38, 39]).reshape((3, 3))
        self.face4 = np.array([41, 42, 43, 44, 45, 46, 47, 48, 49]).reshape((3, 3))
        self.face5 = np.array([51, 52, 53, 54, 55, 56, 57, 58, 59]).reshape((3, 3))
        self.face6 = np.array([61, 62, 63, 64, 65, 66, 67, 68, 69]).reshape((3, 3))

def addChild(parent, depth):  # , rubik):
    rubik_Copy = copy.deepcopy(parent.rubik)
    for i in range(0, 12):
        if (i == 0):
            rubik_Copy.face_1(True)
        elif (i == 1):
            rubik_Copy.face_1(False)
        elif (i == 2):
            rubik_Copy.face_2(True)
        elif (i == 3):
            rubik_Copy.face_2(False)
        elif (i == 4):
            rubik_Copy.face_3(True)
        elif (i == 5):
            rubik_Copy.face_3(False)
        elif (i == 6):
            rubik_Copy.face_4(True)
        elif (i == 7):
            rubik_Copy.face_4(False)
        elif (i == 8):
            rubik_Copy.face_5(True)
        elif (i == 9):
            rubik_Copy.face_5(False)
        elif (i == 10):
            rubik_Copy.face_6(True)
        elif (i == 11):
            rubik_Copy.face_6(False)
        # print("herustic: ",rubik_Copy.herustic())
        new_node = Node(i, rubik_Copy.heuristic(), parent, rubik_Copy)
        parent.add_child(new_node)
    depth = + 1
    return parent, depth

def path(nodo, Tree_path):
    if (nodo != None):
        print("-", nodo.cube_pos)
        Tree_path.append(nodo.cube_pos)
        path(nodo.padre, Tree_path)
    return Tree_path

def initTree(init, depth):
    # print("Numero de hijos: ", len(init.children))
    if not 0 < len(init.children):
        init.children = []
        init, depth = addChild(init, depth - 1)
    for i in range(0, 12):
        init.children[i], depth = addChild(init.children[i], depth)
    for i in range(0, 12):
        for j in range(0, 12):
            init.children[i].children[j], depth = addChild(init.children[i].children[j], depth)
    for i in range(0, 12):
        for j in range(0, 12):
            for k in range(0, 12):
                init.children[i].children[j].children[k], depth = addChild(init.children[i].children[j].children[k],
                                                                           depth)
    return init, depth

def BuscarMayor(init, nodomayor):
    mayor = 0
    for i in range(0, 12):
        for j in range(0, 12):
            for k in range(0, 12):
                for l in range(0, 12):
                    nodo = init.children[i].children[j].children[k].children[l]
                    # print("value: ", nodo.value," pos: ", nodo.cube_pos)
                    # print("Esto es el valor del nodo: ", nodo.value)
                    if mayor < nodo.value:
                        mayor = nodo.value
                        nodomayor = nodo
    return init, nodomayor

def add_face_move(var, cube_moves):
    cube_moves.append(var)

"""MAIN"""

def rotate_face(var, rubik,cube_moves):
    if(str(var) == "rf1"):   
        rubik.face_1(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf2"):   
        rubik.face_2(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf3"):   
        rubik.face_3(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf4"):   
        rubik.face_4(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf5"):   
        rubik.face_5(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf6"):   
        rubik.face_6(True)
        add_face_move(var,cube_moves)

    if(str(var) == "lf1"):   
        rubik.face_1(False)
        add_face_move(var,cube_moves)
    if(str(var) == "lf2"):   
        rubik.face_2(False)
        add_face_move(var,cube_moves)
    if(str(var) == "lf3"):   
        rubik.face_3(False)
        add_face_move(var,cube_moves)
    if(str(var) == "lf4"):   
        rubik.face_4(False)
        add_face_move(var,cube_moves)
    if(str(var) == "lf5"):   
        rubik.face_5(False)
        add_face_move(var,cube_moves)
    if(str(var) == "lf6"):   
        rubik.face_6(False)
        add_face_move(var,cube_moves)

def rotate_face2(var, rubik):
    if(str(var) == "rf1"):   
        rubik.face_1(True)
    if(str(var) == "rf2"):   
        rubik.face_2(True)
    if(str(var) == "rf3"):   
        rubik.face_3(True)
    if(str(var) == "rf4"):   
        rubik.face_4(True)
    if(str(var) == "rf5"):   
        rubik.face_5(True)
    if(str(var) == "rf6"):   
        rubik.face_6(True)

    if(str(var) == "lf1"):   
        rubik.face_1(False)
    if(str(var) == "lf2"):   
        rubik.face_2(False)
    if(str(var) == "lf3"):   
        rubik.face_3(False)
    if(str(var) == "lf4"):   
        rubik.face_4(False)
    if(str(var) == "lf5"):   
        rubik.face_5(False)
    if(str(var) == "lf6"):   
        rubik.face_6(False)

def random_cube(var, rubik):
    if str(var) == "random cube" :
        rubik.random_cube2(10)

def instructions(var):
    if str(var) == "instructions" :
        while True:
            os.system('cls')

            print("comandos usados:\n")
            print("--> movimiento de caras:\n")
            print("     -> cara 1:\n")
            print("          * Derecha  : 'rf1'\n")
            print("          * Izquierda: 'lf1'\n")
            print("     -> cara 2:\n")
            print("          * Derecha  : 'rf2'\n")
            print("          * Izquierda: 'lf2'\n")
            print("     -> cara 3:\n")
            print("          * Derecha  : 'rf3'\n")
            print("          * Izquierda: 'lf3'\n")
            print("     -> cara 4:\n")
            print("          * Derecha  : 'rf4'\n")
            print("          * Izquierda: 'lf4'\n")
            print("     -> cara 5:\n")
            print("          * Derecha  : 'rf5'\n")
            print("          * Izquierda: 'lf5'\n")
            print("     -> cara 6:\n")
            print("          * Derecha  : 'rf6'\n")
            print("          * Izquierda: 'lf6'\n")
            print("--> Generar un cubo aleatoriamente: 'random cube'\n")
            print("--> Generar un el cubo inicial o resetear el cubo:\n 'reset'\n")
            print("--> Resolver el cubo actual paso a paso: 'solve'\n")
            var = input("WRITE 'back' TO BACK TO DE RUBIK CUBE \n")
            if str(var) == "back":
                os.system('cls')
                break

def get_inverse_cube_move(move):
    if(move == "rf1"):
        return "lf1"       
    if(move == "rf2"):
        return "lf2"       
    if(move == "rf3"):
        return "lf3"       
    if(move == "rf4"):
        return "lf4"       
    if(move == "rf5"):
        return "lf5"       
    if(move == "rf6"):
        return "lf6"   
    if(move == "lf1"):
        return "rf1"   
    if(move == "lf2"):
        return "rf2"   
    if(move == "lf3"):
        return "rf3"   
    if(move == "lf4"):
        return "rf4"   
    if(move == "lf5"):
        return "rf5"   
    if(move == "lf6"):
        return "rf6"
    return ""  


def solve(var, rubik,cube_moves):
    print("el cubo se resolvera")
    vec = []
    if str(var) == "solve cube" :
        longitud = len(cube_moves)

        if longitud > 5:
            cube_moves1 = np.flip(cube_moves, -1)

            for move in cube_moves1:
                vec.append(get_inverse_cube_move(move))
                rotate_face2(get_inverse_cube_move(move) ,rubik)
                try:
                    os.system('cls')
                    rubik.show()
                    input("Press enter to continue")
                except SyntaxError:
                    pass
                if longitud == 5:
                    break
                longitud = longitud - 1
        if(longitud <= 5 ):
            print("solve")
            
            depth = 0
            nodomayor = None
            #start_time = time.time()
            Tree_path = []
            
            init = Node("initial", rubik.heuristic, None, rubik)

            init, depth = addChild(init, depth) 
            #print(rubik.heuristic())
            #rubik.random_cube()
            #rubik.show()
            while (init.value != 54):
                init, depth = initTree(init, depth)
                init, nodomayor = BuscarMayor(init, nodomayor)
                init = copy.deepcopy(nodomayor);
                #print("mayor: ", nodomayor.value, " posicion Mayor: ", nodomayor.cube_pos, " padre: ", nodomayor.padre.cube_pos)
                Tree_path = path(nodomayor, Tree_path)
                #print(Tree_path[::-1])  # voltea el vector
            
            #print("--- {} seconds ---".format(time.time() - start_time))

def heuristics(var, rubik):
    if str(var) == "heuristic":
        print("heuristica:", rubik.heuristic())
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass

if __name__ == '__main__':
    """MAIN"""
    #file = open("cubei.txt", "r") 
    cube_moves = []
    rubik = Rubik()
    rubik.initial()

    rubik_initial = copy.deepcopy(rubik)
    var = ""
    while(True):
        os.system('cls')
        #print (file.read()) 
        if str(var) == "exit" :
            break
        if str(var) == "reset":
            rubik = copy.deepcopy(rubik_initial)

        random_cube(var ,rubik)
        rotate_face(var ,rubik,cube_moves)
        instructions(var)
        solve(var,rubik,cube_moves)
        heuristics(var, rubik)

        rubik.show()
        var = input("Write the number of the face to be rotated or \n'exit' to exit \n")
        print ("you entered", var)

    os.system('cls')
    print("you exit() of the rubik solver")