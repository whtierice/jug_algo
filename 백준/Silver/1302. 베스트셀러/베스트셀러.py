import sys
from collections import defaultdict

def solve():
    # 1. 입력 설정 (빠른 입출력)
    input = sys.stdin.readline
    
    # N 입력 받기
    N = int(input())
    
    # 2. 집계 (Aggregation) - defaultdict(int) 활용
    books = defaultdict(int)
    
    # N번 반복하며 책 제목 입력 받고 카운팅
    # 주의: 입력받은 문자열 양 끝의 공백(줄바꿈) 제거 필요
    for _ in range(N):
        name_book = input().strip()
        books[name_book] += 1
        
    # ---------------------------------------------------------
    # [쉬운 접근법 로직]
    
    # 3. 1차 정렬: '책 제목(Key)' 순으로 먼저 정렬
    # 목적: 판매량이 같을 때 자동으로 사전 순으로 앞선 것을 선택하기 위함
    # 힌트: 딕셔너리의 .items()를 sorted() 함
    
    rank = sorted(list(books.items()))
    
    # 4. 최종 추출: 정렬된 리스트에서 '판매량(Value)'이 가장 큰 것 뽑기
    # 힌트: max() 함수와 key=lambda 활용 (판매량 기준)
    
    top_sale = max(rank, key=lambda x: x[1])
    
    # ---------------------------------------------------------
    
    # 5. 결과 출력 (가장 많이 팔린 책의 제목만)
    print(top_sale[0])
    

if __name__ == "__main__":
    solve()