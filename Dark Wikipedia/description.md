# Limitation
Wikipedia pages are different from a web site using a common style scheme.  
It's quite difficult to modify colors and keep the shade variety for various elements on a page.  
Often wiki pages use a template. In a template the style is expectable and so pages which uses them can be styled quite safely.  
But there are dozens or hundrets of templates, and they can be edited too.  
A template can be very different for different language mutation.  
And then there are pages which do not use a template, but define a style inline. (in wiki source) Those are quite impossible to style.  

So a style for Wikipedia, using only CSS will never be perfect.  
Most styles, or all of them, will just change a table heading and data entry to certain color.  
In this Userstyle, I try to style templates I encounter, keeping a difference in coloring. Colors are lightness-reversed.

Still there are issues, where colors are reversed in a table this way. There might be a description, a cheatsheet, showing what data each color represents.
But color symbols in this chart are not re-styled. So e.g. it will show that light-blue represents rivers, but in table the color is dark blue.  

But the worst are the custom themed wiki pages. As each is like an individual web page.  
The practice I implemented is to keep 2/3 of red-darker toned colors, assuming overall the color will be darker (not always).
And all brighter colors are replaced by a corresponding darker B/W shade. In 6 different shades.
Specifically, All colors starting with #A....., #B....., ..., $F..... are replaced by #333, #555, ...  
Not perfect at all. But on most wiki pages this will at least show a difference between those colors. Unlike in other Userstyles, where all colors are styled to one dark shade.

With this in mind, let me know if there is unreadable text on certain wiki page. Or an important color shade not distinguished from other, using _Issues_.

