# -*- coding: utf-8 -*-
import pytest
import os
import json
import jsonpickle
from fixture.application import WinApplication
from generator.group import GroupGenerator

fixture = None
target = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    if not fixture:
        fixture = WinApplication()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture:
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def load_config(file):
    global target
    if target is None:
        config_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_name) as config_file:
            target = json.load(config_file)
    return target


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = GroupGenerator(app).read()
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
