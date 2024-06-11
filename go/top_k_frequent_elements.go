package main

import "fmt"

func topKFrequent(nums []int, k int) []int {

	nFrequency := make(map[int]int)

	for _, num := range nums {
		nFrequency[num]++
	}

	bucket := make([][]int, len(nums)+1)

	for num, freq := range nFrequency {
		bucket[freq] = append(bucket[freq], num)
	}

	result := make([]int, 0)
	numAdded := 0
	for i := len(bucket) - 1; i >= 0; i-- {
		for _, num := range bucket[i] {

			result = append(result, num)

			if numAdded++; numAdded == k {
				return result
			}
		}
	}

	return result
}

// func main() {
// 	fmt.Printf("%v\n", topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2))
// }
