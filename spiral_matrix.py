# leet-code #59
# Given a positive integer n, generate a square matrix filled with elements from 1 to n**2 in spiral order.

def generateMatrix(n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0]*n for i in range(n)]
        
        vectors = [[0,1], [1, 0], [0,-1], [-1, 0]]
        current_vec_idx = 0
        x,y = 0, 0
    
        for i in range(n**2 -1):
            # insert point
            ret[x][y] = i + 1  # start from 0, plus 1
                            
            # find next (x, y)
            while True:
                # find vector
                vec_x, vec_y = vectors[current_vec_idx % len(vectors)]
                next_x = x + vec_x
                next_y = y + vec_y
                
                # check next x, y is available and not occupied
                if 0 <= next_x < n and 0<= next_y < n and ret[next_x][next_y] == 0:
                    x = next_x
                    y = next_y
                    break
                else:
					# try next vector
                    current_vec_idx += 1
        
        # insert final point
        ret[x][y] = n**2
        
        return ret
        
if __name__ == '__main__':
        n = ''
        generateMatrix(n)
  
