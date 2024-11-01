# 05-pjt

### 검색 결과 추출
```python
import io

  keywords = Keyword.objects.all()

  for kw in keywords:
      titles = get_google_data(kw.name, period='year')
      
      # 검색 결과 개수 추출
      match = re.search(r'([\d,]+)', titles)
      search = int(match.group(1).replace(',', ''))
```
- 첫 번째 그룹에 결과 개수가 저장되어 있으므로 group(1)을 가져와 쉼표를 제거한 후 정수로 변환해야 데이터베이스에 저장이 가능하다.

### 막대 그래프 그리기
```python
  # 키워드와 결과 값을 각각 리스트로 만듭니다.
    keywords = [trend.name for trend in trends]
    values = [trend.result for trend in trends]

    # 그래프의 크기를 설정 후 keywords와 value 값으로 막대그래프를 그린다.
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, values)

    # 그래프 제목과 축 레이블을 설정합니다.
    plt.title("Technology Trend Analysis")
    plt.ylabel("Result")
    plt.xlabel("Keyword")
    plt.grid(True)  # 그리드를 추가합니다.
    plt.legend(["Trends"], loc="best")  # 범례를 추가

    # 그래프 이미지를 메모리에 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png')  # PNG 형식으로 저장
    plt.close()
    buf.seek(0)  # 버퍼의 포인터를 처음으로 이동
    image_png = buf.getvalue()  # 이미지 데이터를 가져옵니다.
    graph = base64.b64encode(image_png).decode('utf-8')  # 이미지 base64로 인코딩

    # 컨텍스트에 그래프 데이터를 추가
    context = {
        'graph': graph,
    }
```
- pip install matplotlib으로 matplotlib 라이브러리를 가져와야 한다.
- keywords와 value 값으로 막대그래프를 그린다.