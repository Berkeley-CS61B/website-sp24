#!/bin/bash
set -eux

export HOME="${HOME:-"$(echo ~)"}"

deploy_semester() {
	semester="$1"
	ref="$2"

	repo_dir="$HOME/web-repos/$semester"
	public_dir="$HOME/public_html/$semester"

	eval "$("$HOME/.rbenv/bin/rbenv" init - bash)"

	export GIT_SSH_COMMAND="ssh -i '$HOME/web-repos/deploy-keys/$semester'"
	git -C "$repo_dir" fetch --prune
	git -C "$repo_dir" reset --hard "$ref"

	cd "$repo_dir"
	source build.sh

	rsync -rltOvzpog --chmod=D771,F664 --chown=cs188:cs188-staff --delete "$repo_dir/_site/" "$public_dir/"
}

if [[ -z "$1" ]]; then
	echo "Missing semester arg"
fi
if [[ -z "$2" ]]; then
	echo "Missing ref arg"
fi

mkdir -p "$HOME/web-repos/logs"
deploy_semester "$1" "$2" 2>&1 | tee "$HOME/web-repos/logs/$1.log"
