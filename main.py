import json
import random
from enum import Enum
from datetime import datetime
# 퀴즈 표시 방식을 나타내는 모드
# QUESTION_ONLY: 질문만 표시
# WITH_CHOICES : 질문 + 선택지
# WITH_ANSWER  : 질문 + 선택지 + 정답
# WITH_HINT    : 질문 + 선택지 + 힌트
# ALL          : 질문 + 선택지 + 정답 + 힌트
class ShowMode(Enum):
    QUESTION_ONLY = 1
    WITH_CHOICES = 2
    WITH_ANSWER = 3
    WITH_HINT = 4
    ALL = 5
# read_int 기능: 문자 공백제거, 빈 입력에 대응, 숫자아닌 입력에 대응, 숫자범위 벗어난 입력에 대응
# pre_msg : str 타입으로 사용자에게 어떤것을 입력해야할지 메세지를 표시한다
# value_min: int 타입으로 숫자범위 최소값
# value_max: int 타입으로 숫자범위 최대값
# return 값: int 타입으로 반환함
def read_int(pre_msg:str,value_min:int,value_max:int) -> int:
    # 올바른 정수가 들어올때 까지 반복
    while True:
        usr_str = input(pre_msg).strip() # strip으로 앞뒤 공백을 제거함
        if usr_str=="":
            print("입력이 비어 있어요. 다시입력 하세요")
            continue
        #02, 03과 같이 앞에 0을 붙이는 경우 int("02") -> 2로 처리하므로, 스트링 비교처리로 제외시키자
        if len(usr_str)>1 and usr_str.startswith("0"):
            print("숫자 앞에 0을 붙이지 말아주세요")
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
        usr_str = input(pre_msg).strip() # strip으로 앞뒤공벡제거
        if usr_str=="":
            print("입력이 비어 있어요, 다시입력 하세요")
            continue

        return usr_str # while문 수행멈추고 함수 호출 위치로 복귀 return 

"""
게임에서 퀴즈 1개를 표현하는 클래스
"""
from typing import Self
class Quiz:
    def __init__(self, question:str, choice_list:list, choice_count:int, answer:int, hint:str):
        if len(choice_list)!=choice_count:
            raise ValueError(f"문제선택 항목 리스트 와 항목 개수 불일치(list={len(choice_list)}, count={choice_count})")
        if len(choice_list)<2:
            raise ValueError(f"문제 선택항목은 최소 2개 이상이어야합니다 (현재 {len(choice_list)}개 입력됨)")
        if not isinstance(answer,int) or not (1<=answer<=len(choice_list)):
            raise ValueError(f"정답은 1~{len(choice_list)} 사이의 정수여야 합니다. (현재값 : {answer})")
        self.question=question      # 문제 질문
        self.choice_list = choice_list  # 보기 선택지 리스트
        self.choice_count = choice_count # 선택지 리스트의 개수를 정해주어 만약 state.json데이터를 임의로 깨뜨려도 검증가능함
        self.answer = answer        # 정답 번호 1~4
        self.hint = hint # 힌트 정보 문자열
    """
    show 함수: quiz_num 는 int형식으로 문제를 몇 번으로 표시할 것인지 정하는 숫자 이고 문제 내부적으로 
              mode에 따라 실제 문제(질문) 와 선택 지문이 선택적으로 표시된다.
    """
    def show(self, quiz_num:int, mode:ShowMode=ShowMode.WITH_CHOICES):
        print()
        print("-"*40)
        print(f"[문제{quiz_num} 번]",end=" ")
        print(self.question)
        print()
        if mode == ShowMode.QUESTION_ONLY:
            return
        for choice_num, choice_text in enumerate(self.choice_list,start=1):#start=1 index=0번 아이템을 1로 시작한다
            # choice_num 은 1,2,3,4 나오게 된다
            # choice_text는 실제 선택 문항이 나오게 된다
            print(f"{choice_num}. {choice_text}")

        if mode in (ShowMode.WITH_ANSWER, ShowMode.ALL):
            print(f"정답: {self.get_answer_msg()}")
        if mode in (ShowMode.WITH_HINT, ShowMode.ALL):
            print(f"힌트: {self.hint}")

    # choice_list에서 정답을 골라 표시한다
    def get_answer_msg(self)->str:
        return f"{self.answer}. {self.choice_list[self.answer-1]}"

    def check_answer(self,usr_answer) -> bool:
        return self.answer==usr_answer # 문제가 원래 갖고 있는 정답과 사용자가 입력한 정답이 같은지 체크한다

    # dictionary 데이터를 사용해서 class인스턴스 생성
    @classmethod #cls를 통하여 객체가 생성되지 않았을때 객체를 생성
    def from_dict(cls, data:dict)->Self: # 호출한 클래스와 항상 같은 타입을 반환한다는 사실이 코드에 반영되어 , 타입검사가 실제런타임 동작과 어긋나지 않도록 함
        return cls(data["question"],list(data["choice_list"]),data["choice_count"],data["answer"],data["hint"])
    
    # 클래스 객체 속성 값을 dictionary형태로 변환
    def to_dict(self):
        return {
            "question":self.question,
            "choice_list":list(self.choice_list), #일어나진 않지만 얕은 복사시 동일참조되는 문제 해결위해 list를 새로생성함
            "choice_count":self.choice_count,
            "answer":self.answer,
            "hint":self.hint,
        }

