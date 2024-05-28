# SubStyle
This is a concept. It is not implemented in Stylus. Maybe authors will like this idea and add it to a new version. Maybe there will be another styles manager which will support it. Maybe I'll make one. For now, jump to (#Workaround).

SubStyle is an user Style dependent on another style.

It is used to additionally modify another Style, without editing it.

To use such Style, a dependency, the super-Style, must also be installed and enabled.

## Why use a SubStyle

Editing a Style would disable automatic updates.
When modding a Style using another Style, the original Style will update if the target site changes
and its authors will fix this super-Style. Chances are the subStyle would still work, or at least not break the site to an unreadable state.

It's more sustainable. Easier to maintain many Styles in a working order.

## Re-sort

Sometimes a subStyle overriding rules from super-Style needs to be applied after the super-Style.
Go to:

Manage > (Style injection order) button right of the Options button >
Put subStyles below their dependency superStyles. Or give subStyle a "star".



