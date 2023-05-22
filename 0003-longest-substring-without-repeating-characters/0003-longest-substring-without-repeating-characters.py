import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0

        q = collections.deque()
        for i in s:
            # 큐에 들어있지 않다면 삽입한다.
            if i not in q:
                q.append(i)
            else:
                # 큐에 들어있다면 index를 찾는다
                index = q.index(i)

                # 인덱스까지의 모든 요소를 pop 한다.
                for j in range(index + 1):
                    q.popleft()

                # 다시 문자열을 넣어준다.
                q.append(i)

            # 문자열이 들어오고 나갈때 마다 최대값을 비교한다.
            max_len = max(max_len, len(q))

        return max_len
                
            
        