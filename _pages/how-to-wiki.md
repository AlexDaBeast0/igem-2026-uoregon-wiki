---
layout: page
permalink: how-to-wiki

title: How to wiki
subtitle: For now, this page demonstrates how to write wiki pages.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---



(note that you don't have to write the title ("How to wiki") here, it's generated automatically; if you want to change the title and subtitle ("For now, this page demonstrates how to write wiki pages."), change them on the Notion. the page hint (that is displayed in the navigation bar on top of the page) can be also changed there.)

The wiki uses markdown (a simple markup language, same as the one used in Notion) for all pages. Please do not embed HTML code directly---I (Fedor) will ignore that and reject your edit. If you want more complex functionality, contact me directly. For consistency, I am trying to keep all pages in this mostly-plain-text style. 

Below, `this font` indicates the literal way you write something before formatting is applied.

# Text formatting:

Three dashes `---` are automatically converted to long---em dashes (please use them when appropriate!). Same with ellipses...

You can write **bold text** by enclosing it in two asterisks: `**bold text**`. *Italic* (one asterisk: `*Italic*`), ***italic bold*** (three asterisks: `***italic bold***`), and ~~strikethrough~~ (two tildes: `~~strikethrough~~`) work similarly. Inline code such as `import pandas as pd` can be done using back-ticks; block code is done with three backticks:
```
import pandas as pd

print("Hello World!")
```

To [link](/uoregon/engineering) to another page on the wiki, use this: `[link text goes here](URL goes here)`. The URL needs to be root-relative, meaning it needs to start with `/uoregon/`: earlier, I used `[link](/uoregon/engineering)`. To link to an [outside page](https://igem.org), use the same format, but with the whole URL: `[outside page](https://igem.org)`.

# Headings:

You can use hashmarks (`#`) to create headings of different size (more hashmarks---smaller header). Please don't use more than three, it doesn't look nice.

# Header 1
## Header 2
### Header 3

↑ was done using:
```
# Header 1
## Header 2
### Header 3
```

# Lists:
- You can make unordered lists.
  - including nesting!
- by putting dashes at the beginning of the line, and indenting for nesting (with two spaces. do not you dare to use the tab character.)
- like this:

```
- You can make unordered lists.
  - including nesting!
- by putting dashes at the beginning of the line, and indenting for nesting (with two spaces. do not you dare to use the tab character.)
- like this:
```

1. Ordered lists
2. work similarly
   1. including indentation

# Figures:

Do not just insert pictures into Notion, I will ignore that.

All non-vector pictures need to go on the iGEM CDN (content delivery network); in the wiki page, you then link to that picture using a special include. See [how to CDN](https://app.notion.com/p/How-to-use-the-iGEM-CDN-3bfd26e796458049b8ebc0a63cf8fc77?source=copy_link)

If a figure can be made in a vector format (.svg), please do so. This especially applies to plots (they should almost always be .svg). Unfortunately, the CDN doesn’t allow for `.svg` files, so we have a different system. To insert a `.svg` (and only a `.svg`), go to the wiki assets folder for the page you’re working on on our [Google Drive](https://drive.google.com/drive/folders/16NgxMysbzJJAic9iknoVxyJD2Rk85pG2), and add it there. Once I upload it to the gitlab, the URL will be of the format `assets/pages/PAGENAME/FIGURENAME.svg` (so put a correctly written URL in the figure include)

Once your picture is in the correct place, you can use this include to add it:

```jsx
{% raw %}{% include figure.html 
    url="URL,_IN_QUOTES"
    caption="CAPTION_GOES_HERE"
    alttext="DESCRIPTION_FOR_PEOPLE_WHO_USE_SCREEN_READERS" 
    label="LABEL"
%}{% endraw %}
```

Replace the ALL_CAPS text with corresponding values. If using the CDN, the URL is the link to the picture; if using a .svg file, the URL is in the format specified above.

If you want to link to this figure somewhere else in the page, use the `fig-ref`  include (below). The `label`s should match for the linking to work. This works like `\label{}` and `\ref{}`  in LaTeX.

```jsx
{% raw %}{% include fig-ref.html 
    label="LABEL"
    text="SOME_TEXT_IN_THE_LINK"
%}{% endraw %}
```

# Citations/bibliography:

On Zotero, there’s a folder called `Wiki_pages`  that has a subfolder for each page (make the subfolder if needed). Put all references for a given page there. Zotero makes a citation key for each reference (eg. `tsuboyamaMegascaleExperimentalAnalysis2023`), that you can see in the sidebar. 

To make an in-text citation, use this include:

```jsx
{% raw %}{% cite CITATION_KEY_GOES_HERE --file PAGE_NAME_GOES_HERE %}{% endraw %}
```

`PAGE_NAME_GOES_HERE` should be replaced with the page name as it’s written in its URL (for example, the Description page has the URL `https://2026.igem.wiki/uoregon/description`, so page name will be `description`)

To add the bibliography, the include is below. Put it at the end of the page.
```
{% raw %}{% bibliography --file PAGE_NAME_GOES_HERE --cited_in_order %}{% endraw %}
```



