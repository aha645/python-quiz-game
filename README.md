# 프로젝트 개요

터미널에서 실행하는 **Python 퀴즈 게임**입니다. `main.py` 하나로 동작합니다.

퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 퀴즈 삭제, 점수 확인(전체 게임 기록 포함), 게임 종료 기능을 메뉴 방식으로 제공하며, 진행한 퀴즈 데이터·최고 점수·게임 기록(score_history)은 `state.json` 파일에 저장되어 프로그램을 재실행해도 유지됩니다.

# 퀴즈 주제 선정 이유

기본 내장 퀴즈는 **Python 문법**을 주제로 선정했습니다. 프로젝트 자체가 Python으로 작성되었기 때문에, 개발 과정에서 학습·정리한 Python 언어 개념을 퀴즈로 만들어 스스로 복습하고 다른 학습자에게도 도움이 되도록 하기 위함입니다.

# 실행 방법

Python 3.11 이상이 설치되어 있어야 합니다 (typing 모듈의 `Self` 타입 힌트 등 최신 문법 사용).

```bash
python3 main.py
```

실행 후 화면에 표시되는 메뉴 번호(1~6)를 입력해 원하는 기능을 선택합니다. 메뉴로 돌아올 때마다 ANSI 이스케이프 코드로 화면을 지워 항상 깔끔한 화면에서 메뉴를 확인할 수 있습니다.
# 1.퀴즈 풀기 실행 예제
```
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 퀴즈 종료
========================================

숫자선택: 1
몇 문제 풀까요? (1~5): 3

[문제1 번] 다음 중 제너레이터(generator)를 만드는 방법이 아닌 것은?

1. yield를 사용하는 함수
2. (x for x in range(5)) 형태의 표현식
3. [x for x in range(5)] 형태의 표현식
4. __next__와 __iter__를 구현한 클래스

힌트를 보시겠어요? (1:예, 2:아니오): 2

정답입력 :3
⭕️ 정답입니다.
========================================
결과: 3 문제 중 1.5 문제 맞춤! (50 점)
========================================

새로운 최고점수 :50점 입니다

계속하려면 Enter를 눌러주세요...
```

# 기능 목록

| 메뉴 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 몇 문제를 풀지 입력받은 뒤(1~등록된 문제 수), 전체 퀴즈를 무작위로 섞어 그중 원하는 개수만큼 출제합니다. 문제마다 힌트를 볼지 선택할 수 있으며, 힌트를 사용하면 정답을 맞혀도 0.5점만 인정됩니다. 채점 결과를 백분율 점수로 계산해 보여주고, 매 판 결과를 게임 기록(`score_history`)에 추가·저장하며, 기존 최고 점수보다 높으면 최고 점수도 함께 갱신·저장합니다. |
| 2 | 퀴즈 추가 | 문제 내용, 선택지 개수(2~6개), 선택지 내용, 정답 번호, 힌트를 입력받아 새 퀴즈를 목록에 추가하고 즉시 `state.json`에 저장합니다. |
| 3 | 퀴즈 목록 | 등록된 모든 퀴즈를 문제·선택지·힌트와 함께 출력합니다. |
| 4 | 퀴즈 삭제 | 등록된 퀴즈의 문제만 나열해서 보여준 뒤, 삭제할 문제 번호를 입력받아 목록에서 제거하고 저장합니다. |
| 5 | 점수 확인 | 저장된 최고 점수와 지금까지의 전체 게임 기록(플레이 일시, 푼 문제 수, 점수)을 함께 보여줍니다. 아직 퀴즈를 한 번도 풀지 않았다면 안내 메시지를 표시합니다. |
| 6 | 퀴즈 종료 | 프로그램을 종료합니다. |

