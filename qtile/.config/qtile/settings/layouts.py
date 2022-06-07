from libqtile import layout
from libqtile.config import Match


def cmd_zoom(self):
    """dwm's zoom function"""
    curr_win = self.clients.current_client
    main_win = self.clients.focus_first()
    if curr_win == main_win:
        if self.align == self._left:
            self.cmd_swap_right()
        elif self.align == self._right:
            self.cmd_swap_left()
    else:
        self.cmd_swap_main()


def cmd_switch_col(self):
    """dwm's switch_col function"""
    curr_win = self.clients.current_client
    main_win = self.clients.focus_first()
    if curr_win == main_win:
        if self.align == self._left:
            self.cmd_right()
        elif self.align == self._right:
            self.cmd_left()
    else:
        if self.align == self._left:
            self.cmd_left()
        elif self.align == self._right:
            self.cmd_right()


# monkey patch
layout.MonadTall.cmd_zoom = cmd_zoom
layout.MonadTall.cmd_switch_col = cmd_switch_col


layout_theme = {
    "border_width": 4,
    "margin": 4,
    "border_focus": "a6e22e",
    "border_normal": "444444",
}


def init_layouts():
    return [
        layout.MonadTall(
            new_client_position="top",
            ratio=0.55,
            **layout_theme,
        ),
        layout.Columns(
            insert_position=1,
            **layout_theme,
        ),
        layout.Max(**layout_theme),
    ]


def init_floating_layout():
    return layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ]
    )
