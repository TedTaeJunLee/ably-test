# ably-test
- 이 레포는 ably의 테스트 과제 진행을 위해 만들어진 레포입니다.
- Developer: TaeJun Lee
- Contacts: tejunlee007@gmail.com

# Requirements
- django 4.1.1 이상
- poetry (package Manager)
- mysql 5.7(or sqlite3 for local test)


# Initialization
### hosts
로컬에서 127.0.0.1 특정 domain 을 연결하여 테스트 하고 싶을때 사용합니다.
/etc/hosts 내부에 아래의 코드를 넣어줍니다.
```
127.0.0.1 w.ably-test.local
127.0.0.1 ably-test-mysql 
```

### certs
로컬에서 https(SSL)로 동작하는 API 를 실행하기 위해 설치해 줍니다.. 
```
brew install mkcert
brew install nss # For Firefox
make certs
```

#### Install Poetry(optional)
해당 프로젝트의 package 관리는 poetry를 사용하여 행해집니다.
- docker-compose로 실행시에는 로컬 PC #### Install Poetry
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && source $HOME/.poetry/env
```
- [Pycharm plugin](https://koxudaxi.github.io/poetry-pycharm-plugin/)
환경에 설치하지 않아도 되지만 로컬에서 poetry의 가상환경 세팅 경험을 해보기 싶으시다면 아래의 명령어로 poetry를 설치해줍니다.
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && source $HOME/.poetry/env
```
- [Pycharm plugin](https://koxudaxi.github.io/poetry-pycharm-plugin/)

### 앱 실행 방법
- 로컬에서 장고앱 실행시
   ```
      cd 'root 폴더'
      make run-local-ably-test-backend 
   ```
- docker-compose로 실행시
   ```
      시간이 부족하여 완료 못하였습니다.
   ```
  
### API Swagger 문서 접근 주소
   ```
      http://0.0.0.0:8000/api/swagger/
      http://127.0.0.1:8000/api/swagger/
   ```


### 개발 API 명세 및 테스트 시 참고 사항 
1. 회원 가입 위한 전화 번호 인증 (/validations/phone-validation/send-code/ & /validations/phone-validation/verify-code/)
   - 회원 가입을 위한 전화 번호 인증 API 에서 usage_type = 'SING_UP' 입니다
   - 전환번호로 실제 메세지 전송 대신 API 응답으로 랜덤 코드 반환하기
   - 유효한 인증 번호를 tracking 하기 위햇 phone_validation_code 라는 테이블을 만듬. code 생성 히스토리를 트랙킹.
   - phone_validation_code 에 expire_at 을 두어서 유효시간이 지난 코드의 경우 사용 안하도록 처리
   - 인증 완료시 반환 받는 token(jwt)을 사용하여 회원가입시 인증 완료 여부 체크(해당 토큰은 5분만 유효하도록 설정)
2. 회원가입(/accounts/sign-up/)
   - 인증 완료 상태의 사용자만이 회원가입 절차 진행 가능하도록 구현
   - 개발 기능 요구 사항애 명시된 필요한 데이터 + 전화번호 인증 token을 API에 전달하여 회원가입 진행 가능
   - 인증 완료 token의 유효 기간이 지난 상태라면 회원가입이 실패하도록 처리
   - 고려 사항:
     - 이미 사용중인 이메일 혹은 닉네임 혹은 phone이라면 회원가입을 거부하도록 하였습니다.
3. 로그인 기능(/accounts/sign-in/)
   - (아매일 / 닉네임 / 전화번호) + 비밀번호 조합으로 로그인 시 로그인 되도록 구현하였습니다
4. 내 정보 조회 기능(/accounts/users/me/)
   - 로그인 / 회원가입 이후 발급받은 token(jwt)을 사용하여 정보를 조회 할 수 있습니다.
   - 기본적으로 이메일 & 전화번호는 보안을 위해서 API 응답시 masking 처리 하였습니다.
5. 비밀번호 재설정을 위한 전화 번호 인증 (/validations/phone-validation/send-code/ & /validations/phone-validation/verify-code/)
    - 비밀번호 재설정을 위한 전화 번호 인증 API 에서 usage_type = 'PASSWORD_RESET' 입니다
    - 성공시 200 status_code 가 응답됩니다.
. 비밀번호 재설정(/accounts/password-reset/)
   - 비밀번호 재설정을 위한 전화 번호 인증 API 에서 발급받은 token을 사용하여 비밀번호를 재설정 합니다 
   - 성공시 200 status_code 가 응답됩니다.
