class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        return sorted(hashmap, key=hashmap.get, reverse=True)[:k]