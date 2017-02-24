def Reverse_Recursive(head):
    cur = head
    new_head = head

    while cur is not None:
        temp_prev = cur.prev
        cur.prev = cur.next
        cur.next = temp_prev
        new_head = cur
        cur = cur.prev

    return new_head
