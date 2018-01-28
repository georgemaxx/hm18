matrix = [
     [1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]
]


a=[[[matrix[a][0]] for a in range(3)],
   [[matrix[a][1]] for a in range(3)],
   [[matrix[a][2]] for a in range(3)],
   [[matrix[a][3]] for a in range(3)]
   ]

a=[[matrix[a][b] for a in range(3)] for b in range(4)]
