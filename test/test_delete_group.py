# -*- coding: utf-8 -*-
import random


def test_delete_group(app):
    old_list = app.group.get_group_list()
    group_to_delete_number = random.randrange(len(old_list))
    app.group.delete_group_by_index(group_to_delete_number)
    new_list = app.group.get_group_list()
    old_list.remove(old_list[group_to_delete_number])
    assert sorted(old_list) == sorted(new_list)
