import pytest 
from linked_list_demo import Node


@pytest.mark.linkedlist
def test_insert(linked_list_obj):
	linked_list_obj.insert(Node("A"))
	assert linked_list_obj.head.data == "A"
	linked_list_obj.insert(Node("B"))
	assert linked_list_obj.head.next.data == "B"

@pytest.mark.linkedlist
def test_contains(linked_list_obj_elems):
	assert linked_list_obj_elems.contains("A") == True
	assert linked_list_obj_elems.contains("J") == False

@pytest.mark.linkedlist	
def test_delete(linked_list_obj_elems):
	linked_list_obj_elems.delete("A")
	assert linked_list_obj_elems.head.data == "B"
	assert linked_list_obj_elems.head.next.data == "C"
	linked_list_obj_elems.delete("C")
	assert linked_list_obj_elems.head.next.data == "D"
	

@pytest.mark.linkedlist
def test_is_empty(linked_list_obj, linked_list_obj_elems):
	assert linked_list_obj.is_empty() == True
	assert linked_list_obj_elems.is_empty() == False

	
@pytest.mark.linkedlist
def test_length(linked_list_obj):
	assert linked_list_obj.length() == 0
	linked_list_obj.insert(Node("A")) 
	assert linked_list_obj.length() == 1

@pytest.mark.linkedlist
def test_str(linked_list_obj_elems):
	assert linked_list_obj_elems.__str__() == "A->B->C->D"



