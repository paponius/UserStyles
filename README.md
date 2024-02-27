<!-- tesing links in md files  
[Will reload the page but will open md without File tree and jumps to anchor OK](https://github.com/paponius/userstyles/#stylish-boycott)
There could be slash before hash: /userstyles/#stylish-boycott
[this will reload the md file and show File tree](README.md#stylish-boycott)  
[without reload](#stylish-boycott)  
-->

# userstyles
Collection of web styling CSS for use with **Stylus** or similar browser plugin. ([Licence is not Stylish compatible](#stylish-boycott))  
Style files are not located here in GIT, [because of technical limitation.](#git)  
They are now only in USw repository. https://userstyles.world/user/papo  

Description of some of my Styles:  
[BBC](Dark%20BBC/description.md)  

The main problem with _styles_ is, they tend to stop working over time. This is because the site they are made for does change
and the maintainer does not have time to keep updating the style.  

In this set of _styles_ I try to keep a _style_ as simple as possible, not changing every small detail, but only those that matter the most.  
This way I can keep up with fixes to all my _styles_.  
I use these _styles_ myself since 2017, so there is some warranty of continuity.  
I have tens of _styles_ and plan to share majority of them.  

### ADs
A preview image of a Style does not show ADs. But they are still on the site.  
These are color styling Styles.  
We shouldn't mix-in multiple features into one Style.  
Yes, I do use another gimmicks to not just hide ADs, but useless content too, like from Outbrain.  
But as these are crucial for a site support, I will not help or force disabling ADs by mixing them with a Style.

### Features
Dark _Styles_ I use for news media and similar sites have these common features:  
No bright colors. Easy on eyes. No white background, bars or blocks in and around main article.  
High contrast. No dark text on dark background as many _styles_ do, but bright white on nearly black.  
A special color for _visited_ links. Like good old web does by default, so you know what you've already read when another article is referenced in an article.  
Main colors can be changed on all styles in _Configure_ of the _style_.  
Sometimes the header is restyled. Specially if the original is using bright colors.  
#### Resolution
How Styles perform in lower resolutions is not tested for now.  
But there is a plan to support lower widths. Specially if Stylus will be made available in Firefox mobile, or Chrome will allow plugins in mobile browser.  
For now, if it's obvious from original site's CSS that a rule which is being overrid applies only to certain resolution, I try to keep the overridden the same way.

### Minus
The style might not always look very fancy.  
If you go deeper in a site, the styling might not work. e.g. menus, sharing features, featured articles.  
If you find a text which is not readable, e.g. white on white background, or dark on black, report it and I'll fix it,
but I'll not be adding a complete site style overdo.  
I don't use ADs. They are not styled, as I don't see them. I will not be adding add blocker to any of my _styles_. But if there is an AD banner too bright,
you can ask me to _style_ it to a darker version.

### The theme
I use a common _Configure_ header and scheme.  
You can use the _Configure_ in the menu of Stylus to change main colors. That setting will survive most updates.  
Not always are all options in _Configure_ working, because I just copy one over, to ease the maintenance of so many _styles_,
but not always add rules to support all options from the _Configure_. Though the plan is to implement all options in time.  
The background pattern and part of the header code was taken from: https://github.com/StylishThemes  

### Advanced customization
Advanced users could also override variables in :root section of my _styles_, to customize the style even more. To do that, create your own style, use the same @-moz-document
and define just the :root section only with rules you want to override. Then use **Actions > Style Injection Order** in Stylus plugin Options, to place your _style_ above mine.
When site changes and I'll update my _style_, your override rules will still work and you don't have to do anything to keep the site as you like it.  

### Reporting problems
There might be unstyled elements, as I have various site customizing gadgets. Not just AD blocker.  
I try to disable them sporadically to check how the site would look for others. But not always and not thoroughly.  
If you see an element which is particularly intrusive by its brightness, please file an Issue, make a screenshot and add a description.  
If you want, you can make a fix yourself and push a merge. I'll accept, but later will probably edit your edit anyway. So expect that in advance and don't be upset.  

### Stylish boycott
I plan to change this common part, from _USO_ pre-processor to _default_ or _stylus_, to intentionally break compatibility with _Stylish_ plugin.  
Stylish is evil. Spying on users, sending all history, even confidential data to analytics site.  
Breaking rules of content writers and Extension Stores. It should be banned. I will not support it further with my _styles_.  
If you use **Stylish**, change to **Stylus**, you can keep all styles you have and use more sources for even more _styles_.  
Also, the licence of my Styles is not compatible with Stylus plugin. You can't use it legaly in Stylish plugin (while OK in other, like Stylus).  
It is because I use non-commercial licence, CC BY-NC-SA 4.0, and Stylish is making money on exploiting its users and misusing user created content commercially.  

### GIT
My styles are not here in git now.  
You can find them in this _Store_: https://userstyles.world/user/papo  
Use **Issues** here in Github to report a problem.  

If you really really want to fix a _style_, you can commit the whole css file here and I'll manually link it or copy it to USw Store.  
The rules are: Maintain principles mentioned above. Use existing code style. Overload original site css where possible, do not use !important,
do not style insignificant details or not easy reachable page, use variable where appropriate.
To save your time, discuss in _Issues_ section before, to be sure the commit won't be discarded.

I am still trying to find / waiting for a good work-flow solution.  
Maintaining a style could be time demanding as the styled site can change often.  
What I do is, when I see a problem, I'll fix it in Stylus web editor.  
It then offers a way to upload to userstyles.world by a press of a button. But I can't get them here to git auto-magically.  
We can link styles in userstyles.world to git, and they're updated when a style in git updates, but not the other way around.  

