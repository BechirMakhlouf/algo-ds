package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	chars := [26]uint16{}

	for i := 0; i < len(s); i++ {
		chars[s[i]-'a']++
	}

	for i := 0; i < len(t); i++ {
		chars[t[i]-'a']--
		if chars[t[i]-'a'] < 0 {
			return false
		}
	}
	for _, n := range chars {
		if n != 0 {
			return false
		}
	}
	return true
}