공통 입력 검증 기능:
- **빈 입력 방지**: 아무것도 입력하지 않으면 다시 입력을 요청합니다.
- **숫자 형식 검증**: 숫자가 아닌 값을 입력하면 오류 메시지를 표시하고 재입력을 요청합니다.
- **범위 검증**: 지정된 최소~최대 범위를 벗어난 숫자는 거부합니다.
- **0으로 시작하는 숫자 차단**: `02`처럼 앞에 0이 붙은 입력은 거부합니다(`int("02")`가 `2`로 처리되어 발생할 수 있는 혼란 방지).
- `Ctrl+C`, `Ctrl+D` 입력 시 프로그램을 안전하게 종료합니다.

# 파일 구조

```
python-quiz-game/
├── main.py        # 게임 전체 로직 (퀴즈/게임 클래스, 입력 검증, 저장/불러오기, 실행 진입점)
├── state.json      # 퀴즈 목록, 최고 점수, 게임 기록을 저장하는 데이터 파일 (최초 실행 시 자동 생성)
├── README.md       # 프로젝트 설명 문서
├── .gitignore      # __pycache__, *.pyc, .vscode/, .idea/ 등 버전관리 제외 목록
└── .vscode/        # VS Code 편집기 설정
```

`main.py`의 주요 구성 요소:
- `read_int()`, `read_str()`: 사용자 입력을 검증하며 받는 공통 함수
- `ShowMode`: 퀴즈를 어떤 정보까지 표시할지 정하는 열거형(`QUESTION_ONLY`, `WITH_CHOICES`, `WITH_ANSWER`, `WITH_HINT`, `ALL`). 퀴즈 목록·삭제 화면 등 상황에 따라 표시 범위를 다르게 제어하는 데 쓰입니다.
- `Quiz`: 문제 1개(질문, 선택지 2~6개, 선택지 개수, 정답 번호, 힌트)를 표현하는 클래스. `show()`가 `ShowMode`에 따라 출력 내용을 다르게 보여주고, `to_dict()` / `from_dict()`로 JSON과 상호 변환합니다.
- `QuizGame`: 퀴즈 목록·최고 점수·게임 기록(`score_history`)을 관리하며, 메뉴 표시·퀴즈 풀기/추가/목록/삭제·점수 확인·저장·불러오기를 담당하는 메인 클래스

# 데이터 파일 설명

`state.json`은 프로그램 실행 중 생성/갱신되는 데이터 파일로, UTF-8 인코딩의 JSON 형식입니다.
 load()함수에서 정상 파일이면 로드, 아니면 기본값으로 대체, save()함수는 play(), add_quiz(), update_score() 에서 저장을수행합니다.
```json
{
  "quiz_list": [
    {
      "question": "다음 중 얕은 복사(shallow copy)를 수행하는 방법은?",
      "choice_list": ["copy.deepcopy(리스트)", "리스트[:]", "리스트2 = 리스트1 (대입 연산)", "json.dumps(리스트)"],
      "choice_count": 4,
      "answer": 2,
      "hint": "대입은 주소만 공유하고 deepcopy는 깊은 복사를 수행합니다. 슬라이싱 문법을 찾아보세요"
    }
  ],
  "best_score": 80,
  "score_history": [
    {
      "datetime": "2026-08-04 20:05:12",
      "total_len": 5,
      "score": 80
    }
  ]
}
```

- `quiz_list`: 등록된 퀴즈 배열. 각 항목은 `question`(문제), `choice_list`(선택지 배열), `choice_count`(선택지 배열의 개수), `answer`(정답 번호, 1~`choice_count`), `hint`(정답 힌트)로 구성됩니다.
- `best_score`: 지금까지 기록한 최고 점수(0~100). 퀴즈를 한 번도 풀지 않았다면 `null`입니다.
- `score_history`: 퀴즈를 풀 때마다 한 판씩 쌓이는 게임 기록 배열입니다. 각 항목은 `datetime`(플레이 일시, `YYYY-MM-DD HH:MM:SS` 형식), `total_len`(그 판에서 푼 문제 수), `score`(그 판의 점수)로 구성되며, 최고 점수 갱신 여부와 상관없이 매 판마다 저장됩니다.

