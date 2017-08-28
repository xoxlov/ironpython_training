# -*- coding: utf-8 -*-
import time

def test_minimum(app):
    app.group.open_group_editor()
    time.sleep(1)
    app.group.close_group_editor()
