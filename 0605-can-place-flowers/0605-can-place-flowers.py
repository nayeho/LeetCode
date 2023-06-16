class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        one_cnt = flowerbed.count(1)
        
        one_index_list = []
        cnt = 0
        
        if one_cnt >= 2:
            for i, bed in enumerate(flowerbed):
                if bed == 1:
                    one_index_list.append(i)



            for i in range(len(one_index_list) - 1):
                start = one_index_list[i]
                end = one_index_list[i + 1]
                cnt_zero = end - start - 1
                cnt += (cnt_zero - 1) // 2

            # start
            if flowerbed[0] == 0:
                start = one_index_list[0]
                cnt += start // 2

            if flowerbed[-1] == 0:
                end = one_index_list[-1]
                cnt += (len(flowerbed) - 1 - end) // 2
                
        elif one_cnt == 1:
            one_idx = flowerbed.index(1)
            cnt += one_idx // 2
            cnt += (len(flowerbed) - 1 - one_idx) // 2
            
        else:
            # 1 -> 1, 2 -> 1, 3-> 2, 4 -> 2, 5 -> 3
            cnt += (len(flowerbed) + 1) // 2
            
            
        return cnt >= n