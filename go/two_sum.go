package main

func twoSum(nums []int, target int) []int {
	var result []int
	existingNumbers := make(map[int][]int)

	for i, n := range nums {
		existingNumbers[n] = append(existingNumbers[n], i)
	}

	for number, occurrences := range existingNumbers {
		println("number: ", number)
		if number*2 == target {
			if len(occurrences) > 1 {
				result = []int{occurrences[0], occurrences[1]}
				break
			}
			continue
		}
		if len(occurrences) > 0 && len(existingNumbers[target-number]) > 0 {
			println("hell world: ", number, target-number)
			result = []int{occurrences[0], existingNumbers[target-number][0]}
			break
		}
	}
	return result
}

func main() {
	result := twoSum([]int{3, 2, 4}, 6)
	println("result:", result[0], ",", result[1])
}
