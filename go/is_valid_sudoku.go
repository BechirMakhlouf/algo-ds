package main

import "fmt"

func isValidSudoku(board [][]byte) bool {
	// check for rows
	for i := 0; i < 9; i++ {
		existingNumbers := make(map[byte]bool)
		for j := 0; j < 9; j++ {
			c := board[i][j]
			if c == '.' {
				continue
			}
			if existingNumbers[c] {
				return false
			}
			existingNumbers[c] = true
		}
	}

	// check for columns
	for i := 0; i < 9; i++ {
		existingNumbers := make(map[byte]bool)
		for j := 0; j < 9; j++ {
			c := board[j][i]
			if c == '.' {
				continue
			}
			if existingNumbers[c] {
				return false
			}
			existingNumbers[c] = true
		}
	}

	var squareNumbers [3][3]map[byte]bool

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			c := board[j][i]

			if c == '.' {
				continue
			}

			if squareNumbers[i/3][j/3] == nil {
				squareNumbers[i/3][j/3] = make(map[byte]bool)
			}

			if squareNumbers[i/3][j/3][c] {
        fmt.Printf("/v", squareNumbers[i/3][j/3])
				return false
			}

			squareNumbers[i/3][j/3][c] = true
		}
	}

	return true
}


