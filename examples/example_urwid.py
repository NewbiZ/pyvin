#!/usr/bin/env python2

import urwid

def unhandled_input(key):
    if key in ('q', 'Q'):
        application.quit()

class PageSetup(urwid.Overlay):
    def __init__(self):
        self.editKey = urwid.Edit('Key: ')
        self.editTurns = urwid.IntEdit('Maximum turns: ')
        self.editMap = urwid.Edit('Map: ')
        self.buttonOk = urwid.Button('Ok')
        self.buttonCancel = urwid.Button('Cancel')

        urwid.connect_signal(self.buttonOk, 'click', self.validate)
        urwid.connect_signal(self.buttonCancel, 'click', self.cancel)

        super(PageSetup, self).__init__(
                urwid.LineBox(urwid.ListBox(urwid.SimpleFocusListWalker([
                    urwid.Text('GAME SETUP', align='center'),
                    urwid.Divider(),
                    self.editKey,
                    self.editTurns,
                    self.editMap,
                    urwid.Divider(),
                    urwid.Columns([self.buttonOk, self.buttonCancel])
                    ]))),
                urwid.SolidFill(),
                align='center', width=('relative', 20),
                valign='middle', height=('relative', 9),
                min_width=25, min_height=9)

    def validate(self, button):
        application.switchToGame()

    def cancel(self, button):
        application.quit()

class PageGame(urwid.Overlay):
    def __init__(self):
        super(PageGame, self).__init__(
                urwid.LineBox(urwid.ListBox(urwid.SimpleFocusListWalker([
                    urwid.Text('GAME!', align='center'),
                    urwid.Divider(),
                    ]))),
                urwid.SolidFill(),
                align='center', width=('relative', 50),
                valign='middle', height=('relative', 50),
                min_width=50, min_height=50)

class Application(urwid.WidgetPlaceholder):
    def __init__(self):
        super(Application, self).__init__(PageSetup())

    def switchToSetup(self):
        self.original_widget = PageSetup()

    def switchToGame(self):
        self.original_widget = PageGame()

    def quit(self):
        raise urwid.ExitMainLoop()

application = Application()
palette = [('reversed', 'standout', '')]
loop = urwid.MainLoop(application, palette=palette, unhandled_input=unhandled_input)
loop.run()
