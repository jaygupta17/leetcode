class Solution {
        
        public ListNode sortList(ListNode head){
            return mergeSort(head);
    }
    
        public static ListNode mergeTwoLL(ListNode left , ListNode right) {
          ListNode head = null;
          ListNode tail =null;

          if(right.val>left.val){
          head = left;
          tail=left;
          left = left.next;
        }
        else{
            head=right;
            tail=right;
            right=right.next;
        }
        while(left!=null && right!=null){
            if(left.val> right.val){
                tail.next=right;
                tail=tail.next;
                right=right.next;
            }
            else{
                tail.next=left;
                tail=tail.next;
                left=left.next;
            }
        }
        if(left!=null){
            tail.next=left;
        }
        else{
            tail.next=right;
        }
        return head;
        }
        public static ListNode middle(ListNode head){
       
         ListNode slow=head;
         ListNode fast=head;
        while(fast.next!=null && fast.next.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        return slow;
    }

        public static ListNode mergeSort(ListNode head) {

        if(head==null || head.next==null){
            return head;
        }
        ListNode mid = middle(head);
        ListNode leftHead=head;
        ListNode rightHead=mid.next;
        mid.next=null;
      leftHead=mergeSort(leftHead);
        rightHead=mergeSort(rightHead);

        return mergeTwoLL(leftHead,rightHead);
        }

 
     
    
}