파일이 없거나(`FileNotFoundError`), 비어 있거나, JSON 형식이 손상되었거나, 필수 데이터(`quiz_list`)가 유효하지 않은 경우에는 자동으로 기본 제공 퀴즈 5문항으로 초기화한 뒤 `state.json`을 새로 저장합니다.

# 대용량 데이터 시 성능/메모리 고려사항

`state.json`의 퀴즈 개수가 매우 커지는 상황(예: 1,000만 문항 이상)을 가정하면 다음과 같은 문제가 발생할 수 있습니다.

- **시작 시 전체 로딩**: `load()`가 파일 전체를 문자열로 읽고 `json.loads()`로 한 번에 파싱한 뒤, 모든 문항을 `Quiz` 객체로 즉시 생성하므로 메모리 사용량과 시작 시간이 문항 수에 비례해 커집니다.
- **매 저장마다 전체 재작성**: `save()`는 퀴즈 추가/삭제/점수 갱신 시마다 `quiz_list` 전체를 다시 직렬화해 파일 전체를 덮어쓰므로, 문항 하나만 바뀌어도 데이터 개수만큼 탐색하는 비용이 듭니다.
- **`play()`의 셔플 비용**: `random.shuffle()`로 전체 목록을 섞은 뒤 원하는 개수만큼 슬라이스하므로, 소수의 문제만 출제해도 전체 목록을 섞는 비용이 듭니다.
- **목록 출력**: `show_quiz_list()` / `delete_quiz()`가 전체 목록을 한 번에 출력해 터미널 flood가 발생할 수 있습니다.

이 중 손쉽게 적용 가능한 개선 두 가지를 실제로 적용했습니다.

**1) `Quiz` 클래스에 `__slots__` 적용 — 인스턴스 메모리 절감**

```python
class Quiz:
    __slots__ = ("question", "choice_list", "choice_count", "answer", "hint")
```

일반적인 파이썬 객체는 인스턴스마다 속성을 저장하기 위한 `__dict__`(해시테이블 기반)를 별도로 생성하는데, 여유 버킷 공간과 해시 구조 때문에 속성이 몇 개 안 되어도 인스턴스당 오버헤드가 상당히 큽니다. `__slots__`를 선언하면 인스턴스별 `__dict__` 생성을 생략하고, 선언된 속성 개수만큼의 고정 크기 슬롯(배열)만 인스턴스에 붙기 때문에 인스턴스 1개당 메모리 사용량이 줄어들고, 속성 접근도 해시 조회 대신 고정 오프셋 접근이라 약간 더 빨라집니다. 문항 수가 수백만~수천만 개 규모가 되면 이 차이가 전체 메모리 사용량에서 큰 비중을 차지하게 됩니다. 단, `__init__`에서 선언하지 않은 속성을 인스턴스에 동적으로 추가할 수 없다는 제약이 생깁니다.

**2) `random.shuffle()` + 슬라이스 대신 `random.sample()` 사용 — 불필요한 전체 셔플 제거**

```python
shuffled_quiz_list = random.sample(self.quiz_list, usr_wanted_quiz_count)
```

기존 방식은 `self.quiz_list[:]`로 전체 목록을 복사한 뒤 `random.shuffle()`로 전체를 섞고, 그중 앞부분만 슬라이스해서 사용했습니다. 이 경우 5문제만 출제하더라도 1,000만 개 전체를 복사·셔플하는 비용이 그대로 발생합니다. `random.sample(population, k)`는 원본 리스트를 복사하거나 전체를 섞지 않고 필요한 `k`개만 무작위로 추출하므로, 문항 수가 아무리 많아도 뽑으려는 문제 수(`k`)에 비례하는 비용만 듭니다.


