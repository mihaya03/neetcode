package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	// 真ん中で連結リストを分割する
	firstHalf, secondHalf := splitList(head)

	// 分割された後半部分の連結リストは逆順にソートする
	secondHalf = reverseList(secondHalf)

	// 前半と後半の連結リストを交互に連結する
	first := firstHalf
	second := secondHalf
	for first != nil && second != nil {
		nextFirst := first.Next
		nextSecond := second.Next

		first.Next = second
		if nextFirst == nil {
			break
		}
		second.Next = nextFirst

		first = nextFirst
		second = nextSecond
	}

}

func splitList(head *ListNode) (*ListNode, *ListNode) {
	if head == nil || head.Next == nil {
		return head, nil
	}

	slow := head
	fast := head.Next

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	secondHalf := slow.Next
	slow.Next = nil

	return head, secondHalf
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	var prev *ListNode = nil
	current := head

	for current != nil {
		next := current.Next
		current.Next = prev
		prev = current
		current = next
	}
	return prev
}
