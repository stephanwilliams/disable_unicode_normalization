# Disable Unicode Normalization

This addon patches out the `unicodedata.normalize` function that Anki uses to
normalize data, for example, when importing flash cards.

I wrote this plugin to prevent Anki from normalizing certain kanji (e.g.
(隆)[https://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=F9DC]) into
their more common variants (e.g.
(隆)[://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=9686]) when importing
notes. It works for my purposes, but I haven't looked over all the uses of
`unicodedata.normalize` in Anki that this addon patches out, so I would be
cautious using it as it may cause issues elsewhere.

Licensed under the GNU GPL v3.
