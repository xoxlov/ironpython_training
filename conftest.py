# -*- coding: utf-8 -*-
import pytest
import os
import json
from fixture.application import WinApplication

fixture = None
target = None


@pytest.fixture(scope="session", autouse=True)
def app(request, config):
    global fixture
    if not fixture:
        fixture = WinApplication(config=config)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture:
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


def load_config(file):
    global target
    if target is None:
        config_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_name) as config_file:
            target = json.load(config_file)
    return target


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
