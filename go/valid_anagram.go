package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	s_occurrences := [26]int{}
	t_occurrences := [26]int{}

	for _, c := range s {
		s_occurrences[c-'a']++
	}
	for _, c := range t {
		t_occurrences[c-'a']++
	}

	for i := range s_occurrences {
		if s_occurrences[i] != t_occurrences[i] {
			return false
		}
	}

	return true
}

// func main() {
//   println("result: ", isAnagram("angrama", "anagram"))
// }
