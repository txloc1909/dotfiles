local home = os.getenv("HOME")

local _M = {
	terminal = "kitty",
	modkey = "Mod1",
	editor = "vim",
	wallpaper = "~/.local/share/backgrounds/wallpaper.png",
	dmenu = "rofi -show run",
	youtube = "brave --app=https://youtube.com",
	facebook = "brave --app=https://facebook.com",
	reddit = "brave --app=https://reddit.com",
	notion = "chromium --app=https://notion.so",
}

return _M
