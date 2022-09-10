# ably-test
- 이 레포는 ably의 테스트 과제 진행을 위해 만들어진 레포입니다.
- Developer: TaeJun Lee
- Contacts: tejunlee007@gmail.com


# Initialization
### hosts
```
127.0.0.1 w.ably-test.local
127.0.0.1 ably-test-mysql 
```

### certs
```
brew install mkcert
brew install nss # For Firefox
make certs
```

### 주요 기능 요구 사항
1. 전화 번호 인증
   - 전환번호로 실제 메세지 전송 대신 API 응답으로 랜덤 코드 반환하기
   - 코드를 입력시 인증 완료
2. 전환 번호 인증 완료 후 회원가입
   - 인증 완료 상태의 사용자만이 회원가입 절차 진행 가능
   - 고려 사항:
     - 만약 인증 완료 -> 회원가입 시도 중 중단 후 1~2일 이후에 다시 접속한다면? 전화번호 인증했다고 처리해야할지?
3. 로그인 기능
   - 식별 가능한 모든 정보로 로그인이 가능해야 합니다.
   - 식별 가능한 모든 정보가 무엇인지는 스스로 판단하여 결정하시면 됩니다.  
     예) 아이디 혹은 전화번호 + 비밀번호를 입력하면 로그인이 가능합니다.  
4. 내 정보 조회 기능
5. 비밀번호 찾기 기능

