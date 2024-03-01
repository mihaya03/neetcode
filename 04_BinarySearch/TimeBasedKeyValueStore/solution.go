type TimeValuePair struct {
	timestamp int
	value     string
}

type TimeMap struct {
	store map[string][]TimeValuePair
}

func Constructor() TimeMap {
	return TimeMap{store: make(map[string][]TimeValuePair)}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	if _, ok := this.store[key]; !ok {
		this.store[key] = make([]TimeValuePair, 0)
	}
	this.store[key] = append(this.store[key], TimeValuePair{timestamp, value})
}

func (this *TimeMap) Get(key string, timestamp int) string {
	// keyが存在しない場合
	if _, ok := this.store[key]; !ok {
		return ""
	}

	// keyが存在する場合は二分探索を行う
	left, right := 0, len(this.store[key])-1
	for left <= right {
		mid := left + (right-left)/2
		if this.store[key][mid].timestamp <= timestamp {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	// 指定されたtimestampが、そのkeyに設定されたすべてのtimestampよりも小さい場合
	if right < 0 {
		return ""
	}

	return this.store[key][right].value
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */