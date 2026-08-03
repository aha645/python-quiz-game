
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
게임에서 퀴즈 1개를 표현하는 클래스
"""
from typing import Self
class Quiz:
    def __init__(self, question:str, choice_list:list, answer:int):
        self.question=question      # 문제 질문
        self.choice_list = choice_list  # 보기 선택지 리스트(4개 리스트)
        self.answer = answer        # 정답 번호 1~4
    """
    show 함수: quiz_num 는 int형식으로 문제를 몇 번으로 표시할 것인지 정하는 숫자 이고 문제 내부적으로 
              실제 문제(질문) 와 4지 선택 지문이 자동 표시된다.
    """
    def show(self, quiz_num:int):
        print("-"*40)
        print(f"[문제{quiz_num} 번]",end=" ")
        print(self.question)
        print()
        for choice_num, choice_text in enumerate(self.choice_list,start=1):#start=1 index=0번 아이템을 1로 시작한다
            # choice_num 은 1,2,3,4 나오게 된다
            # choice_text는 실제 선택 문항이 나오게 된다
            print(f"{choice_num}. {choice_text}")
        print()

    def check_answer(self,usr_answer) -> bool:
        return self.answer==usr_answer # 문제가 원래 갖고 있는 정답과 사용자가 입력한 정답이 같은지 체크한다

    # dictionary 데이터를 사용해서 class인스턴스 생성
    @classmethod #cls를 통하여 객체가 생성되지 않았을때 객체를 생성
    def from_dict(cls, data:dict)->Self: # 호출한 클래스와 항상 같은 타입을 반환한다는 사실이 코드에 반영되어 , 타입검사가 실제런타임 동작과 어긋나지 않도록 함
        return cls(data["question"],data["choice_list"],data["answer"])
    
    # 클래스 객체 속성 값을 dictionary형태로 변환
    def to_dict(self):
        return {
            "question":self.question,
            "choice_list":self.choice_list,
            "answer":self.answer
        }

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
        try:
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
                    case _: # read_int에서 걸렀기 때문에 여기 오지 않지만 안전장치로 추가
                        print("잘못된 입력입니다.")
        except (KeyboardInterrupt,EOFError):
            print("프로그램을 강제 종료합니다.")

if __name__ == "__main__":
    game = QuizGame()
    game.run()