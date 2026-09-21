# Edit your website

1. Open https://app.pagescms.org and sign in with GitHub.
2. When installing its GitHub App, choose **Only select repositories** and select **chinwayland/waylandchin.com**.
3. Open **waylandchin.com**, branch **main**.
4. Choose **Home**, **About**, **Education**, **Projects**, **Documents**, **Contact**, or an individual **Project** in the sidebar.
5. Edit a heading or use the Word-style text toolbar. Fields follow the order in which content appears on the page. Link destinations are separate from link labels.
6. Save. This publishes your edit after GitHub finishes building the site, normally a few minutes. Refresh https://waylandchin.com to see it.

Use **Site identity & contact** for the shared name, tagline, footer description and contact details. Use **Images** to upload public images and insert them using a text editor's image button.

## Replace your CV or portfolio

In **Public PDFs**, replace the existing file using its existing filename. This keeps every download and PDF reader link working:

- `Wayland_Chin_Academic_CV.pdf`
- `Wayland_Chin_Educational_Innovation_Portfolio.pdf`

Then edit the version and page-count labels under **Documents**. If you use a different filename, update both download and viewer links (and any home-page download link). The viewer URL's `file` parameter must point to the same PDF.

Only upload material intended to be public. This repository and its uploaded files are public. Do not upload contracts, private certificates, student information or institutional files.

## What this editor covers

All 13 existing content pages have editable wording, formatted paragraphs and link destinations. Illustrations keep their layout while their labels can be edited. Creating new page layouts or new project routes still requires a development change. The travel calendar remains managed separately.

## If an edit does not appear

Check https://github.com/chinwayland/waylandchin.com/actions . A failed build keeps the previously deployed site live. GitHub history retains prior versions, so an accidental edit can be reverted. Saving content also rebuilds the travel calendar; a calendar build failure can delay publication.
