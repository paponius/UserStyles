<!-- testing links in md files
There seems to be no way to open an md page other than the main readme.md in a view without the File tree.
To avoid reload, when just jumping anchors, use only "#anchor".

[Will reload the page but will open md without File tree and jumps to anchor OK](https://github.com/paponius/userstyles/#stylish-boycott)
There could be a slash before hash, or not: /userstyles/#stylish-boycott
[this will reload the md file and show File tree](README.md#stylish-boycott)  
[without reload](#stylish-boycott)  
 -->

# UserStyles
Collection of UserCSS (UC), web styling CSS for use with **Stylus** or similar browser plugins. ([except Stylish](#stylish-boycott))  

There are two types of UserStyles in this collection. Name of one always starts with *Dark*, the other with *DeAnnoy*.  
They work together or independently.  
*Dark* UCs use nearly identical Options and the same selection of colors. Thanks to that it's possible to create a "sub-style" which can change an Option for all 40+ targeted web sites in one step.

*Dark* UserCSSs are completely customizable. They can even be set to black and white only.  
Besides custom colors, they also add some features to a web page content.  
- different color for visited - read article pages
- different color for links to specific article pages and to a general topic pages (which are mostly time waster for a reader re-circulation purpose)
- change of text size, font and space between lines (extra useful on a mobile to have comfortably readable text but not have to swipe around too much)
- different colors for specific elements of a page. e.g. to have a special color for byline helps to quickly find a date of an article page
- color for ADs background, so an AD will not trick a reader to think it's part of the article content

Because of a limitation of a repository, some UserCSS are not accessible from Stylus popup menu and can only be added from the repository. e.g. torrent sites, Radio Free Europe  
[Link to the repository](https://userstyles.world/user/papo)

*DeAnnoy* UserCSSs usually offer an Option to un-stick headers, make article text wider, rearrange or hide objects on a site.  
see: https://github.com/paponius/UserStyles/blob/main/DeAnnoy/DeAnnoy.md

Note, that the look used in a thumbnail preview is just a default setting (3). This can very easily and completely be changed in Options.  
There might be three reasons for a user to seek a change of the usual style of the web page, with black text on white background.  
1. Page is too bright. Hurting the eyes.
2. Page is not clean, uniform.
3. The page is hypnotizing and is hard to keep focus while reading."

Here is an example how Wikipedia would look, for each of these points, with a change in Options done by just a few clicks.  
<img src="https://github.com/user-attachments/assets/10f476c8-2309-412d-b7ad-7839236d69e4" width="33%">
<img src="https://github.com/user-attachments/assets/947b507b-6e26-4ede-893c-690a5676dfa6" width="33%">
<img src="https://github.com/user-attachments/assets/fd1d7a0e-3dd1-4868-9b59-dd88100301f7" width="33%">

Despite the customization, the *Dark* theme must stay "dark". That is lighter text on darker background.  
The reason the primary text color can be changed (from white) is to have less contrasted text if desired. But the text color should remain whitish.  

[m] in the description of a style from this set means it also covers mobile version of a page, and/or various page width. Without the [m] in the description, the result is uncertain.

### Support
If you find a broken page, especially one where text can't be seen, let me know.  
Use [Issue](https://github.com/paponius/UserStyles/issues/new)  
or [Discussion](https://github.com/paponius/UserStyles/discussions/new/choose)  
or Discord: @paponius, DM or maybe on [UserStyles user-chat channel](https://discord.gg/KsbaWj8N)  

This GIT repo is only used for description and feedback/issue tracker for now. It does not contain the actual ...user.css files.  
UserStyle files are in USw repository: https://userstyles.world/user/papo  
That is because of the [incompatible workflow](#git).  

#### Main purpose of these UserStyles
Dark Styles I create are primarily made for the purpose of comfortable reading and fast orientation.  
Color of elements is not removed or made uniform, on the contrary.  
e.g. Links. Special color is used for links to a page section (tags) vs links to a specific article. Color for visited links is added back where the site removes it.  
Separate colors are used for main heading/headline and sub-heading.  
Despite that, if someone prefers "clean" mode, these colors can be made uniform.

[To share, or not to share. Or why and why not.](/description/why.md)

### UserStyle Options
#### Text Primary
Text color of the main content. The body of an article page, text of cards, other significant text.

#### Text Secondary
Less significant text. Something which can be skipped while reading the main content.

#### Text insignificant ("Dark")
Text repeatedly used on all pages. Something a frequent visitor ignores while reading a page.

#### Headline
The headline of an Article page. Also a card can have a headline, but only if there is additional text on such card.

#### Headings
Labels of page sections, also headings within the article.

#### Link color, Visited link color, Link color hover
Links within an Article content.

#### Text lead
"lede" of an article. The first, most significant paragraph of an article.

#### Text deck
"dek" is a more detailed secondary headline of an article.

#### Text byline
The by-line is mentioning the author/source, date and location.

#### Text breadcrumb
On various sites, these are also called Tags, Trending, Sections, ...  
The breadcrumb color is also used on links leading to a breadcrumb. This is handy while reading an article. Link color means there are more details on a specific topic. It leads to a connected article, or external web page. Breadcrumb color on a link means, the linked page only contains articles grouped in the same general topic. This is usually a honey-trap, used to recirculate (recycle) the visitor.

#### Text Primary size, Text Primary line height, Text Primary font
_Primary_ here means the content of an Article page. It's only a subset of Text Primary (color).  
Changing the line height will also change the spacing between paragraphs on some sites.

#### Custom Text Primary font
Only applicable when _Text Primary font_ is set to _Custom_. enter value for ["font-family" property](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family). The default value which can be seen in this Option, is the same as the _Default_ value within the _Text Primary font_ Option.  
For font names including spaces, use double quotes. This will not load a font. Used font must either already be loaded by the web page, or installed in the Operating system. Fonts present within the _Text Primary font_ Option are basically most of all universally available fonts.

#### Styled Quote
Optionally present on some UserStyles. The color is service specific. i.e. Blue border for twitter. This might only be visible if browser is set to not allow external content. Otherwise a twitter tweet would be shown in an iframe from twitter.com, ignoring the blue border option.

#### Background color
There are three types of Background color/pattern used in these US.  
1. `Background`: color or pattern. Used for empty parts of a web page.  
2. `Text background`: color or pattern. Background for the main text of a page. Parts which a visitor spends most time reading.  
3. Section background: Encloses elements of the same group together.  

First two can be fully customized. To a different pattern, a color, or nothing - transparent.  
Section background can't be changed, it's mostly fixed to 30% transparency. In some cases a tint of such group can be changed.  

When _Background_, or _Text background_ is set to _Custom_, the value of the `background` property can be entered in _Custom Background_ and/or _Custom Text Background_.  
[See background property.]([url](https://developer.mozilla.org/en-US/docs/Web/CSS/background))

##### Background image type
When a background is an image. This Option chooses if the image should be shown just once, or the space should be tiled with repeating patters of the background image.

##### Background image attachment
When a background is an image (or a pattern made from an image), should the background scroll with the page content, or stay fixed.
On some (newer) US, for this option if() function is used. This function is today supported only on Chrome. Firefox will ignore this Option.

##### ADs background color
Frame ADs in a color shade. This makes ADs, specially those trying to mimic an article story stick-out. Text on ADs may not be readable with other than white background color (see ADs below).

The practice of using a pattern for page background and text background, instead of a solid color has an important purpose of not hypnotizing the reader. They do help to stay on the line and in focus. The negative effect of solid background and sharp contrast of a text on people reading it is a proofed concept.  

#### Description of some of my Styles:  
[Dark BBC](Dark%20BBC/description.md)  
[Dark Wikipedia](Dark%20Wikipedia/description.md)

The main problem with _styles_ is, they tend to stop working over time. This is because the site they are made for does change
and the maintainer does not have time to keep updating the style.  

In this set of _styles_ I try to keep a _style_ as simple as possible, not changing every small detail, but only those that matter the most.  
This way I can keep up with fixes to all my _styles_.  
I use these _styles_ myself since 2017, so there is some warranty of continuity.  
I have tens of _styles_ and plan to share majority of them.  

### ADs
Standard ADs are not removed by *Dark* and *DeAnnoy* UserCSS.  
For two reasons. I don't want to support general AD removing. And to follow a practice of not combining multiple purposes into one package.  

The exception are annoying and nefarious ADs. Such can be disabled in *DeAnnoy* UC.
I consider annoying ADs to be those sticking on the screen, or hiding page content until dismissed. I try to unstick them, not hide them.  
Nefarious ADs imitate a style of a news article. They look or even say they are relevant to the news article, but they never contain what was promised they would.  
Opening them results in wasted time or even being mislead about some health treatment as they try to pretend they were written by some respected news outlet.  
Sometimes these AD providers mix such ADs with real related stories. In some *DeAnnoy* UC there is an Option to only hide ADs from such blocks, in some only to hide whole more-on sections.

more-on cards not dark-styled or unreadable  
Some cards on moreon sections mentioned above can't be styled. I try to return light BG for them, or just exclude those sections from dark styling, while offering an Option to hide them in *DeAnnoy*.  
As I myself have them disabled, I rarely check if text on them is at least readable, but I would fix an issue with them if reported.

Some ADs might become unreadable.  
*Dark* UserCSS offer Option to highlight ADs by adding a custom background to them. But this might make some poorly coded ADs unreadable.  
Furthermore, in some cases, ADs in an iframe without src will get dark background and white text colors, which also breaks readability of such ADs.  
I don't try to fix these cases. The content provider still gets paid by the AD owner and the AD owner should not have been relying on white BG and black text.

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
All styles using this look-alike theme are located 
Styles using Around 40 indistyles are not here in git now.  
They are for now only in USw repository: https://userstyles.world/user/papo  
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

