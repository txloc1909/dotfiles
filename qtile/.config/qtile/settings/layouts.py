from libqtile import layout
from libqtile.config import Match

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
