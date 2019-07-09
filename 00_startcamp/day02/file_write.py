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
