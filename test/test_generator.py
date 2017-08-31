# -*- coding: utf-8 -*-
from generator.group import GroupGenerator


def test_generator(app):
    gg = GroupGenerator(app)
    gg.generate()


def test_reader(app):
    gg = GroupGenerator(app)
    print(gg.read())