# 커밋 단위/메세지 규칙
```
 브랜치명 작업내용
```
```bash
commit f634efabeebc9b608bf290ffca8aec39868dd4f0
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 20:19:05 2026 +0900

    feature/add-quiz add_quiz()기능 구현,show_quiz_list()기능구현
```

# 브랜치 목적 및 병합의 이유
### 브랜치를 하는 목적
- 원본보호 : 메인 코드에 직접 손대지 않아 에러발생을 방지함
- 독립개발 : 다른 작업에 방해받지 않고 오직 한 가지 기능이나 버그를 수정하고자 할때 사용
- 동시작업 : 여러 사함이 동시에 서로 다른 기능을 각자 편하게 개발
### 병합을 하는 이유
- 기능통합 : 브랜치에서 검증되고 완성된 코드를 메인 프로젝트로 합치기 위해
- 최신화반영: 각자 따로 개발한 결과물을 하나로 합쳐서 최종 서비스나 프로그램 형태로 완성


# 원격 저장소 및 10개 이상의 커밋 증빙 로그
```bash
thinkover20221658@c4r6s1 python-quiz-game % git log 
commit 6e0da29361c1a1a5150f1131b5b0f8b6d4f504e9 (HEAD -> main, origin/main, origin/HEAD)
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 21:04:39 2026 +0900

    메모리용량 적게차지하도록 __slots__ 항목 추가, 대용량 데이터 에서 shuffle 사용시 문제점 보완하는 방법으로 random.sample 으로 변경

commit c18deb4a524614c95bd43ada2716f30273162ad1
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 20:27:27 2026 +0900

    score_history 저장시 시간정보에 T들어가는 문제 해결

commit d8f46260b0666e934605fdcab67c2edcc7ea9c83
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 20:12:05 2026 +0900

    메뉴표시시 ansi escape코드로 화면 지우는 기능추가, 점수기록히스토리에서 날짜 와 시간 사이에 T자 제거, Quiz.show()표시하는 부분에 한줄 띄도록 수정

commit f5fd0de02a258d52130cff6fba082f491a6e81a0
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 19:42:00 2026 +0900

    보너스5: load()함수에 score_history복원, play()에서 score_history 만들고 save()호출해서 최고점수 못넘긴게임도 score_history저장, show_score()함수에서 게임기록 표시하도록 기능 추가

commit 7761e2464b38a7e56ceb13368b5ec56700e4dc82
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 19:13:04 2026 +0900

    보너스4: 퀴즈삭제기능구현, 퀴즈정보보여주는 기능을 Enum을 사용하여 mode에따라 다르게출력되는 show()함수 구현, delete_quiz()함수 구현

commit 5bfc53c92705cd4c7b147ce4ccc634ea1b21b5e1
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 17:40:34 2026 +0900

    보너스3번: 힌트 기능 구현

commit ed4c39313c4a675b18da585bb3f887d54700d945
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 17:08:26 2026 +0900

    보너스2번: 퀴즈풀기시 몇 문제를 풀지 선택기능 play()함수에 추가

commit 659da20f00a7fd54534bc0f73749dd0a01f7680e
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 16:54:53 2026 +0900

    보너스1번: 퀴즈풀기 시 문제순서를 랜덤하게 섞는 기능 구현

commit a850d1ce2a3ec0fc6bd600e3f35d7eb772a6c57d
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 16:20:33 2026 +0900

    ..

commit b074afbb1f8c4d9f65d4955ba3591b64e7f2cfc0
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 16:01:34 2026 +0900

    .gitignore에 state.json추가

commit ede58d6a7e4c4310e3cdaf2402f794a6b9380e4b
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 15:58:15 2026 +0900

    README.md state.json 내용수정

commit 32a03b0da4481721aedb60deb9e9236d7fc87ed0
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 15:53:41 2026 +0900

    README.md내용 수정

commit 5e88ed37e2461fc7a2faa8e0cdc0fa353b1c5fba
Merge: 7a031d7 f3ba421
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 15:50:38 2026 +0900

    Merge branch 'feature/dynamic-mcq' of https://github.com/aha645/python-quiz-game
    원격지 feature/dynamic-mcq 를 로컬 main브랜치로 합친다 --no-ff옵션적용함

commit f3ba42181d8be999704686f8b6563c574d99cbf7 (origin/feature/dynamic-mcq)
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 15:40:55 2026 +0900

    feature/dynamic-mcq Quiz생성할때 선택문항 최소2개에서 6개사이로 가변입력 가능하도록 수정함 __init__에는 데이터 깨지는 오류관련 기능추가, play함수는 정답입력시 범위를 선택지 개수크기로 하도록 수정, add_quiz함수는 선택지 개수를 추가로 입력받도록 하여 퀴즈를 생성하도록 수정함

commit 7a031d782fc5ee74d50585ca341ee1ad5f5d6f16
Merge: 27c8aee 584f5ac
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 13:40:54 2026 +0900

    Merge branch 'feature/save-load'
    feature/save-load브랜치를 main브랜치로 합침 --no-ff 옵션사용함

commit 584f5acdf5bb386a3c5766164e44f9953eef58fd
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 13:36:33 2026 +0900

    feature/save-load 브랜치에 save(), load(),_init_default_data()함수 구현 및 __init__()함수 내용 수정

commit 27c8aee776c64b09262b24fc4e81ba499b0399bb
Merge: 11d315f 754cd93
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 12:17:34 2026 +0900

    Merge branch 'feature/score'
    feature/score를 main 브랜치로 합치는작업수행

commit 754cd93bc9a42e657e52c98be0b7516886485923
Author: aha645 <likylove@naver.com>
Date:   Tue Aug 4 12:16:49 2026 +0900

    feature/score read_int()에서 02 와 같은 숫자앞에 0붙이는 버그수정, update_score(), show_score()함수 기능 구현

commit 11d315fd0d5fbc4e340c0ee2e22c33ed0d92cbfe
Merge: f6589e2 f634efa
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 20:20:11 2026 +0900

    Merge branch 'feature/add-quiz'

commit f634efabeebc9b608bf290ffca8aec39868dd4f0
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 20:19:05 2026 +0900

    feature/add-quiz add_quiz()기능 구현,show_quiz_list()기능구현

commit f6589e28c47d88e07e11340a90384d28a6d969a1
Merge: eea4601 d0c7cc0
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 19:29:18 2026 +0900

    Merge branch 'feature/play-quiz'

commit d0c7cc0d45043a1e3475640a5581ce23b5f93658
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 19:05:55 2026 +0900

    Feature/play-quiz 퀴즈풀기 기능구현

commit eea4601dba1ddd9e808d4b40a7e224bb96b46560
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 17:58:19 2026 +0900

    기본퀴즈데이터5문제 추가(주제:python)

commit 79ebc9adbf80b0035032a6ea5cd9dd6eca646421
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 17:45:17 2026 +0900

    Quiz 클래스 추가 및 KeyboardInterrupt 와 EOFError일때 프로그램 강제종료 기능 추가

commit 48d268ef782a158f1452ad1dbc690f665197aed6
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 16:01:33 2026 +0900

    종료문구수정

commit e1515ef36a7c15067bbb4c7fecfa536d1527d4af
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 15:59:37 2026 +0900

    Feature: 메뉴출력, read_int, read_str,게임종료기능 구현

commit 797640a038f58137a4e19143180fc4200c50539b
Author: aha645 <likylove@naver.com>
Date:   Mon Aug 3 14:50:05 2026 +0900

    프로젝트초기설정(.gitignore,README.md뼈대)
```

