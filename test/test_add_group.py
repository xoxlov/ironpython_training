# -*- coding: utf-8 -*-


def test_add_new_group(app, data_groups):
    old_list = app.group.get_group_list()
    new_group_name = str(data_groups)
    app.group.add_new_group(new_group_name)
    new_list = app.group.get_group_list()
    old_list.append(new_group_name)
    assert sorted(old_list) == sorted(new_list)
