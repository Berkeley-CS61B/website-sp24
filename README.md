# CS 61B Staff Website

New course website for FA22 developed by Peyrin (ping on Slack in the `#61b-new-website-fa23` channel if there are any problems).


## Updating assignments

- Instructions for uploading discussion worksheets are in `_data/discussions.yml`.
- Instructions for releasing homeworks are in `_data/homeworks.yml`.
- Instructions for releasing projects are in `_data/projects.yml`.


## Building website

To update the website, just push to this repo, and the website will automatically build and update in around a minute. To keep the repo clean, **please tag your commit messages** by adding an assignment tag at the beginning. Examples:
- `[disc02] release`
- `[hw02] add electronic hw`
- `[proj1] fix typo in spec`

To build the website locally, [install Jekyll](https://jekyllrb.com/docs/installation/) and run `bundle exec jekyll serve`.