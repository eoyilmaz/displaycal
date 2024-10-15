# -*- coding: utf-8 -*-

# import comtypes.gen.TaskbarLib as tbl
import comtypes.client as cc
cc.GetModule("TaskbarLib.tlb")
import comtypes.gen.TaskbarLib as tbl


TBPF_NOPROGRESS = 0
TBPF_INDETERMINATE = 0x1
TBPF_NORMAL = 0x2
TBPF_ERROR = 0x4
TBPF_PAUSED = 0x8

taskbar = cc.CreateObject(
    "{56FDF344-FD6D-11d0-958A-006097C9A090}", interface=tbl.ITaskbarList3
)
taskbar.HrInit()


class Taskbar(object):
    def __init__(self, frame, maxv=100):
        self.frame = frame
        self.maxv = maxv

    def set_progress_value(self, value):
        if self.frame:
            taskbar.SetProgressValue(self.frame.GetHandle(), value, self.maxv)

    def set_progress_state(self, state):
        if self.frame:
            taskbar.SetProgressState(self.frame.GetHandle(), state)
