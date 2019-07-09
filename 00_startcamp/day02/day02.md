# what is git

git: scm(source code manager) / vcs(version control system) 두 가지 역할

git => 버전관리를 해주는 감시카메라

github => 사진들을 업로드하는 sns 개념(비슷하게는 gitlab, bitbucket도 있다)

git이 관리하는 폴더 > repo(sitory) 리포 라고 부른다 즉 카메라가 달려있는 방

![1562634422214](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562634422214.png)

* cd: change directory > 상하위 폴더로 '이동'할 때 쓰는 명령/ cd .. > 상위폴더/ cd 폴더명 > 해당 폴더로 들어가기
* rm 파일명 : 파일 삭제
* touch 파일명 : 파일 생성
* ~ : 홈(우리에게는 student)을 의미



* `git init` :감시자 생성 > 폴더 옆에 `(master)` 생성

* `git add <filename>` >> 여기보세요~

* `git commit -m '<message>'` >> 찰칵

  변경사항 저장

* `git add <filename>`

* `git commit -m '<message>'`

... 

- `git status`: 상태를 물어보는 명령어, 변경사항을 트래킹해서 보여줌
- `git log`: 사진(commit)들 로그를 보여줌



* `git add .`  또는 `git add -A` : 폴더 안에 있는 모든 파일의 변경사항을 한번에 처리하고 싶을 때 사용

* `git commit -m '<message>'` >> 찰칵

  변경사항 저장

* ```
  git remote add origin https://github.com/Dianeha/TIL.git
  git push origin master
  ```

  ★핵심은 add > commit > push

  

  ### 점심시간

  ![os and kernel family treeì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://raw.githubusercontent.com/MIAPtech/digipres-posters/master/OS_kernel_family_tree.jpg)

  

  

  # vscode

  

  ※ CLI(Command Line Interface, 명령 줄 인터페이스) - 중 하나가 cmd, bash

  ※ 프로그래밍 >> 명령어의 집합, 컴퓨터에 일을 시키는 것

  

  1. vscode에서 bash 연결함

  2. CLI에서는 자신이 어디있는지를 확인하기 >  cd를 통해 실행할 파일이 있는 경로로 이동해주기

  ![1562646804573](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562646804573.png)

  3. 그 다음 python아(동작주체) / --을 실행해줘(명령) 2단계로 명령내리기

     ![1562646820852](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562646820852.png)

  

  

  ※ ctrl + / : 드래그한 줄들이 모두 # 주석처리 됨
  
  ※ ctrl + F5 : vscode에서 자동실행 단축키(py web_browser.py 안해도 실행됨)
  
  
  
  ### web 연습
  
  ● 연습1) 브라우저창 5개 한번에 띄우기
  
  ```python
  import webbrowser
  
  urls = [
      'http://edu.ssafy.com',
    'www.google.com',
      'https://github.com/Dianeha',
    'https://2-ss3.slack.com/messages/CKWED8XAN/team/UL7PVL2VA/',
      'www.youtube.com'
]
  
for url in urls:
      webbrowser.open(url)

  ```

  
  
  ★ Web 의 기본: 4개 키워드
  
  ''주소(url)''로 ''요청'', ''문서(html,xml,)''로 ''응답''
  
  여기서의 문서는 WYSIWYG(what you see is what you get 위지위그)가 아님. 
  
  '페이지 소스 보기' 눌러서 나오는 것이 우리가 요청해서 응답받은, 다운받은 문서 > 우리가 보는 네이버 화면(정말 긴 2000줄짜리 html 한 장의 문서)이나 마크다운은 인간이 보는 문서모양.
  
  따라서 문서 내용 수정이 가능하다. 
  
  
  
  #### web에서 status code
  
  - [200] - ok
  - [404] - not found
  
  
  
  ●  연습2) 네이버 금융에서 코스피지수 가져오기
  
  ```python
  import requests
  import bs4
  
  # response라는 박스안에 네이버 소스코드 문자열 넣음
  url = 'https://finance.naver.com/marketindex/'
  response = requests.get(url).text
  # BeautifulSoup에 response를 넣었다 빼서 text에 넣음
  text = bs4.BeautifulSoup(response, 'html.parser')
  # 네이버 금융 시세 코드들 중에서 특정부분만 빼내서 kospi 박스에 넣음
  exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
  
  print(exchange_rate.text)
  
  ```



 ● 연습3) 멜론차트 50 가져오기

```python
import requests
import bs4

url = 'https://www.melon.com/chart/index.htm'

# 딕셔너리(키, 밸류)
headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    print(rank, title, artist)

```

