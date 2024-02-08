func isAnagram(s string, t string) bool {
	s_map := make(map[rune]int)
	for _, char := range s {
		s_map[char]++
	}
	t_map := make(map[rune]int)
	for _, char := range t {
		t_map[char]++
	}
	if len(s_map) != len(t_map) {
		return false
	}
	for key, value1 := range s_map {
		if value2, ok := t_map[key]; !ok || value2 != value1 {
			return false
		}
	}
	return true
}