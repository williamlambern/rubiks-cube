#centre of cube i,j,k 0,0,0

'''
to add:
- ai
'''

from rotation_matrices import *


class Cube:
    
    def __init__(self):
        self.data = []
        self.sorted = [[],[],[]]
        self.reset()

    def reset(self):
        
        #front
        self.data.append(Piece(-1,1,1, ['b','r','w']))
        self.data.append(Piece(0,1,1, [None,'r','w']))
        self.data.append(Piece(1,1,1, ['g','r','w']))

        self.data.append(Piece(-1,0,1, ['b',None,'w']))
        self.data.append(Piece(0,0,1, [None,None,'w']))
        self.data.append(Piece(1,0,1, ['g',None,'w']))

        self.data.append(Piece(-1,-1,1, ['b','o','w']))
        self.data.append(Piece(0,-1,1, [None,'o','w']))
        self.data.append(Piece(1,-1,1, ['g','o','w']))

        #middle
        self.data.append(Piece(-1,1,0, ['b','r',None]))
        self.data.append(Piece(0,1,0, [None,'r',None]))
        self.data.append(Piece(1,1,0, ['g','r',None]))

        self.data.append(Piece(-1,0,0, ['b',None,None]))
        self.data.append(Piece(0,0,0, [None,None,None])) #centre piece
        self.data.append(Piece(1,0,0, ['g',None,None]))
        
        self.data.append(Piece(-1,-1,0, ['b','o',None]))
        self.data.append(Piece(0,-1,0, [None,'o',None]))
        self.data.append(Piece(1,-1,0, ['g','o',None]))

        #back
        self.data.append(Piece(-1,1,-1, ['b','r','y']))
        self.data.append(Piece(0,1,-1, [None,'r','y']))
        self.data.append(Piece(1,1,-1, ['g','r','y']))
        
        self.data.append(Piece(-1,0,-1, ['b',None,'y']))
        self.data.append(Piece(0,0,-1, [None,None,'y']))
        self.data.append(Piece(1,0,-1, ['g',None,'y']))

        self.data.append(Piece(-1,-1,-1, ['b','o','y']))
        self.data.append(Piece(0,-1,-1, [None,'o','y']))
        self.data.append(Piece(1,-1,-1, ['g','o','y']))

        self.sort() #store in a logical way. A dictionary with keys [ijk]

    def sort(self):
        self.sorted = {}
        for p in range(len(self.data)):
            self.sorted[str(str(self.data[p].i) + str(self.data[p].j) + str(self.data[p].k))] = self.data[p]
            
    def rotate(self,fr):
        fr = fr.lower()
        transformation_vectors = {'l' : l, "l'" : l_prime, 'r' : r, "r'" : r_prime, 'f' : f, "f'" : f_prime, 'b' : b, "b'" : b_prime, 'u' : u, "u'" : u_prime, 'd' : d, "d'" : d_prime}
        
        if fr == 'l' or fr == "l'":
            for p in range(len(self.data)):
                if self.data[p].i == -1: #x=-1 (left face)
                    position = [self.data[p].i,self.data[p].j,self.data[p].k]
                    new_position = self.matrix_multiplication(transformation_vectors[fr],position)
                    
                    self.data[p].i = new_position[0]
                    self.data[p].j = new_position[1]
                    self.data[p].k = new_position[2]

                    colours_before = self.data[p].colour
                    colours_after = [colours_before[0], colours_before[2], colours_before[1]]
                    self.data[p].colour = colours_after

        if fr == 'r' or fr == "r'":
            for p in range(len(self.data)):
                if self.data[p].i == 1: #x=1 (right face)
                    position = [self.data[p].i,self.data[p].j,self.data[p].k]
                    new_position = self.matrix_multiplication(transformation_vectors[fr],position)
                    
                    self.data[p].i = new_position[0]
                    self.data[p].j = new_position[1]
                    self.data[p].k = new_position[2]

                    colours_before = self.data[p].colour
                    colours_after = [colours_before[0], colours_before[2], colours_before[1]]
                    self.data[p].colour = colours_after

        if fr == 'f' or fr == "f'":
            for p in range(len(self.data)):
                if self.data[p].k == 1: #k=-1 (front face)
                    position = [self.data[p].i,self.data[p].j,self.data[p].k]
                    new_position = self.matrix_multiplication(transformation_vectors[fr],position)
                    
                    self.data[p].i = new_position[0]
                    self.data[p].j = new_position[1]
                    self.data[p].k = new_position[2]

                    colours_before = self.data[p].colour
                    colours_after = [colours_before[1], colours_before[0], colours_before[2]]
                    self.data[p].colour = colours_after

        if fr == 'b' or fr == "b'":
            for p in range(len(self.data)):
                if self.data[p].k == -1: #k=-1 (back face)
                    position = [self.data[p].i,self.data[p].j,self.data[p].k]
                    new_position = self.matrix_multiplication(transformation_vectors[fr],position)
                    
                    self.data[p].i = new_position[0]
                    self.data[p].j = new_position[1]
                    self.data[p].k = new_position[2]

                    colours_before = self.data[p].colour
                    colours_after = [colours_before[1], colours_before[0], colours_before[2]]
                    self.data[p].colour = colours_after

        if fr == 'u' or fr == "u'":
            for p in range(len(self.data)):
                if self.data[p].j == 1: #j=1 (top face)
                    position = [self.data[p].i,self.data[p].j,self.data[p].k]
                    new_position = self.matrix_multiplication(transformation_vectors[fr],position)
                    
                    self.data[p].i = new_position[0]
                    self.data[p].j = new_position[1]
                    self.data[p].k = new_position[2]

                    colours_before = self.data[p].colour
                    colours_after = [colours_before[2], colours_before[1], colours_before[0]]
                    self.data[p].colour = colours_after

        if fr == 'd' or fr == "d'":
            for p in range(len(self.data)):
                if self.data[p].j == -1: #j=-1 (bottom face)
                    position = [self.data[p].i,self.data[p].j,self.data[p].k]
                    new_position = self.matrix_multiplication(transformation_vectors[fr],position)
                    
                    self.data[p].i = new_position[0]
                    self.data[p].j = new_position[1]
                    self.data[p].k = new_position[2]

                    colours_before = self.data[p].colour
                    colours_after = [colours_before[2], colours_before[1], colours_before[0]]
                    self.data[p].colour = colours_after                   
        self.sort()

    def matrix_multiplication(self,tm,pv):
        #tm = transformation matrix , pv = position vector
        nv = []
        nv.append(tm[0][0]*pv[0] + tm[0][1]*pv[1] + tm[0][2]*pv[2])
        nv.append(tm[1][0]*pv[0] + tm[1][1]*pv[1] + tm[1][2]*pv[2])
        nv.append(tm[2][0]*pv[0] + tm[2][1]*pv[1] + tm[2][2]*pv[2])

        return nv

    def isCubeSolved(self):
        if self.isFaceSolved(x=-1) == True and self.isFaceSolved(x=0) == True:
            if self.isFaceSolved(x=1) == True:
                if self.isFaceSolved(y=-1) == True and self.isFaceSolved(y=0) == True:
                    if self.isFaceSolved(y=1) == True:
                        if self.isFaceSolved(z=-1) == True and self.isFaceSolved(z=0) == True:
                            if self.isFaceSolved(z=1) == True:
                                return True
        return False

    def isFaceSolved(self, **kwargs):
        if 'x' in kwargs.keys():
            value = kwargs['x']
            colour = 0
            toCheck = '{0}11 {0}01 {0}-11 {0}10 {0}00 {0}-10 {0}1-1 {0}0-1 {0}-1-1'.format(value).split(' ')
            
        elif 'y' in kwargs.keys():
            value = kwargs['y']
            colour = 1
            toCheck = '1{0}1 1{0}0 1{0}-1 0{0}1 0{0}0 0{0}-1 -1{0}1 -1{0}0 -1{0}-1'.format(value).split(' ')

        elif 'z' in kwargs.keys():
            value = kwargs['z']
            colour = 2
            toCheck = '11{0} 10{0} 1-1{0} 01{0} 00{0} 0-1{0} -11{0} -10{0} -1-1{0}'.format(value).split(' ')
            
        else:
            return False #call error
   
        for i in range(len(toCheck)-1):
            if self.sorted[toCheck[i]].colour[colour] != self.sorted[toCheck[i+1]].colour[colour]:         
                return False
        return True

    def numberOfPairs(self):
        pairs = 0
        for i in range(-1,1):
            for j in range(-1,1):
                for k in range(-1,1):
                    for c in range(3):
                        if self.sorted['{}{}{}'.format(i,j,k)].colour[c] != None:
                            if self.sorted['{}{}{}'.format(i,j,k)].colour[c] == self.sorted['{}{}{}'.format(i,j,k+1)].colour[c]:
                                pairs += 1
                            if self.sorted['{}{}{}'.format(i,j,k)].colour[c] == self.sorted['{}{}{}'.format(i,j+1,k)].colour[c]:
                                pairs += 1
                            if self.sorted['{}{}{}'.format(i,j,k)].colour[c] == self.sorted['{}{}{}'.format(i+1,j,k)].colour[c]:
                                pairs += 1
        return pairs
    

class Piece:

    def __init__(self,i,j,k,colour):
        self.i = i
        self.j = j
        self.k = k
        self.colour = colour #list in form [ci,cj,ck}




