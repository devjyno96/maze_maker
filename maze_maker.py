import random


class maze_maker :
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    

    def __init__(self, seed = None):
        self.DIRECTION_RANDOM = random
        if seed != None :
            self.DIRECTION_RANDOM.seed(seed)


    def change_seed(self, seed):
        self.DIRECTION_RANDOM.seed(seed)


    def check_make_way_possible(self, maze_dic, location, direction):
        location_shift = []

        if direction == self.UP :
            location_shift = [-1, 0]
        elif direction == self.DOWN :
            location_shift = [1, 0]
        elif direction == self.LEFT :
            location_shift = [0, -1]
        elif direction == self.RIGHT :
            location_shift = [0, 1]
        next_location = [location[0] + location_shift[0], location[1] + location_shift[1]]
        # 가장자리 확인
        if next_location[0] <= 0 or next_location[1] <= 0 or next_location[1] >= maze_dic['width']-1 or next_location[0] >= maze_dic['height']-1 :
            return False
        
        # 이미 지나간 길인 경우
        if maze_dic['maze'][next_location[0]][next_location[1]] == 1 :
            return False

        # 해당 방향 좌, 우에 길이 나있는 경우 false
        if location_shift[0] == 0:# 좌우 이동했음, 이동한 좌표의 위, 아래를 확인해봐야함
            if maze_dic['maze'][next_location[0] + 1][next_location[1]] == 1 or maze_dic['maze'][next_location[0] - 1][next_location[1]] == 1:
                return False
        if location_shift[1] == 0:# 상하 이동했음, 이동한 좌표의 좌 우 를 확인해봐야함
            if maze_dic['maze'][next_location[0]][next_location[1] + 1] == 1 or maze_dic['maze'][next_location[0]][next_location[1] - 1] == 1:
                return False

        # 벽 뒤에 길이 있는 경우
        next_location[0] += location_shift[0]
        next_location[1] += location_shift[1]

        # 해당 방향 좌, 우에 길이 나있는 경우 false
        if location_shift[0] == 0:# 좌우 이동했음, 이동한 좌표의 위, 아래를 확인해봐야함
            if maze_dic['maze'][next_location[0] + 1][next_location[1]] == 1 or maze_dic['maze'][next_location[0] - 1][next_location[1]] == 1:
                return False
        if location_shift[1] == 0:# 상하 이동했음, 이동한 좌표의 좌 우 를 확인해봐야함
            if maze_dic['maze'][next_location[0]][next_location[1] + 1] == 1 or maze_dic['maze'][next_location[0]][next_location[1] - 1] == 1:
                return False
        
        return True

    def make_maze(self, width, height, way_in= [0, 1], way_out = None) :
        """make maze 2 X 2 metrix

        Args:
            width ([int]): [maze width decide]
            height ([int]): [maze height decide]
            entry ([[int, int]]): [maze entry decide]
            exit ([[int, int]]): [maze exit decide]
        """
        maze_dic = {
            "width" : width,
            "height" : height,
            "way_in" : way_in,
            "way_out" : way_out,
            "maze" : [],
        }

        rand_direction = lambda x  : self.DIRECTION_RANDOM.randint(1, x)
        if way_out == None :
            maze_dic['way_out'] = [height-1, width - 2]
        
        maze_dic['maze'] = [[ 0 for _ in range (width)] for _ in range(height)]
        maze_dic['maze'][maze_dic['way_in'][0]][maze_dic['way_in'][1]] = 1 # entry

        stack = [ maze_dic['way_in'] ]
        
        while stack :

            possible_direction = []
            for i in range(1,5):#4가지 방향 진행
                #  갈 수 있는 방향 전부 조사 - 갈 수 있는 길만 possible_direction에 저장
                if self.check_make_way_possible(maze_dic, stack[-1], i):
                    possible_direction.append(i)

            if len(possible_direction) == 0 : #갈 수 있는곳이 없다면? pop
                stack.pop()
                continue

            direction = possible_direction[rand_direction(len(possible_direction)) -1 ]
            location_shift = []
            if direction == self.UP :
                location_shift = [-1, 0]
            elif direction == self.DOWN :
                location_shift = [1, 0]
            elif direction == self.LEFT :
                location_shift = [0, -1]
            elif direction == self.RIGHT :
                location_shift = [0, 1]

            maze_dic['maze'][stack[-1][0]+location_shift[0]][stack[-1][1] + location_shift[1]] = 1
            stack.append([stack[-1][0]+location_shift[0], stack[-1][1] + location_shift[1]])
        
        maze_dic['maze'][maze_dic['way_out'][0]][maze_dic['way_out'][1]] = 1 #exit


        return maze_dic
                        

    def check_move_way_possible(self, maze_dic, location, direction):
        location_shift = []
        if direction == self.UP :
            location_shift = [-1, 0]
        elif direction == self.DOWN :
            location_shift = [1, 0]
        elif direction == self.LEFT :
            location_shift = [0, -1]
        elif direction == self.RIGHT :
            location_shift = [0, 1]
            
        if maze_dic['maze'][ location[0] + location_shift[0] ][ location[1] + location_shift[1] ] != 1:
            return False
        
        return True


    def solve_maze(self, maze_dic):
        """[summary]

        Args:
            maze_dic ([dictionaly]): maze_dic = {
                                    "width" : width,
                                    "height" : height,
                                    "way_in" : way_in,
                                    "way_out" : way_out,
                                    "maze" : []
        }
        """
        # 0 : 벽 / 1 : 길 / 2 : 방문한 길 / 3 : 갈 수 없는 길
        stack = [ maze_dic['way_in'] ]
        check = False
        while stack :
            location = stack[-1]
            maze_dic['maze'][location[0]][location[1]] = 2 # 방문했음
            if location == maze_dic['way_out'] :
                check = True
                break
            
            possible_direction = []
            for i in range(1, 5):
                if self.check_move_way_possible(maze_dic, location, i):
                    possible_direction.append(i)

            if len(possible_direction) == 0 :
                maze_dic['maze'][location[0]][location[1]] = 3 #갈 수 없는길                
                stack.pop()
                continue
            
            for direction in possible_direction:
                location_shift = []
                if direction == self.UP :
                    location_shift = [-1, 0]
                elif direction == self.DOWN :
                    location_shift = [1, 0]
                elif direction == self.LEFT :
                    location_shift = [0, -1]
                elif direction == self.RIGHT :
                    location_shift = [0, 1]
                stack.append([ location[0]+location_shift[0] , location[1] + location_shift[1] ])
            

        return maze_dic, check


    def get_maze(self, width, height, way_in= [0, 1], way_out = None) :
        maze = self.make_maze(width, height, way_in, way_out = None)
        maze_solved, maze_solved_possible = self.solve_maze(maze)
        while not maze_solved_possible :
            maze_solved, maze_solved_possible = self.solve_maze(maze)
            if maze_solved_possible == False : # 풀 수 없는 미로의 경우 다시 생성
                continue
        return maze_solved