"""
 게임 전체를 관리하는 클래스 뼈대 만들기
"""
class QuizGame: # 상속받지않고
    def __init__(self): # 객체가 생성되는 순간 생성되는 변수, 객체 각각 별도공간 할당됨
        self.score_history:list[dict]=[]
        self.quiz_list:list[Quiz]=[] # 퀴즈를 리스트로 메모리에서 관리함
        self.best_score = None # 퀴즈 풀었을때 최고 점수, 퀴즈풀지않고 스코어 확인시 None이면 퀴즈를 풀라고 해야함, 0으로 초기화하면 풀지도않았는데 점수가 0 인것으로 오해됨
        self.load() # load함수 내부에서 정상적이면 파일 내용으로 채우고 파일이 문제가 있다면 기본값으로 재설정 합니다
        self.menu_list=[
        "퀴즈 풀기",
        "퀴즈 추가",
        "퀴즈 목록",
        "퀴즈 삭제",
        "점수 확인",
        "퀴즈 종료"]

    # state.json파일이없을때 사용할 기본 퀴즈 생성
    def default_quiz_list(self)->list[Quiz]:
        return [
            Quiz("다음 중 얕은 복사(shallow copy)를 수행하는 방법은?",
                ["copy.deepcopy(리스트)", "리스트[:]", 
                 "리스트2 = 리스트1 (대입 연산)", 
                 "json.dumps(리스트)"
                ], 4, 2, 
                "대입은 주소만 공유하고 deepcopy는 깊은 복사를 수행합니다. 원본 리스트의 시작부터 끝까지 범위를 지정해 새 리스트를 만드는 슬라이싱 문법을 찾아보세요"
                ),
            Quiz("""다음 코드의 출력 결과는?
                    def outer():
                        x = 10
                        def inner():
                            nonlocal x
                            x += 1
                            return x
                        return inner
                    f = outer()
                    print(f(), f())""",
                ["10 10", 
                 "11 12", 
                 "10 11", 
                 "11 11"
                ], 4, 2,
                "nonlocal x는 내부 함수가 호출될 때마다 외부 함수의 x 값을 유지하며 누적 변경합니다. 함수 f를 연속으로 두 번 호출했을 때 변화를 추적해 보세요."
                ),
            Quiz("다음 중 제너레이터(generator)를 만드는 방법이 아닌 것은?",
                ["yield를 사용하는 함수", 
                 "(x for x in range(5)) 형태의 표현식",
                 "[x for x in range(5)] 형태의 표현식", 
                 "__next__와 __iter__를 구현한 클래스"
                ], 4, 3,
                "제너레이터는 데이터를 한 번에 메모리에 올리지 않고 대기(Lazy) 상태로 둡니다. 대괄호[]를 사용하는 표현식은 대기하지 않고 메모리에 리스트 전체를 즉시 생성합니다."
                ),
            Quiz("GIL(Global Interpreter Lock)에 대한 설명으로 옳은 것은?",
                ["멀티프로세싱도 GIL 때문에 CPU 병렬 처리가 불가능하다",
                 "CPU-bound 작업에서 멀티스레딩의 성능 향상을 제한한다",
                 "GIL은 Python 3.10부터 완전히 제거되었다",
                 "I/O-bound 작업에서는 멀티스레딩 성능 향상을 전혀 얻을 수 없다"
                 ], 4, 2,
                 "GIL은 한 번에 하나의 스레드만 파이썬 바이트코드를 실행하도록 제한합니다. 따라서 여러 스레드가 동시에 연산을 수행해야 하는 CPU 중심(CPU-bound) 작업에서 병목 현상이 발생합니다."
                 ),
            Quiz("`is`와 `==`의 차이에 대한 설명으로 틀린 것은?",
                ["`is`는 객체의 메모리 주소(정체성)를 비교한다",
                "`==`는 객체의 값을 비교한다",
                "작은 정수(-5~256)는 캐싱되어 `is`로 비교해도 True가 나올 수 있다",
                "모든 문자열 리터럴은 항상 `is`로 비교했을 때 True가 보장된다"
                ], 4, 4,
                "파이썬은 실행 시점이나 최적화 방식(예: 긴 문자열, 동적 생성)에 따라 같은 문자열이라도 서로 다른 메모리 주소에 할당할 수 있습니다. 따라서 항상 주소 비교(is)가 참이 된다고 보장할 수는 없습니다."
                ),
        ]

    def show_menu(self):
        print()
        print("="*40)
        for idx,menu_str in enumerate(self.menu_list,start=1):
            print(f"{idx}. {menu_str}")
        print("=" * 40)
        print()

    # 저장된 퀴즈를 출제하고 정답체크 후 점수를 합산한다
    def play(self):
        if not self.quiz_list:
            print("퀴즈 목록이 없어요. 퀴즈를 추가해 주세요")
            return
        usr_wanted_quiz_count = read_int(pre_msg=f"몇 문제 풀까요? (1~{len(self.quiz_list)}): ",value_min=1,value_max=len(self.quiz_list))
        ok_cnt=0        
        shuffled_quiz_list = self.quiz_list[:] # list(self.quiz_list) 라고 하지않는 이유는 속도차이때문, slice가 더 빠르다고함
        random.shuffle(shuffled_quiz_list) # random하게 재배치된 결과가 shuffled_quiz_list에 반영되어짐
        shuffled_quiz_list = shuffled_quiz_list[:usr_wanted_quiz_count]# 섞은 퀴즈 목록의 처음부터 :usr_wanted_quiz_count까지 잘라서 새로운 리스트로 넘겨줌
        total_len = len(shuffled_quiz_list)
        for quiz_num, quiz in enumerate(shuffled_quiz_list,start=1):
            quiz.show(quiz_num)
            is_hint_used = read_int("힌트를 보시겠어요? (1:예, 2:아니오): ",1,2) == 1 # 1 -> True, 2 -> False
            if is_hint_used:
                print(f"힌트: {quiz.hint}")
            
            usr_answer = read_int("정답입력 :",1,len(quiz.choice_list))
            if quiz.check_answer(usr_answer):
                print("⭕️ 정답입니다.")
                ok_cnt = ok_cnt + (0.5 if is_hint_used else 1) # hint를 사용하면 ok_cnt + 0.5 절반점수만 인정
            else:
                print(f"❌ 오답입니다. (정답: {quiz.get_answer_msg()})")
        score = round((ok_cnt/total_len)*100) # 반올림((맞춘개수/전체문제)x100)
        print()
        print("="*40)
        print(f"결과: {total_len} 문제 중 {ok_cnt} 문제 맞춤! ({score} 점)")
        print("="*40)
        print()
        self.score_history.append({
            "datetime":datetime.now().isoformat(timespec="seconds"),
            "total_len":total_len,
            "score":score
        })
        self.save() # 최고점수 갱신 여부와 상관없이 기록은 항상 저장한다
        self.update_score(score)

    def add_quiz(self):
        # 문제 텍스트를 입력받는다
        question = read_str("문제를 입력하세요 :")
        # 선택지 개수를 입력받는다
        choice_count = read_int("선택지 개수입력(2~6):",2,6) #현재는 2~6개 까지 가변 선택지 문제를 등록할수있다
        # 선택지 텍스트를 입력받는다
        choice_list = []
        for i in range(1,choice_count+1):
            choice_str = read_str(f"{i}번 :")
            choice_list.append(choice_str)        
        # 정답 숫자를 입력받는다
        answer_num = read_int("정답 번호 입력: ",1,choice_count)

        # 정답에 대한 힌트 정보를 입력받는다
        hint_str = read_str("힌트를 입력하세요: ")

        # self.quiz_list 의 맨 뒷부분에 추가한다 append
        self.quiz_list.append(Quiz(question,choice_list,choice_count,answer_num,hint_str))
        # 전체 내용을 state.json에 저장한다
        self.save()
        print("\n퀴즈가 추가되었 습니다")

    def show_quiz_list(self,mode:ShowMode=ShowMode.WITH_HINT):
        # self.quiz_list 에 데이터가 존재하는지 체크한다
        if not self.quiz_list:
            print("\n등록된 퀴즈가 없습니다")
            return
        print(f"\n등록된 퀴즈 (총 {len(self.quiz_list)} 개)")
        print("-"*40)
        # self.quiz_list 를 순차적으로 표시한다 (정답/힌트 표시여부는 quiz.show 내부에서 mode로 처리)
        for quiz_num, quiz in enumerate(self.quiz_list,start=1):
            quiz.show(quiz_num,mode)
        print("-"*40)

    def show_score(self):
        # self.best_score 값이 None 이면 퀴즈를 풀지 않은것임
        if self.best_score == None:
            print("\n아직 퀴즈를 풀지 않았습니다. 퀴즈를 풀어야 점수확인이 가능합니다.")
            return
        print(f"\n최고점수: {self.best_score} 점")
        print(f"\n전체 게임 기록 (총 {len(self.score_history)} 회)")
        print("-"*40)
        for record in self.score_history:
            print(f"{record['datetime']} | {record['total_len']}문제 | {record['score']}점")
        print("-"*40)

    def update_score(self, new_score:int):
        # self.best_score가 None이면 new_score를 self.best_score에 저장
        # new_score와 self.best_score를 비교해서 self.best_score보다 크면 self.best_score에 저장
        if self.best_score==None or self.best_score < new_score:# 비교순서 바뀌면 안됨
            self.best_score = new_score
            print(f"새로운 최고점수 :{new_score}점 입니다")
            self.save()

    def save(self):
        #메모리에 있는 내용을 파일로 저장
        w_data={
            "quiz_list":[ quiz.to_dict() for quiz in self.quiz_list],
            "best_score":self.best_score,
            "score_history":self.score_history,
        }
        #w_data를 state.json으로 저장하는데 utf-8 인코딩형태로 저장한다
        try:
            with open(file="state.json",mode="w",encoding="utf-8") as file:
                #ensure_ascii: 한글 같은 비 ascii문자를 유니코드 이스케이프문자(\uXXXX)로 바꾸지 말라는 의미
                json.dump(obj=w_data,fp=file,ensure_ascii=False)
        except OSError:
            print("파일 저장 중 요류발생")

    def load(self):
        # state.json 파일을 읽어서 self.quiz_list 와 self.best_score 값을 복원
        try:
            with open(file="state.json", mode="r", encoding="utf-8") as file:
                r_data = file.read().strip()
                
                if not r_data:
                    raise ValueError("파일이 비어있습니다.")
                
                # 파일 객체가 아닌 '문자열'을 파싱하므로 json.loads() 사용
                data = json.loads(r_data)
                
            if not isinstance(data, dict):
                raise ValueError("데이터가 dictionary 형태가 아닙니다.")
                
            if "quiz_list" not in data or not data["quiz_list"]:
                raise ValueError("퀴즈 데이터가 유효하지 않습니다.")
                
            # 데이터 복원 진행
            self.quiz_list = [Quiz.from_dict(quiz_dict) for quiz_dict in data["quiz_list"]]
            
            # 안전하게 get() 메서드를 사용하여 KeyError 방지 및 기본값 처리
            self.best_score = data.get("best_score", None)
            self.score_history = data.get("score_history", [])

        except FileNotFoundError:
            print("저장된 파일이 없어 기본 데이터로 시작합니다.")
            self._init_default_data()

        except (ValueError, json.JSONDecodeError, KeyError, TypeError) as e:
            # 데이터 포맷 변환 실패, 키 누락 등 파일 손상 케이스 처리
            print(f"파일 손상 또는 데이터 오류({e})로 인해 기본 데이터로 초기화합니다.")
            self._init_default_data()

    def _init_default_data(self):
        # 중복되는 초기화 및 저장 로직을 별도 메서드로 분리
        self.quiz_list = self.default_quiz_list()
        self.best_score = None
        self.save()

    def delete_quiz(self):
        if not self.quiz_list:
            print("\n등록된 퀴즈가 없습니다")
            return
        self.show_quiz_list(ShowMode.QUESTION_ONLY) # 퀴즈의 문제만 출력됨, 선택지 출력안됨
        del_quiz_num = read_int("삭제하고자 하는 문제 번호 입력 : ",1,len(self.quiz_list))
        self.quiz_list.pop(del_quiz_num-1)
        self.save()
        print("\n퀴즈가 삭제되었습니다")

    def run(self):
        try:
            while True:
                self.show_menu()
                usr_sel = read_int("숫자선택: ",1,len(self.menu_list))
                match usr_sel:
                    case 1:
                        self.play()
                    case 2:
                        self.add_quiz()
                    case 3:
                        self.show_quiz_list()
                    case 4:
                        self.delete_quiz()
                    case 5:
                        self.show_score()
                    case 6:
                        print("게임을 종료합니다.")
                        break
                    case _: # read_int에서 걸렀기 때문에 여기 오지 않지만 안전장치로 추가
                        print("\n잘못된 입력입니다.")
        except (KeyboardInterrupt,EOFError):
            print("\n프로그램을 강제 종료합니다.")

if __name__ == "__main__":
    game = QuizGame()
    game.run()