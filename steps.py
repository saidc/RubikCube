import os
import numpy as np

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
# addface move

def add_face_move2(var, cube_moves,face_move_back):
    lp=len(cube_moves)-1
    if lp > 0 :
        #print(get_inverse_cube_move(var))
        if(get_inverse_cube_move(var) != cube_moves[lp] ):
            cube_moves.append(var)
            print("se agrega el dato")
            face_move_back = False
        else:
            if (not face_move_back):
                print("no se agerga el dato")
                face_move_back = True
            else:
                cube_moves.append(var)
                print("se agrega el dato")
                face_move_back = False
    else:
        cube_moves.append(var)
        face_move_back = False
        print("se agrega el dato")
    return face_move_back

def add_face_move(var, cube_moves):
    cube_moves.append(var)

def rotate_face(var, cube_moves):
    if(str(var) == "rf1"):   
        #rubik.face_1(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf2"):   
        #rubik.face_2(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf3"):   
        #rubik.face_3(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf4"):   
        #rubik.face_4(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf5"):   
        #rubik.face_5(True)
        add_face_move(var,cube_moves)
    if(str(var) == "rf6"):   
        #rubik.face_6(True)
        add_face_move(var,cube_moves)
    if(str(var) == "lf1"):   
        #rubik.face_1(False
        add_face_move(var,cube_moves)
    if(str(var) == "lf2"):   
        #rubik.face_2(False
        add_face_move(var,cube_moves)
    if(str(var) == "lf3"):   
        #rubik.face_3(False
        add_face_move(var,cube_moves)
    if(str(var) == "lf4"):   
        #rubik.face_4(False
        add_face_move(var,cube_moves)
    if(str(var) == "lf5"):   
        #rubik.face_5(False
        add_face_move(var,cube_moves)
    if(str(var) == "lf6"):   
        #rubik.face_6(False
        add_face_move(var,cube_moves)

def rubik_show(var, cube_moves):
    if (str(var) == "show steps"):
        print("show solve step by step")
    else:
        print(cube_moves)
        
def solve(var , cube_moves):
    vec = []
    if str(var) == "solve" :
        print("se resolvera el cubo")
        longitud = len(cube_moves)
        cube_moves1 = np.flip(cube_moves, -1)
        for move in cube_moves1:
            vec.append(get_inverse_cube_move(move))
    return vec

if __name__ == '__main__':
    """MAIN"""
    cube_moves = []
    var = ""
    while(True):
        os.system('cls')
        #print (file.read()) 
        if str(var) == "exit" :
            break
        rotate_face(var , cube_moves)
        solve(var, cube_moves)
        rubik_show(var,cube_moves)
        var = input("Write the number of the face to be rotated or \n'exit' to exit \n")
        print ("you entered", var)

    os.system('cls')
    print("you exit() of the rubik solver")