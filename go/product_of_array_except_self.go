package main

import "fmt"

func productExceptSelf(nums []int) []int {
	result := make([]int, len(nums))

	acc := 1
	zeroIndex := -1
  result[0] = 1
	for i := 1; i < len(nums); i++ {

		if nums[i - 1] == 0 {
			if zeroIndex != -1 {
				return make([]int, len(nums))
			}
			zeroIndex = i - 1
			continue
		}

		acc *= nums[i-1]
		result[i] = acc
	}

	if zeroIndex != -1 {
		result := make([]int, len(nums))
		result[zeroIndex] = acc
		return result
	}

	acc = 1
  fmt.Printf("result: %v\n", result)
	for i := len(nums) - 2; i >= 0; i-- {
		acc *= nums[i+1]
		result[i] *= acc
	}
	return result
}

// func main() {
// 	fmt.Printf("%v\n", productExceptSelf([]int{1, 2, 3, 4}))
// }
