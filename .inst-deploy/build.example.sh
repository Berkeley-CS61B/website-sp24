#!/bin/bash
set -eux

bundle install
bundle exec jekyll build --destination _site/
