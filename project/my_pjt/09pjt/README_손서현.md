# 09-pjt


### iframe: 외부 웹사이트 콘텐츠를 웹페이지 내에 삽입
1. i-frame
- 효과적으로 다른 HTML 페이지를 현재 페이지에 포함시키는 중첩된 브라우저
- iframe 요소를 이용하면 해당 웹 페이지 안에 어떠한 제한 없이 다른 페이지를 불러와서 삽입할 수 있다.
- iframe의 기본구조
```html
<iframe 
  src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
  width="560" 
  height="315" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
  allowfullscreen
></iframe>
```

2. iframe 속성
- src : 삽입 할 홈페이지 url
- name : 프레임 이름
- width : 프레임 가로 너비
- height : 프레임 세로 길이
- frameborder : 프레임 테두리 선 (0으로 설정하면 프레임의 테두리선 x, 1로 설정하면 프레임의 테두리선 o)
- scrolling : 스크롤바의 표시 여부를 나타냅니다. (yes로 설정하면 스크롤 바 무조건 표시, auto는 자동 표시)