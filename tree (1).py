import copy
import time
import random
import numpy as np

class Node(object):
    def __init__(self, cube_pos, value, padre, rubik):
        self.cube_pos = cube_pos 
        self.value = value
        #self.value2 = value2
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
            temp = copy.deepcopy(self.face3[:, 0])  # This saves the first column that is being updated
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

    def face_2(self, flag):
        if flag:
            self.face2 = np.rot90(self.face2, 3)
            temp = copy.deepcopy(self.face3[0, :])  # This saves the first column that is being updated
            self.face3[0, :] = np.flip(self.face4[2, :])
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face6[0, :])
            self.face6[0, :] = temp2
            self.face4[2, :] = np.flip(temp)

        else:
            self.face2 = np.rot90(self.face2)
            temp = copy.deepcopy(self.face6[0, :])  # This saves the first column that is being updated
            self.face6[0, :] = np.flip(self.face4[2, :], -1)
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face3[0, :])
            self.face3[0, :] = temp2
            self.face4[2, :] = np.flip(temp, -1)

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
            temp = copy.deepcopy(self.face3[2, :])  # This saves the first column that is being updated
            self.face3[2, :] = self.face1[2, :]
            temp2 = copy.deepcopy(self.face4[0, :])
            self.face4[0, :] = np.flip(temp)
            temp = copy.deepcopy(self.face6[2, :])
            self.face6[2, :] = np.flip(temp2)
            self.face1[2, :] = temp
           
        else:
            self.face5 = np.rot90(self.face5)
            # Update face1 and face2
            temp = copy.deepcopy(self.face3[2, :])  # This saves the first column that is being updated
            self.face3[2, :] = np.flip(self.face4[0, :])
            temp2 = copy.deepcopy(self.face1[2, :])
            self.face1[2, :] = temp
            temp = copy.deepcopy(self.face6[2, :])
            self.face6[2, :] = temp2
            self.face4[0, :] = np.flip(temp)

    def face_6(self, flag):
        if flag:
            self.face6 = np.rot90(self.face6, 3)
            temp = copy.deepcopy(self.face1[:, 0])  # This saves the first column that is being updated
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
        for i in range(1, 8):
            r = random.randint(1, 6)
            r2 = random.randint(1, 2)

            if r2 == 1:
                print("Se giro la cara: ", r, " Hacia la derecha")
            else:
                print("Se giro la cara: ", r, " Hacia la izquierda")
            if r2 == 1:
                r2 = True
            else:
                r2 = False

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
            rubik.show()

    def random_cube2(self):
        for i in range(1, 50):
            r = random.randint(1, 6)
            r2 = random.randint(1, 2)

            if r2 == 1:
                print("Se giro la cara: ", r, " Hacia la derecha")
            else:
                print("Se giro la cara: ", r, " Hacia la izquierda")
            if r2 == 1:
                r2 = True
            else:
                r2 = False

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


def addchild(parent, depth):

    # rubik_copy = copy.deepcopy(parent.rubik)
    for i in range(0, 12):
        rubik_copy = copy.deepcopy(parent.rubik)
        if i == 0:
            rubik_copy.face_1(True)
        elif i == 1:
            rubik_copy.face_1(False)
        elif i == 2:
            rubik_copy.face_2(True)
        elif i == 3:
            rubik_copy.face_2(False)
        elif i == 4:
            rubik_copy.face_3(True)
        elif i == 5:
            rubik_copy.face_3(False)
        elif i == 6:
            rubik_copy.face_4(True)
        elif i == 7:
            rubik_copy.face_4(False)
        elif i == 8:
            rubik_copy.face_5(True)
        elif i == 9:
            rubik_copy.face_5(False)
        elif i == 10:
            rubik_copy.face_6(True)
        elif i == 11:
            rubik_copy.face_6(False)

        new_node = Node(i, rubik_copy.heuristic(), parent, rubik_copy)
        """
        print("Jugada: ", i)
        new_node.rubik.show()  # SHOW ME THE MOVES
        print("Heuristica: ", new_node.value)"""
        parent.add_child(new_node)

    depth += 1
    return parent, depth

def path(nodo, Tree_path):
    if nodo is not None:
        print("-", nodo.cube_pos)
        Tree_path.append(nodo.cube_pos)
        path(nodo.padre, Tree_path)
    return Tree_path

def initTree(init, depth):
    if not len(init.children) > 0:
        init.children = []
        init, depth = addchild(init, depth - 1)
    for i in range(0, 12):
        init.children[i], depth = addchild(init.children[i], depth)
    for i in range(0, 12):
        for j in range(0, 12):
            init.children[i].children[j], depth = addchild(init.children[i].children[j], depth)

    for i in range(0, 12):
        for j in range(0, 12):
            for k in range(0, 12):
                init.children[i].children[j].children[k], depth = addchild(init.children[i].children[j].children[k], depth)

    return init, depth