# 브랜치 생성 및 병합기록(git log, merge commit) 증빙 로그
```bash
thinkover20221658@c4r6s1 python-quiz-game % git log --graph --oneline      
* 6e0da29 (HEAD -> main, origin/main, origin/HEAD) 메모리용량 적게차지하도록 __slots__ 항목 추가, 대용량 데이터 에서 shuffle 사용시 문제점 보완하는 방법으로 random.sample 으로 변경
* c18deb4 score_history 저장시 시간정보에 T들어가는 문제 해결
* d8f4626 메뉴표시시 ansi escape코드로 화면 지우는 기능추가, 점수기록히스토리에서 날짜 와 시간 사이에 T자 제거, Quiz.show()표시하는 부분에 한줄 띄도록 수정
* f5fd0de 보너스5: load()함수에 score_history복원, play()에서 score_history 만들고 save()호출해서 최고점수 못넘긴게임도 score_history저장, show_score()함수에서 게임
기록 표시하도록 기능 추가
* 7761e24 보너스4: 퀴즈삭제기능구현, 퀴즈정보보여주는 기능을 Enum을 사용하여 mode에따라 다르게출력되는 show()함수 구현, delete_quiz()함수 구현
* 5bfc53c 보너스3번: 힌트 기능 구현
* ed4c393 보너스2번: 퀴즈풀기시 몇 문제를 풀지 선택기능 play()함수에 추가
* 659da20 보너스1번: 퀴즈풀기 시 문제순서를 랜덤하게 섞는 기능 구현
* a850d1c ..
* b074afb .gitignore에 state.json추가
* ede58d6 README.md state.json 내용수정
* 32a03b0 README.md내용 수정
*   5e88ed3 Merge branch 'feature/dynamic-mcq' of https://github.com/aha645/python-quiz-game 원격지 feature/dynamic-mcq 를 로컬 main브랜치로 합친다 --no-ff옵션적용함
|\  
| * f3ba421 (origin/feature/dynamic-mcq) feature/dynamic-mcq Quiz생성할때 선택문항 최소2개에서 6개사이로 가변입력 가능하도록 수정함 __init__에는 데이터 깨지는 오류관련 기능추가, play함수는 정답입력시 범위를 선택지 개수크기로 하도록 수정, add_quiz함수는 선택지 개수를 추가로 입력받도록 하여 퀴즈를 생성하도록 수정함
|/  
*   7a031d7 Merge branch 'feature/save-load' feature/save-load브랜치를 main브랜치로 합침 --no-ff 옵션사용함
|\  
| * 584f5ac feature/save-load 브랜치에 save(), load(),_init_default_data()함수 구현 및 __init__()함수 내용 수정
|/  
*   27c8aee Merge branch 'feature/score' feature/score를 main 브랜치로 합치는작업수행
|\  
| * 754cd93 feature/score read_int()에서 02 와 같은 숫자앞에 0붙이는 버그수정, update_score(), show_score()함수 기능 구현
|/  
*   11d315f Merge branch 'feature/add-quiz'
|\  
| * f634efa feature/add-quiz add_quiz()기능 구현,show_quiz_list()기능구현
|/  
*   f6589e2 Merge branch 'feature/play-quiz'
|\  
| * d0c7cc0 Feature/play-quiz 퀴즈풀기 기능구현
|/  
* eea4601 기본퀴즈데이터5문제 추가(주제:python)
* 79ebc9a Quiz 클래스 추가 및 KeyboardInterrupt 와 EOFError일때 프로그램 강제종료 기능 추가
* 48d268e 종료문구수정
* e1515ef Feature: 메뉴출력, read_int, read_str,게임종료기능 구현
* 797640a 프로젝트초기설정(.gitignore,README.md뼈대)
```

# git clone/pull 실습 증빙 로그
```bash
thinkover20221658@c4r6s1 python-quiz-game % git reflog
6e0da29 (HEAD -> main, origin/main, origin/HEAD) HEAD@{0}: pull origin main: Fast-forward
d8f4626 HEAD@{1}: pull origin main: Fast-forward
a850d1c HEAD@{2}: pull origin main: Fast-forward
b074afb HEAD@{3}: clone: from https://github.com/aha645/python-quiz-game.git
```