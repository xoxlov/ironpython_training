# -*- coding: utf-8 -*-
import time
import clr
import sys
import os
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.1.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")


from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName("UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
from System.Windows.Automation import *


def launch_application():
    application = Application.Launch("c:\\Program Files (x86)\\GAS Softwares\\Free Address Book\\AddressBook.exe")
    return application.GetWindow("Free Address Book")


def exit_application(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()


def add_new_group(main_window, name):
    modal = open_group_editor(main_window)
    modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
    modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
    Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
    close_group_editor(modal)


def open_group_editor(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    return main_window.ModalWindow("Group editor")


def close_group_editor(modal):
    modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()


def get_group_list(main_window):
    modal = open_group_editor(main_window)
    tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
    root = tree.Nodes[0]
    group_list = [node.Text for node in root.Nodes]
    close_group_editor(modal)
    return group_list


def test_add_new_group():
    main_window = launch_application()
    old_list = get_group_list(main_window)
    add_new_group(main_window, "test group")
    new_list = get_group_list(main_window)
    old_list.append("test group")
    assert sorted(old_list) == sorted(new_list)
    exit_application(main_window)
