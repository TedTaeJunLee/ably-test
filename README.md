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
환경에 설치하지 않아도 되지만 로컬에서 poetry의 가상환경 세팅 경험을 해보기 싶으시다면 아래의 명령어로 poetry를 설치해줍니다.
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && source $HOME/.poetry/env
```

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
