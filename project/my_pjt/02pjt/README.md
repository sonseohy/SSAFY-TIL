## 버전1_금융

### practice_b.py
```python
# 날짜 데이터 타입 변경 후 2021년 이후의 데이터만 필터링 하는 코드
df["Date"] = pd.to_datetime(df["Date"])
df_2021 = df[df['Date'] >= '2021']
```
- 날짜 데이터 타입이 object로 설정되어 있으므로 datetime으로 타입 변경을 위해 to_datetime 함수 사용
- 2021년 이후 데이터를 필터링 하기 위해 먼저 df['date'] >= '2021'을 통해 날짜가 '2021'보다 크거나 같은지 확인하고 이 코드를 다시 df에 넣어주어 조건을 만족하는 행들만 필터링 해 df_2021을 생성

```python
# x축 회전
plt.xticks(rotation=45)
```

### practice_d.py
```python
df_2021['month'] = df_2021['Date'].dt.to_period('M')
monthly_avg = df_2021.groupby('month')['Close'].mean()
monthly_avg.index = monthly_avg.index.to_timestamp()
```
- df_2021['month'] = df_2021['Date'].dt.to_period('M')
  - dt.to_period('M') : 날짜를 월별 기간 (Period)으로 변환
  - 형식: 결과는 Period 객체로, 연도와 월을 포함한 특정 기간을 나타냅니다. 예를 들어, 2021-01-15는 2021-01로 변환됨
  - dt.month도 날짜에서 월 정보를 추출하는 방법이지만 출력 형식이 2021-01-15를 1로 변환하여 출력

- monthly_avg = df_2021.groupby('month')['Close'].mean()
  - groupby 메서드는 데이터를 그룹화하여 연산을 수행하는 메서드로, 추가 메서드를 붙여 연산이나 다양한 메서드 적용이 가능함
  - df.groupby('그룹화를 진행할 열')['연산을 진행할 열'].연산 메서드

- monthly_avg.index = monthly_avg.index.to_timestamp()
  - to_timestamp는 주기의 시작값으로 타임스탬프의 DatetimeIndex로 캐스트하는 메서드
  - PeriodIndex를 DatetimeIndex로 변환, PeriodIndex는 기간을 나타내는 반면, DatetimeIndex는 특정 날짜와 시간을 나타냄
  

## 버전2_영화 : aladin

### practice_c.py
#### 딕셔너리 값(value)을 정렬하는 방법
- dictionary의 value 값으로 정렬하는 방법은 sorted 함수 사용
- sorted 함수는 key를 받을 수 있는데, key를 받는 자리에 lambda 식을 사용
- sorted() 함수에 딕셔너리의 items() 메소드를 이용하여 (키, 값) 쌍의 리스트를 만들고, 정렬 기준으로 사용할 값을 선택(튜플의 1번 index를 기준으로 정렬)하여 lambda 함수를 만들어서 sorted() 함수의 key 인자로 전달

#### sort() vs sorted()
- 리스트를 제자리에서(in-place) 수정하는 내장 list.sort() 메서드
- 이터러블로부터 새로운 정렬된 리스트를 만드는 sorted() 내장 함수
- 차이점 : sort() 메서드는 리스트에게만 정의됨, sorted() 함수는 모든 이터러블을 받아들임

#### sorted(iterable, /, *, key=None, reverse=False)
- 키워드 인자로만 지정해야 하는 두 개의 선택적 인자 존재
- key는 하나의 인자를 받는 함수를 지정 : iterable 각 요소들로부터 비교 키를 추출하는 데 사용, 기본값은 None
- reverse는 논리값. True로 설정되면, 각 비교가 뒤집힌 것처럼 리스트 요소들이 정렬

