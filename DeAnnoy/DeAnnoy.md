# DeAnnoy UserCSS
This collection comprises dozens of DeAnnoy UserCSS (UC) for various sites with similar goals.  
Not all UC have all these features and not all are needed for some sites.  
The annoyances targeted by these UC, sorted from the most annoying and most implemented in these UC are:  
- Permanent, sticking elements  
  These include headers with menu, logo or a toolbar, but also buttons - icons. Sometimes, but not as much cookies and similar dialogs asking a confirmation, as those can be more effectively removed with the likes of uBlock origin.
- Interruptions within the Article body  
  "More-ons". Blocks with links to other Articles, site subscription boxes, ... But ADs are not removed.
- Camouflaged ADs and automated re-circulation cards/links  
  The latter are meant to keep a visitor on the site, wasting their time. They rarely have anything common with the Article.
- "Clean Article page - Distractio­n Free"  
  To complement two above points, this Option quite aggressively hides everything not directly related to the article.  
  For those who can't help themselves to click on something interesting, only to later regret the time wasted.
- Width of the main, article body text  
  The Option is mostly included for sites where the content column is too narrow.
- Space saver  
  Anti "modern" and "clean" design. This feature compresses the empty space for better orientation on site, less scrolling, easier jumping over sections of the page.
- "Hide comments"  
  Specially on sites where Comments open up without an interaction. i.e. A button "See comments" is tolerable, but mistakenly seeing someone's witless additions could be annoying.  
  Also this saves space and makes site cleaner for those who do not intent to use/read comments.
- Compress footer  
  Similar to the Space Saver. Shorter footer makes scrolling easier and allows jumping to the end to see e.g. who wrote an article.
- Block menu popup  
  Horrible design idea, where moving with a mouse over a menu will open a sub-menu, sometimes even without a delay. Which will block the content of a page and require a visitor to press Esc or find and click a spot outside of the sub-menu to close it.  
  It is not possible to change "hover" action to "click" action using the CSS. So blocking is usually done only on Article pages. Allowing to still browse the menu on a Home page.
- Hide Pro features  
  Offering buttons and features, if clicking them will instead open log-in screen is annoying.  
  This is "manual" Option, as it would be too complex if possible to detect if a visitor is logged-in and hide these features conditionally. Use it when you never plan to register a site.
- Video player  
  Remove shades and overlying boxes. Sometimes a visitor pauses a video to stop it, as the stop button is usually not present today. But sometimes a video is paused to see a still image.
  Move controls away from the video, when it's not playing in full screen. Why should buttons cover the video, when they can reside below it?
- Shades over videos and pictures
  e.g. when hover. What is the design goal to degrade a picture, when there are other means to mark, outline a selected one?
- Hide paywall  
  This will not circumvent a paywall. Some sites offer a teaser, part of an article for non-paying visitors. This teaser is shaded to make it uncomfortable to read, and/or is longer than what some visitors with e.g. certain screen resolutions can see.  
  This Option will hide the shade and the dialog offering paying options. Instead of it, it will show a small red banner, a notice to warn a visitor they are not seeing the complete article.

- Rearranging elements  
  Mostly to save space. But also to move elements to their expected place and to make the site look more slick.

Those in quotes appear as quoted in the Options. Others have different wording.  
For font type, size and line spacing see the UC from the group *Dark*.  

When all Options are switched off, the UC will do nothing. No CSS is injected into a site and there is no overhaul.  
Options which are ON by default are those which someone looking for a DeAnnoy UC most probably desires.
