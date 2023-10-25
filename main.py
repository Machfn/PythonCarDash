import wx


class DashFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Dash")
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = DashFrame()
    app.MainLoop()

