/*
 *	From: LeetCode - 653.Two Sum IV - Input is a BST (https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)
 *	Level: Easy
 *	Question: Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
 *	Input: 
 *	5,3,6,2,4,null,7
 *	9
 *	Output:
 *	True
 *	Status: AC
 *	Solution: Using HashSet(https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution/)
*/

#include <iostream>
#include <set>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
    	if (root == NULL)
    	{
    		return false;
    	}
    	if (hash.find(k - root->val) != hash.end())
    	{
    		return true;
    	}
    	hash.insert(root->val);
    	return findTarget(root->left, k) || findTarget(root->right, k);
    }

    // void build_BST(TreeNode* &root) {
    // 	char c = getchar();
    // 	if(c == '#') {
    // 		root = NULL;
    // 		return;
    // 	}
    // 	//cout << "get: " << c << endl;
    // 	root = new TreeNode(c-'0');
    // 	build_BST(root->left);
    // 	build_BST(root->right);
    // }

    // void free_BST(TreeNode* &root) {
    // 	if(root == NULL) {
    // 		return;
    // 	}
    // 	build_BST(root->left);
    // 	build_BST(root->right);
    // 	delete root;
    // }

private:
	set<int> hash;
};


int main() {
	
	TreeNode *root;
	Solution s;
	int k;
	
	// 构造树用来进行测试
	// s.build_BST(root);

	cin >> k;
	cout << s.findTarget(root, k);

	// s.free_BST(root);
	return 0;
}