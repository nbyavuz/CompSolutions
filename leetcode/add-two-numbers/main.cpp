/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {

private:
    int findLen(ListNode *list) {
        int i = 1;
        for(; list->next; i++){
            list = list->next;
        }
        return i;
    }

public:
    ListNode *addTwoNumbers(ListNode *list1, ListNode *list2) {

        int len1 = findLen(list1);
        int len2 = findLen(list2);

        std:cout << "Len 1 = " << len1 << " Len 2 = " << len2 << std::endl;
        return NULL;


    }
};