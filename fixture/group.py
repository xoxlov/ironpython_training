# -*- coding: utf-8 -*-


class GroupHelper(object):
    def __init__(self, app):
        self.app = app
        self.modal = None

    def get_group_list(self):
        self.modal = self.open_group_editor()
        tree = self.modal.Get(self.app.white.SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        group_list = [node.Text for node in root.Nodes]
        self.close_group_editor()
        return group_list

    def open_group_editor(self):
        self.app.main_window.Get(self.app.white.SearchCriteria.ByAutomationId("groupButton")).Click()
        self.modal = self.app.main_window.ModalWindow("Group editor")
        return self.modal

    def close_group_editor(self):
        if self.modal:
            self.modal.Get(self.app.white.SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()
            self.modal = None

    def add_new_group(self, name):
        self.modal = self.open_group_editor()
        self.modal.Get(self.app.white.SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        self.modal.Get(self.app.white.SearchCriteria.ByControlType(self.app.uiauto.ControlType.Edit)).Enter(name)
        self.app.white.Keyboard.Instance.PressSpecialKey(self.app.white.KeyboardInput.SpecialKeys.RETURN)
        self.close_group_editor()

    def delete_group_by_index(self, index=0):
        self.modal = self.open_group_editor()
        tree = self.modal.Get(self.app.white.SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        root.Nodes[index].Click()
        self.modal.Get(self.app.white.SearchCriteria.ByAutomationId("uxDeleteAddressButton")).Click()
        self.modal.Get(self.app.white.SearchCriteria.ByAutomationId("uxOKAddressButton")).Click()
        self.close_group_editor()
