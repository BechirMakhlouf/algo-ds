package main

// func containsDuplicate(nums []int) bool {
//   myMap := make(map[int]bool)
//
//   for _, num := range nums {
//     if myMap[num] {
//       return false
//     }
//     myMap[num] = true
//   }
//
//   return true
// }

func containsDuplicate(nums []int) bool {
	occurrences := make(map[int]bool)
	for _, num := range nums {
		if occurrences[num] {
			return true
		}
		occurrences[num] = true
	}

	return false
}
