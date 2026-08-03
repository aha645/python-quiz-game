
# read_int 기능: 문자 공백제거, 빈 입력에 대응, 숫자아닌 입력에 대응, 숫자범위 벗어난 입력에 대응
# pre_msg : str 타입으로 사용자에게 어떤것을 입력해야할지 메세지를 표시한다
# value_min: int 타입으로 숫자범위 최소값
# value_max: int 타입으로 숫자범위 최대값
# return 값: int 타입으로 반환함
def read_int(pre_msg:str,value_min:int,value_max:int) -> int:
    # 올바른 정수가 들어올때 까지 반복
    while True:
        usr_str = input().strip() # strip으로 앞뒤 공백을 제거함
        if usr_str=="":
            print("입력이 비어 있어요. 다시입력 하세요")
            continue

        try:
            usr_val = int(usr_str) #문자열 usr_str을 int()넣었을때 발생할 수 있는 예되는 오직 ValueError
        except ValueError:
            print("잘못된 값을 입력했어요. 숫자형식을 입력하세요")
            continue

        if usr_val < value_min or usr_val > value_max:
            print(f"잘못된 숫자를 입력했어요. {value_min}~{value_max} 사이의 숫자를 입력하세요")
            continue

        return usr_val # while문 수행멈추고 함수 호출 위치로 복귀 return

"""
read_str 기능: 앞뒤 공백제거 및 빈 문자 제거
"""
def read_str(pre_msg:str)->str:
    # 빈 입력이 들어오면 다시처리
    while True:
        usr_str = input().strip() # strip으로 앞뒤공벡제거
        if usr_str=="":
            print("입력이 비어 있어요, 다시입력 하세요")
            continue

        return usr_str # while문 수행멈추고 함수 호출 위치로 복귀 return 

 """
 게임 전체를 관리하는 클래스 뼈대 만들기
 """
class QuizGame: # 상속받지않고
    def __init__(self): # 객체가 생성되는 순간 생성되는 변수, 객체 각각 별도공간 할당됨
        self.quiz_list=[] # 퀴즈를 리스트로 메모리에서 관리함
        self.best_score = 0 # 퀴즈 풀었을때 최고 점수

    def show_menu(self):
        print()
        print("="*40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def run(self):
        while True:
            self.show_menu()
            usr_sel = read_int("숫자선택: ",1,5)
            match usr_sel:
                case 1:
                    print("퀴즈 풀기 시작")
                case 2:
                    print("퀴즈 추가 시작")
                case 3:
                    print("퀴즈 목록 시작")
                case 4:
                    print("퀴즈 점수 확인 시작")
                case 5:
                    print("게임을 종료합니다.")
                    break

if __name__ == "__main__":
    game = QuizGame()
    game.run()