package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
  if head.Next == nil {
    return head
  }
  head.Next = reverseList(head.Next)

  return head 
}
