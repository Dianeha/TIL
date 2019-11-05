// node는 JS가 서버도 관리할 수 있도록 해줌
// 아래는 서버를 직접 짠것 >> 앞으로는 프레임워크를 사용할 것(vue.js)

const http = require('http');
const port = 3001;

http.createServer((req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/plain',
    }); // 요청 헤드
    res.statusCode = 200;
    res.end('End of response\n');
}).listen(port); // 몇번 포트에서 듣겠다

console.log(`Server is running @ http://localhost:${port}`);