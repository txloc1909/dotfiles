#!/usr/bin/env bash

# Give flatpak apps normal binary names,
# by symlink them to some directory in PATH

SRC_PATH='/var/lib/flatpak/exports/bin'
TARGET_PATH='/usr/local/bin'

symlink_to_path() {
    app_name=$1
    binary_name=$2

    [[ ! -f $SRC_PATH/$app_name ]] && echo $app_name does not exist in $SRC_PATH && return
    [[ -x `command -v $binary_name` ]] && echo $binary_name already exists && return

    echo Symlinking $SRC_PATH/$app_name to $TARGET_PATH/$binary_name
    ln -s $SRC_PATH/$app_name $TARGET_PATH/$binary_name
}

symlink_to_path com.brave.Browser       brave-browser
symlink_to_path com.brave.Browser       brave
symlink_to_path com.discordapp.Discord  discord
symlink_to_path com.skype.Client        skype
symlink_to_path com.slack.Slack         slack
symlink_to_path com.spotify.Client      spotify
symlink_to_path md.obsidian.Obsidian    obsidian
symlink_to_path org.ferdium.Ferdium     ferdium
symlink_to_path org.mozilla.Thunderbird thunderbird
symlink_to_path org.mozilla.firefox     firefox
