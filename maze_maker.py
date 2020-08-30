import random


class maze_maker :
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    def __init__(self):
        print("class create")


    def check_make_way_possible(self, width, height, maze, location, direction):
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

        location[0] += location_shift[0]
        location[1] += location_shift[1]
        # 가장자리 확인
        if location[0] <= 0 or location[1] <= 0 or location[1] >= width or location[0] >= height :
            print("check out line" + str(direction))
            print(location_shift)
            return False
        
        # 이미 지나간 길인 경우
        if maze[location[0]][location[1]] == 1 :
            print("check already made path" + str(direction))
            print(location_shift)
            return False
        
        # 벽 뒤에 길이 있는 경우
        location[0] += location_shift[0]
        location[1] += location_shift[1]
        if maze[location[0]][location[1]] == 1 :
            print("check behind wall" + str(direction))
            print(location_shift)
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
        rand_direction = lambda : random.randint(1, 4)
        # 1 UP 2 DOWN 3 LEFT 4 RIGHT
        if way_out == None :
            way_out = [height-1, width - 2]
        
        maze = [[ 0 for _ in range (width)] for _ in range(height)]
        maze[way_in[0]][way_in[1]] = 1 # entry
        maze[way_out[0]][way_out[1]] = 1 #exit

        stack = [ [way_in[0], way_in[1]] ]

        while stack :
            """
            1. 어디로 갈지 정하는 함수 필요 - rand_direction 1~4
            2. 정해진 방향이 갈 수 있는 길인지 확인 하는 함수 - 
            3. 위치 이동시키는 함수 필요 - 
            4. stack 관리 필요
            """
            stack.pop()
        for i in range(1,5):
            print(self.check_make_way_possible(width, height, maze, [1, 1], i))


    """
    2. 미로 해석
        미로 배열을 받아서 해답인 길을 포함한 배열을 반환하도록
        정답 길을 2로 채운 후 반환
    """
    def solve_maze(self, maze):
        print("solve_maze")

    

if __name__ == "__main__" :
    test = maze_maker()
    test.make_maze(4,5)
