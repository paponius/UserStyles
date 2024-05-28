# SubStyle
> This is a concept. It is not implemented in Stylus. Maybe authors will like this idea and add it to a new version. Maybe there will be another styles manager which will support it. Maybe I'll make one. For now, jump to [Workaround](#Workaround).

SubStyle is an user Style dependent on another style.

It is used to additionally modify another Style, without editing it.

## Why use a SubStyle

Editing a Style would disable automatic updates.

Authors of the SubUserStyle can limit the workload of keeping their's Style up to date by only managing their part of the script.

When a site for which the UserStlye is made will change and brake the UserStyle, author of the SubUserStyle can just wait for the authors of the SuperUserStyle to fix it.

If this idea was implemented and used, there only need to be one SuperUserStyle for each web site to color style it to any look. It will define all stylable elements using style variables. SubUserStyle will change values of those variables, optionally add more features.

It's more sustainable. Easier to maintain many Styles in a working order.

## Workaround
As there is no style manager supporting this, manual steps need to be done.  
To use a SubUserStyle, a dependency, the super-Style, must also be installed and enabled.

### Re-sort

Sometimes a SubStyle overriding rules from super-Style needs to be applied after the super-Style.
Go to:

Manage > (Style injection order) button right of the Options button >
Put subStyles below their dependency superStyles. Or give subStyle a "star".



