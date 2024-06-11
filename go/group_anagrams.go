package main

import (
	"slices"
)

func sortString(str string) string {
	runes := []rune(str)
	slices.Sort(runes)
	return string(runes)
}
func groupAnagrams(strs []string) [][]string {
	anagramsMap := make(map[string][]string)
	for _, str := range strs {
		anagramsMap[sortString(str)] = append(anagramsMap[sortString(str)], str)
	}
	result := make([][]string, 0)

	for _, group := range anagramsMap {
		if len(group) > 0 {
			result = append(result, group)

		}
	}

	return result
}

func main() {
	my_str := "bechir"
	runes := []rune(my_str)
	slices.Sort(runes)
	println(string(runes))
}
