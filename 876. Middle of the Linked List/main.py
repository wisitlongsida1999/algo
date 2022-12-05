


# Approach 1 >>> loop to find the length of ListNode then loop again to find the answer
class Solution(object):
    def middleNode(self, head):

        cur_node = head
        cnt_node = 1

        while 1:

            if cur_node.next != None:

                cnt_node+=1

                cur_node = cur_node.next

            else:

                break

        mid_node = cnt_node//2

        cur_node = head

        for i in range(mid_node):

            ans = cur_node.next

            cur_node = cur_node.next

        return ans
    
    
# Approach 2 >>> Loop to find the length of ListNode and store the node in List then answer from the middle member in List
class Solution(object):
    def middleNode(self, head):
        cur_node = head
        buf_node = [head]
        cnt_node = 1

        while 1:

            if cur_node.next != None:

                cnt_node+=1

                cur_node = cur_node.next

                buf_node.append(cur_node)

            else:

                break

        return buf_node[cnt_node//2]