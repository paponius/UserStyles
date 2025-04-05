When using this style, the recommended setting on the Wikipedia page is the *day mode*.  
Night mode is an attempt by Wikipedia to fix the oversight when Wikipedia was designed without Day/Night switch functionality.  
It does some horrific things. Shading all pictures, removing color backgrounds, sometimes crucial for context, adding some generic rules with !important, which use to break this UserStyle.

# Collaboration
Help is appreciated,  
- Use *Issues*: the URL and either a screenshot with the part with an issue marked, or some sort of description.  
- *Discussions* if the problem doesn't fit into *Issues*  
- paponius@discord
- Fix it yourself. Copy the CSS to this directory, follow the approach used in the file.  
  Do not change/add bigger parts without starting a *Discussion*.  
  Do not just add an overruling ruleset somewhere. There is a system. (in most parts)  
  No !important where not necessary, also specificity at the minimum required.  

# Wikipedia Limitation
There will be some unreadable parts. Use mouse to select such parts to read them.  

If it's an issue repeating itself on multiple pages, report it here.  
Wikipedia differs from a common web site in it's being from technical perspective basically a web hosting service.  
Every page is made by different authors and they are allowed to use any colors they desire.  
This is multiplied by all languages the page is available in, where translating authors often chooses yet another color.  
This is why there must be a compromise between total dark customization and preservation of shade and color variety for various elements on a page.  

It is not feasible to make Wikipedia 100% dark and without issues.  
- From maintenance-time perspective
- For practical reason of the Style file being tens or hundred(?) MB in size if all variations of colors are covered.

Though there are ways:  
- Using a script, which would calculate lightness-inverted colors, changing both BG and text colors to keep some contrast.
- Changing all text background colors to dark. This method is used by the other UserStyle. Also the attempt by Wikipedia itself for a dark mode does this in part.  
  Big problem here is, sometimes the information context on a page is represented by the color. e.g. A table with different BG colors for different data. Be that all unicolor dark, the information is lost.  

Often wiki pages use a template. In a template the style is more predictable and so pages which use them can be styled safely.  
But there are still hundreds of templates, and they can be edited and changed too.  
Moreover, a template can be very different for different languages.  

Some elements do use class names. More are added recently. But for some reason these are localized! This is worse than nothing.

So a style for Wikipedia, using only CSS will never be perfect.  
Most styles, or all of them, will just change a table heading and data entry to certain color.  
In this Userstyle, I try to style templates I encounter, keeping a difference in coloring. Colors are lightness-reversed.

Still there are issues, where colors are reversed in a table this way. There might be a description, a cheatsheet, showing what data each color represents.
But color symbols in this chart are not re-styled. So e.g. it will show that light-blue represents rivers, but in table the color is dark blue.  
