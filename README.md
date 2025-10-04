# Python for Living 🐍

> 파이썬으로 먹고사는 개발자를 위한 실전 중급 스터디

## 이런 분들을 위한 스터디입니다

### Pain - 당신의 고민
- 파이썬 할 줄 아는데, 엔지니어 역량을 기르기 위해 무엇을 해야 하는지 모르겠다
- 인공지능하고 싶은데, 솔직히 Python에 대한 이해도가 낮다
- 다른 언어는 잘하는데, 파이썬 생태계에 대한 이해도가 낮다

### Agitation - 이대로 괜찮을까요?
- 파이썬 할 줄 안다고 이력서에 쓰고 질문 공세받고 면접 떨어짐
- 취업해도, 이런 것도 모르냐고 사수한테 혼남
- 이러나 저러나 우울함

### Solution - 우리의 해결책
- **프로덕션 레벨 파이썬**: 단순 문법이 아닌 실무에서 쓰이는 중급, 고급 기능들
- **체계적인 커리큘럼**: 패키징, 로깅, 스레딩, Asyncio, 타이핑, 테스트 등 순서대로 학습
- **실습 중심 학습**: 이론만이 아닌 직접 코드 작성하고 피드백 받기

## 얻어갈 수 있는 것들

- **이력서에 쓸 수 있는 프로젝트**: 제대로 된 패키지 구조와 문서화
- **오픈소스 기여 준비**: 파이썬 생태계 이해하고 컨트리뷰션 시작점
- **중급 개발자의 영역**: 로깅, 에러 처리, 비동기 처리, 웹 서버 이해
- **서드파티 라이브러리 이해**: ruff, pytest, pyright, pydantic, uv

## 스터디 진행 방식

### 일정
- **총 기간**: 10주
- **완주 기준**: 7개 이상의 세션에서 승인(approve) 받기

### 주간 일정
```
월요일: Issue 오픈 (해당 주차 주제 공개)
화~금: 개인 학습 및 PR 작성
금요일: PR 제출 마감
주말: 코드 리뷰 진행
세미나: 최종 합의된 내용 기반 토론 및 발표
```

### 진행 프로세스

1. **학습 및 PR 작성**
   - 매주 월요일 오픈되는 Issue를 확인
   - 주제에 대해 학습하고 자신만의 문서 작성
   - 금요일까지 PR 제출

2. **코드 리뷰**
   - 스터디 관리자 및 동료들의 리뷰 진행
   - 최소 3개의 승인(approve) 필요 (관리자 포함)
   - GitHub 코멘트로 피드백 주고받기

3. **최종 문서 작성**
   - 모든 스터디원의 PR을 기반으로 합의
   - `chapter{N}/{topic}.md` 형식으로 최종 문서 작성
   - 세미나에서 발표 자료로 활용

4. **세미나 발표**
   - 최종 합의된 문서를 바탕으로 토론
   - 20분 내외 발표 및 질의응답

## 커리큘럼

### Session 1: 파이썬답게 코딩하기 (Pythonic Code)
- 컴프리헨션 활용법 (리스트, 딕셔너리, 셋)
- 언패킹과 제너레이터
- 매직 메서드 (`__str__`, `__repr__`, `__eq__` 등)
- 데코레이터 기초와 활용

### Session 2: 타입 시스템 (Type System)
- 타입 힌팅 기초 (typing 모듈)
- 제네릭과 타입 변수
- 프로토콜과 덕 타이핑
- mypy, pyright 툴 사용법

### Session 2-1: 데이터 검증과 직렬화 (Data Validation)
- Pydantic 모델과 검증
- 스키마 정의와 변환
- JSON, MessagePack, Protocol Buffers
- 데이터 클래스와 attrs

### Session 3: 패키징과 의존성 관리 (Packaging)
- 프로젝트 구조 설계
- pyproject.toml 설정
- Poetry vs pip vs uv 비교
- 가상환경 관리와 배포

### Session 4: 테스팅 (Testing)
- pytest 기초와 fixture
- 모킹과 패칭
- 테스트 커버리지
- TDD 실습

### Session 5: 로깅과 에러 처리 (Logging & Error Handling)
- logging 모듈 활용
- 로그 레벨과 핸들러 설정
- 커스텀 예외 클래스
- 에러 추적과 디버깅

### Session 6: 동시성 프로그래밍 (Concurrency)
- 스레딩과 GIL 이해
- multiprocessing 활용
- 동기화 객체 (Lock, Queue)
- 성능 비교와 선택 기준

### Session 7: 비동기 프로그래밍 (Asyncio)
- async/await 문법
- 이벤트 루프와 태스크
- aiohttp를 활용한 비동기 HTTP
- 동시성 vs 비동기 비교

### Session 8: 웹 서버 인터페이스 (WSGI & ASGI)
- WSGI 스펙과 작동 원리
- 간단한 WSGI 애플리케이션 작성
- 비동기의 필요성과 ASGI 탄생 배경
- ASGI 스펙과 WSGI와의 차이점

### Session 9: Django - 풀스택 웹 프레임워크
- Django 기초
- Django 고급 기능
- Django REST Framework

### Session 10: FastAPI - 현대적 API 프레임워크
- FastAPI 기초
- FastAPI 고급 기능
- 데이터베이스 연동

## 참여 방법

### 1. Repository Fork 및 Clone
```bash
git clone https://github.com/{your-username}/python-for-living.git
cd python-for-living
```

### 2. Branch 생성
```bash
git checkout -b session1/your-name
```

### 3. 문서 작성 및 PR
- 학습한 내용을 마크다운으로 작성
- PR 템플릿에 맞춰 제출
- 금요일까지 제출 완료

### 4. 리뷰 반영
- 코드 리뷰 코멘트 확인
- 피드백 반영 후 재요청
- 최소 3개 승인 받기

## 커뮤니케이션

- **질문 및 토론**: GitHub Issues & PR Comments
- **공지사항**: GitHub Issues
- **알림**: Slack (#5th-study-python-for-living)

## Repository 구조

```
python-for-living/
├── README.md
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── chapter1/
│   └── pythonic_code.md
├── chapter2/
│   └── type_system.md
├── chapter3/
│   └── packaging.md
└── ...
```

## 역할

- **[김현수](https://github.com/rover0811)**: 코드 리뷰, PR 머지 관리
- **스터디원**: 주제 학습, 문서 작성, 동료 리뷰, 발표

## PR 체크리스트

- [ ] 주제에 대한 핵심 내용을 다루고 있는가?
- [ ] 실습 가능한 코드 예제가 포함되어 있는가?
- [ ] 마크다운 문법이 올바르게 적용되었는가?
- [ ] 참고 자료 출처가 명시되어 있는가?
