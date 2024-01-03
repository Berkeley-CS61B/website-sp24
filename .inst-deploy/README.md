# inst-deploy

## Overview

Theoretically, after setup is done, GitHub will notify `https://inst.eecs.berkeley.edu/~cs188/cgi-bin/build-website.cgi?semester=SEMESTER` when you push to the repo. The inst.eecs web server will then update its clone of the repo at `~/web-repos/SEMESTER/` and run the build script for the website, then copy the output to `~/public_html/SEMESTER/`. To avoid external dependencies, this relies on common technology available on the inst.eecs web server as much as possible (and is slightly jank as a result).

## Noteworthy Things

* The inst.eecs web server runs an older version of Ruby by default. To get around this, we use Ruby 2.7 built through `rbenv`.
* Semester-specific build info should go in a Bash-compatible `build.sh` in the root of the semester's repo. `build.example.sh` is provided. It should produce a static site in `_site/`.
* The site currently uses the (deprecated?) GitHub Pages gem, which uses Jekyll 3.
* GitHub webhooks have a 10s timeout. The Jekyll build currently takes longer than that (lol). Possible solutions:
  * Return before the build is completed. The webhook output would no longer reflect the build status (build failures usually happen before 10 seconds).
  * Report status through the GitHub commit status API. This requires someone to setup a GitHub API token.
* There may be a bug where Ruby native packages built outside of the inst.eecs web server fail to load on the web server. I suspect a GLIBC version mismatch. Investigation needed.

## Initial Setup

This only needs to be done once overall.

```bash
mkdir -p ~/public_html/cgi-bin/
chmod 711 ~/public_html/cgi-bin/
cp build-website.cgi ~/public_html/cgi-bin/build-website.cgi
chmod 755 ~/public_html/cgi-bin/build-website.cgi
mkdir -p ~/web-repos/deploy-keys/
chmod 700 ~/web-repos/ ~/web-repos/deploy-keys/
cp build.sh ~/web-repos/build.sh
chmod 700 ~/web-repos/build.sh
nano ~/web-repos/secret.txt # generate a secret

git clone https://github.com/rbenv/rbenv.git ~/.rbenv
git clone https://github.com/rbenv/ruby-build.git "$(~/.rbenv/bin/rbenv root)"/plugins/ruby-build
~/.rbenv/bin/rbenv install 2.7.8
~/.rbenv/bin/rbenv global 2.7.8
```

## Per-semester Setup

Once per semester. Change `sp23` as necessary in the commands below.

```bash
ssh-keygen -t ed25519 -C '' -N '' -f ~/web-repos/deploy-keys/sp23
cat ~/web-repos/deploy-keys/sp23.pub
```

* Add deploy key to https://github.com/BerkeleyAI/sp23-website/settings/keys
* Create a webhook at https://github.com/BerkeleyAI/sp23-website/settings/hooks with:
  * URL: `https://inst.eecs.berkeley.edu/~cs188/cgi-bin/build-website.cgi?semester=sp23`
  * Content-Type: `application/json`
  * Secret: the secret (`cat ~/web-repos/secret.txt`)

```bash
GIT_SSH_COMMAND="ssh -i ~/web-repos/deploy-keys/sp23" git clone git@github.com:BerkeleyAI/sp23-website.git ~/web-repos/sp23/
```
