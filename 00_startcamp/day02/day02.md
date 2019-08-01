# what is git

git: scm(source code manager) / vcs(version control system) 두 가지 역할

git => ''버전관리를 해주는 감시카메라''

github => 사진들을 업로드하는 sns 개념(비슷하게는 gitlab, bitbucket도 있다)

git이 관리하는 폴더 > repo(sitory) 리포 라고 부른다 즉 카메라가 달려있는 방

검은색창 > 터미널

![1562634422214](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562634422214.png)

* / : 최상단 디렉토리 : /c/Users/student 처럼

* ~ : 홈(우리에게는 student) 디렉토리를 의미

* pwd : 지금 내 위치 보기

* cd: change directory > 상하위 폴더로 '이동'할 때 쓰는 명령/ cd .. > 상위폴더/ cd 폴더명 > 해당 폴더로 들어가기

* mkdir 폴더명 : 폴더 생성 

* touch 파일명 : 파일 생성 ex) touch test.txt

* rm 파일명 : 파일 삭제 ex) rm test.txt >> 휴지통에 가는 것이 아니고 날라가기 때문제 주의

* rm -r 폴더명/ : 폴더 삭제 ex) rm -r test/

* rm -rf  폴더명/ : 폴더안에 파일이 있든없든 강제로 폴더를 지운다(위험한 명령어, 주의)

* ctrl + c : 취소(cancel) ☆

* ctrol + d: 종료

* ctrk + backspace/w : 단어단위 삭제 

* clear 입력하거나 ctrl + l : 하면 화면이 깔끔하게 올라감 정리. ☆

* 방향키 위: 이전에 입력했던 명령어들 다시 나옴

* ls : 폴더안에 있는 파일 리스트 쭉 보여주기

* ls -a : ./ ../

* cp : 복사

* mv : 이동

* 이름바꾸기도 mv를 쓴다 : mv not_hidden mymy 

* sudo (superuser do:) : 컴퓨터가 막아놓은 일을 가능하게 만드는 명령 > 가능한 안쓰는 것이 좋다

  빨간불에 길을 건널 수 있지만 안건너는게 좋은 것처럼

* 



절대경로 : cd ~/learn_cli/ > 내가 지금 어디있든지 저 위치로 갈것이다.

상대경로 :  ../을 사용하는 것



touch ../where.txt > 내 자리 기준으로 상위폴더에 where이라는 텍스트 파일 만들어짐

rm ../where.txt > 폴더 위치 이동하지 않고도 삭제 가능

touch .hidden >> 윈도우라서 안숨겨지는 것이지 .으로 시작하는 파일은 숨김의 의미가 있다. > ls로는 숨겨진 아이를 볼 수 없고 ls -a해야 볼 수 있다.

touch not_hidden 

mkdir .hidden_dir >  .으로 시작해서 ''숨겨진 폴더 만들기''

cp not_hidden n_h > 같은 공간이므로 not_hidden 을 복사해 n_h 이름의 파일을 생성(같은 이름 불가)

cp not_hidden ../ > 상위공간에 not_hidden 복사본 파일 생성 (다른 공간이므로 이름 달라도 상관없음)

cp not_hidden ./.hidden_dir/n_h > 지금 공간에 hidden_dir 이라는 파일안에 n_h라는 이름으로 복사하겠다



mv .hidden ../

mv ../.hidden .(/) (상위폴더에 있는 hidden 파일을 내 위치로 가져오겠다)



<폴더의 버전관리(최종, 최최종, 진짜 최종...)를 해주는 git 이라는 카메라를 다는 방법>

* `touch .gitignore` 를 먼저하기(init 전에)

* `git init` :감시자 생성 > 폴더 옆에 `(master)` 생성 >> 상위폴더는 카메라 영향을 안받고 하위폴더는 모두 감시되고 있음
* `ls -a` init 후 해보면 .git 이라는 폴더가 생성된 것을 확인할 수 있음(`rm -r .git/` 하면 master 표시가 사라지고 날리는 것이 가능 > 다시 `git init` 가능)
* `git add <filename>` >> 여기보세요~, stage에 올린다는 개념 ex) git add .gitignore/ add . 는 위치가 중요한 것임. 현재 위치
* `git status`: 상태를 물어보는 명령어, 변경사항을 트래킹해서 보여줌 



* `git commit -m '<message>'` >> 찰칵

  변경사항 저장(최종, 진짜 최종, 최최최최종 이런 한 줄 한줄의 기록 의미) / commit은 위치가 중요하지 않음

- `git log`: 사진(commit)들 로그를 보여줌ㅊㅇ



* `git add .`  또는 `git add -A` : 폴더 안에 있는 모든 파일의 변경사항을 한번에 처리하고 싶을 때 사용

  전체가 스테이지에 올려짐( 여기서 . 은 내 위치를 말하는 것임)

* `git commit -m '<message>'` >> 찰칵

  변경사항 저장

* ```
  git remote add aa https://github.com/Dianeha/TIL.git // '이름을 aa'으로 설정한 것
  git remote -v // 이것으로 등록된 이름 확인 가능
  git remote rm aa // 날라감
git push aa master
  (git push -u aa master 로 등록해두면 git push만해도 aa로 들어감, 거기에만 push할 것 같으면)
```
  
★핵심은 add > commit > push
  

  
* `rm -r .git`> 카메라를 떼는 법, master 가 없어진다
  

  
디스크 > 파일, 폴더만 저장 가능
  
cd / > /는 루트(근원)의 의미, 최상단 디렉토리로 이동
  

  

  
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
  
  
  
  ### web 스크래핑과 크롤링 연습
  
  - 웹 스크래핑(website scraping, 웹페이지에서 이름이나 이메일 주소 같은 데이터를 수집하는 것)
  - **웹 크롤링**(Web Crawling)
  
  
  
  
  
● 연습1) 브라우저창 5개 한번에 띄우기
  
  ```python
  import webbrowser
  
  ```

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
  
  요청은 '주소(url)'로 하고, '응답'은 '문서(html,xml,)'로 온다
  
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
# 페이지에스 F12 > copy > copy selector
rows = text.select('.lst50')


for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    print(rank, title, artist)

```



### File control

- file_write(파일 만드는 법)

```python
# CSV 형식 excel viewer를 다운받음
lunches = {
    '양자강': '02-456-1256',
    '김밥카페': '02-521-5555',
    '순남시레기': '02-565-6547'
}

# lunch라는 파일 쓰기
# 'w': write
with open('lunch.csv', 'w', encoding='utf-8') as f:
    f.write('식당이름, 전화번호\n')
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')

```



- file_read(파일 불러오는 법)

```python
import csv

# 'r': read
with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)

```



cd collabo_prj/

touch .gitignore

code .

깃 이그노어에 .vscode/넣기

git init

