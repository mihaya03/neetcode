'''
timestampは単調増加するため、
setの際にタイムスタンプと値のペアをリストの末尾に追加すれば、
getの際には二分探索を行うことで、値をO(logN)で取得できる。
'''

class TimeMap:

    def __init__(self):
        self.map = {} # key: int, value: List[str]  
                
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
            self.map[key].append([timestamp, value])
        else:
            self.map[key].append([timestamp, value])
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        values = self.map[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1       
        return "" if right < 0 else values[right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)