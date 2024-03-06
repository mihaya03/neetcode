package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {

	if head == nil {
		return head
	}

	dummy := &ListNode{0, head}
	length := 0
	first := head

	// 連結リストの要素数を取得
	for first != nil {
		length++
		first = first.Next
	}

	// 削除すべき要素の手前(最後尾からN+1番目)まで移動
	first = dummy
	for i := 0; i < length-n; i++ {
		first = first.Next
	}

	// 削除
	first.Next = first.Next.Next
	return dummy.Next

}
