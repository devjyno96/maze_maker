import random


class maze_maker :
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    def __init__(self):
        print("class create")


    def check_make_way_possible(self, maze_dic, location, direction):
        # location [x, y]  direction : 1~4 (1 : UP , 2 : DOWN ,  3: LEFT, 4:RIGHT)
        # 어떤 상황에 갈 수 없는가?
        # 1. 해당 방향이 가장자리인경우
        # 2. 이미 지나간길인 경우
        # 3. 벽 뒤에 길이 있는경우? - 벽뒤에 길이 있는데도 뚤으면 모든 벽이 없어질것
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
            # print("check out line" + str(direction))
            # print(next_location + location_shift)
            return False
        
        # 이미 지나간 길인 경우
        if maze_dic['maze'][next_location[0]][next_location[1]] == 1 :
            # print("check already made path" + str(direction))
            # print(location_shift)
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
        if maze_dic['maze'][next_location[0]][next_location[1]] == 1 :
            # print("check behind wall" + str(direction))
            # print(location_shift)
            return False
        
        return True

    """
    1. 미로 생성
    1.1 미로는 어떻게 만들것인지??
        가로 X 세로 를 주고 만들게 하기
        인자는 뭘 줄껀지? (가로, 세로)
        그럼 입, 출구는 내가 지정? 아님 고정? (변수로 받자)
        반환은 2차원 배열로
        미로내부 구성(0 벽, 1 길, 2 정답)
    """
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

        rand_direction = lambda x  : random.randint(1, x)
        if way_out == None :
            maze_dic['way_out'] = [height-1, width - 2]
        
        maze_dic['maze'] = [[ 0 for _ in range (width)] for _ in range(height)]
        maze_dic['maze'][maze_dic['way_in'][0]][maze_dic['way_in'][1]] = 1 # entry
        maze_dic['maze'][maze_dic['way_out'][0]][maze_dic['way_out'][1]] = 1 #exit

        stack = [ maze_dic['way_in'] ]
        
        """
            1. 어디로 갈지 정하는 함수 필요 - rand_direction 1~4
            2. 정해진 방향이 갈 수 있는 길인지 확인 하는 함수 - check_make_way_possible
            3. 위치 이동시키는 함수 필요 - 
            4. stack 관리 필요
            1. 갈 수 있는 방향의 수 찾기
            1.1 갈 수 있는 길이 없다 - pop
            1.2 갈 수 있는 길이 있다 - 그 길중 하나 진행 push
            갈 수 있는 길이 없을때 까지 반복 - stack이 빌때 까지 진행
        """
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

        return maze_dic
                        


    """
    2. 미로 해석
        미로 배열을 받아서 해답인 길을 포함한 배열을 반환하도록
        정답 길을 2로 채운 후 반환
    """
    def solve_maze(self, maze):
        print("solve_maze")

    

if __name__ == "__main__" :
    test = maze_maker()
    maze = test.make_maze(100,20)['maze']
    maze_str = []
    temp = ""
    for line in maze :
        temp = ''
        for i in line:
            if i == 0:
                temp += "■"
            else :
                temp += "□"
        maze_str.append(temp)
    # print(maze_str)
    f = open('maze.txt', 'w', encoding="utf=8")
    for i in maze_str:
        f.writelines(i)
        f.writelines("\n")
