from heapq import heappop, heappush

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 우선순위 큐 (최대 힙을 만들기 위해 음수 값 사용)
        max_heap = []
        
        if a > 0:
            heappush(max_heap, (-a, 'a'))
        if b > 0:
            heappush(max_heap, (-b, 'b'))
        if c > 0:
            heappush(max_heap, (-c, 'c'))
        
        result = []
        
        while max_heap:
            # 가장 많이 남은 문자를 먼저 꺼냄
            count1, char1 = heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                # 만약 연속으로 두 번 같은 문자가 나왔을 경우 두 번째 문자를 사용
                if not max_heap:
                    break  # 다른 문자가 없다면 더 이상 문자열을 만들 수 없음
                count2, char2 = heappop(max_heap)
                result.append(char2)
                count2 += 1  # 문자를 사용했으므로 하나 줄임
                if count2 < 0:
                    heappush(max_heap, (count2, char2))  # 남은 문자가 있으면 다시 삽입
                heappush(max_heap, (count1, char1))  # 첫 번째 문자는 다시 삽입
            else:
                # 가장 많이 남은 문자를 추가
                result.append(char1)
                count1 += 1  # 문자를 사용했으므로 하나 줄임
                if count1 < 0:
                    heappush(max_heap, (count1, char1))  # 남은 문자가 있으면 다시 삽입
        
        return ''.join(result)