def search_highest(init, nodomayor, mayor, rubik_face1, rubik_face2, rubik_face3):
    highest_node = copy.deepcopy(nodomayor)
    mayor2 = copy.deepcopy(mayor)
    rubik_f1 = copy.deepcopy(rubik_face1)
    rubik_f2 = copy.deepcopy(rubik_face2)
    rubik_f3 = copy.deepcopy(rubik_face3)
    for i in range(0, 12):
        nodo = init.children[i]
        if np.any(rubik_f1 == nodo.rubik.face1):  # and np.any(rubik_f2 is nodo.rubik.face2) and np.any(rubik_f3 is nodo.rubik.face3):
            print(rubik_f1, " = ", nodo.rubik.face1)
        if nodo.value >= mayor2 and (np.any(rubik_f1 is not nodo.rubik.face1) and np.any(rubik_f2 is not nodo.rubik.face2) and np.any(rubik_f3 is not nodo.rubik.face3)):
            mayor2 = nodo.value
            highest_node = nodo
        for j in range(0, 12):
            nodo = init.children[i].children[j]
            if np.any(rubik_f1 is nodo.rubik.face1) and np.any(rubik_f2 is nodo.rubik.face2) and np.any( rubik_f3 is nodo.rubik.face3):
                print("Pillado")
            if nodo.value >= mayor2 and (np.any(rubik_f1 is not nodo.rubik.face1) and np.any(rubik_f2 is not nodo.rubik.face2) and np.any(rubik_f3 is not nodo.rubik.face3)):
                mayor2 = nodo.value
                highest_node = nodo
            for k in range(0, 12):
                nodo = init.children[i].children[j].children[k]
                if np.any(rubik_f1 is nodo.rubik.face1) and np.any(rubik_f2 is nodo.rubik.face2) and np.any(rubik_f3 is nodo.rubik.face3):
                    print("Pillado")
                if nodo.value >= mayor2 and (np.any(rubik_f1 is not nodo.rubik.face1) and np.any(rubik_f2 is not nodo.rubik.face2) and np.any(rubik_f3 is not nodo.rubik.face3)):
                    mayor2 = nodo.value
                    highest_node = nodo
                for l in range(0, 12):
                    nodo = init.children[i].children[j].children[k].children[l]
                    if np.any(rubik_f1 is nodo.rubik.face1) and np.any(rubik_f2 is nodo.rubik.face2) and np.any(rubik_f3 is nodo.rubik.face3):
                        print("Pillado")
                    if nodo.value >= mayor2 and (np.any(rubik_f1 is not nodo.rubik.face1) and np.any(rubik_f2 is not nodo.rubik.face2) and np.any(rubik_f3 is not nodo.rubik.face3)):
                        mayor2 = nodo.value
                        highest_node = nodo
    print(highest_node)
    return init, highest_node, mayor2

if __name__ == '__main__':
    Tree_path = [] 
    """MAIN"""
    start_time = time.time()
    depth = 0
    nodomayor = None

    rubik = Rubik()
    rubik.initial()
    print(rubik.heuristic())
    rubik.random_cube()
    # rubik.show() Estado del cubo despues del random
    
    init = Node("initial", rubik.heuristic, None, rubik)
    print(init.cube_pos, init.padre)
    print(rubik.heuristic())

    #init, depth = addchild(init, depth)
    mayor3 = 0
    rubik_state_face1 = []
    rubik_state_face2 = []
    rubik_state_face3 = []

    while(init.value != 54):
        init, depth = initTree(init, depth)
        copia = copy.deepcopy(mayor3)
        init, nodomayor, mayor3 = search_highest(init, nodomayor, mayor3, rubik_state_face1, rubik_state_face2, rubik_state_face3)

        # Here we store every state of the cube
        #print(nodomayor.rubik.face1)
        rubik_state_face1.append(nodomayor.rubik.face1)
        rubik_state_face2.append(nodomayor.rubik.face2)
        rubik_state_face3.append(nodomayor.rubik.face3)
        print("Estado de faces 1: ", len(rubik_state_face1)) #, rubik_state_face1)
        print("Estado de faces 2: ", len(rubik_state_face2))
        print("Estado de faces 3: ", len(rubik_state_face3))

        init = copy.deepcopy(nodomayor)
        print("mayor: ", nodomayor.value, " posicion Mayor: ", nodomayor.cube_pos, " padre: ", nodomayor.padre.cube_pos)
        print("BEST POS")
        init.rubik.show()
        Tree_path = path(nodomayor, Tree_path)
        print(Tree_path[::-1])  # flip the vector

        """if copia >= mayor3:
            mayor3 = 0
            init.rubik.random_cube2()"""
    print("--- {} seconds ---".format(time.time() - start_time))
