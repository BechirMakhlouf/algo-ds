package main

func twoSum(nums []int, target int) []int {
	numPosition := make(map[int]int)

	for i, num := range nums {
		numPosition[num] = i
	}
	var result []int
	for key, val := range numPosition {
		if numPosition[target-key] != 0 || numPosition[nums[0]] == target-key {
			result = []int{val, numPosition[target-key]}
		}
	}
	return result
}
