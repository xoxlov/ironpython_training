# -*- coding: utf-8 -*-
import random
import string


def random_group_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


def test_add_new_group(app):
    old_list = app.group.get_group_list()
    new_group_name = random_group_name("Group ", 10)
    app.group.add_new_group(new_group_name)
    new_list = app.group.get_group_list()
    old_list.append(new_group_name)
    assert sorted(old_list) == sorted(new_list)
