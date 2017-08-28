# -*- coding: utf-8 -*-
import clr
import sys
import os
from fixture.group import GroupHelper


class WinApplication(object):

    class White(object):
        def __init__(self):
            project_dir = os.path.dirname(os.path.abspath(__file__))
            sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
            sys.path.append(os.path.join(project_dir, "Castle.Core.3.1.0\\lib\\net40-client\\"))
            clr.AddReferenceByName("TestStack.White")

            from TestStack.White import Application
            from TestStack.White.InputDevices import Keyboard
            from TestStack.White.WindowsAPI import KeyboardInput
            from TestStack.White.UIItems.Finders import *
            self.Application = Application
            self.Keyboard = Keyboard
            self.KeyboardInput = KeyboardInput
            self.SearchCriteria = SearchCriteria

    class UIAutomation(object):
        def __init__(self):
            clr.AddReferenceByName("UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
            from System.Windows.Automation import *
            self.ControlType = ControlType

    def __init__(self, config):
        self.white = self.White()
        self.uiauto = self.UIAutomation()
        self.group = GroupHelper(self)
        self.application = self.white.Application.Launch(config["application"]["path"])
        self.main_window = self.application.GetWindow(config["application"]["window_title"])

    def destroy(self):
        if self.main_window:
            self.main_window.Get(self.white.SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()
