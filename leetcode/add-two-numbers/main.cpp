/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {

public:
    ListNode *addTwoNumbers(ListNode *list1, ListNode *list2) {

        int sum = 0;
        ListNode *head = NULL;
        ListNode **solList = &head;
        while (list1 || list2 || sum > 0) {

            if (list1) {
                sum += list1->val;
                list1 = list1->next;
            }

            if (list2) {
                sum += list2->val;
                list2 = list2->next;
            }

            *solList = new ListNode(sum % 10);
            solList = &((*solList)->next);
            sum /= 10;
        }
        return head;
    }
};