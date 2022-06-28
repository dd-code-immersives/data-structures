import pytest


def test_get_min_val(simple_tree_obj,tree_obj):

	assert simple_tree_obj.get_min_val() == 1
	assert tree_obj.get_min_val() == 1

def test_get_min_val_t(simple_tree_obj,tree_obj):

	assert simple_tree_obj.get_min_val_t() == 1
	assert tree_obj.get_min_val_t() == 1 

def test_get_max_val(simple_tree_obj,tree_obj):

	assert simple_tree_obj.get_max_val() == 3
	assert tree_obj.get_max_val() == 14

def test_get_max_val_t(simple_tree_obj,tree_obj):

	assert simple_tree_obj.get_max_val_t() == 3
	assert tree_obj.get_max_val_t() == 14

def test_in_order_traversal(simple_tree_obj,tree_obj):
	assert simple_tree_obj.in_order_traversal() == [1, 2, 3]
	assert tree_obj.in_order_traversal() == [1, 3, 4, 6, 7, 8, 10, 13, 14]

def test_pre_order_traversal(simple_tree_obj,tree_obj):

	assert simple_tree_obj.pre_order_traversal() == [2, 1, 3]
	assert tree_obj.pre_order_traversal() == [8, 3, 1, 6, 4, 7, 10, 14, 13]

def test_post_order_traversal(simple_tree_obj,tree_obj):

	assert simple_tree_obj.post_order_traversal() == [1, 3, 2]
	assert tree_obj.post_order_traversal() == [1, 4, 7, 6, 3, 13, 14, 10, 8]

def test_insert(simple_tree_obj,tree_obj):

	simple_tree_obj.insert(4)
	tree_obj.insert(15)
	tree_obj.insert(9)
	assert simple_tree_obj.right.right.data == 4
	assert tree_obj.right.right.right.data == 15
	assert tree_obj.right.left.data == 9

def test_search(simple_tree_obj,tree_obj):

	found1, path1 = simple_tree_obj.search(3)

	found1a, _ = simple_tree_obj.search(5)
	found2, path2 = tree_obj.search(6)

	assert found1 == True 
	assert path1 == "2-3"

	assert found2 == True
	assert path2 == "8-3-6"

	assert found1a == False


def test_get_level(simple_tree_obj,tree_obj):

	assert simple_tree_obj.get_level(3) == 1
	assert tree_obj.get_level(4) == 3


def test_is_identical(simple_tree_obj,tree_obj):

	assert not simple_tree_obj.is_identical(tree_obj)
	assert simple_tree_obj.is_identical(simple_tree_obj)