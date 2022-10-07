# using pfetch or neofetch as fish_greeting
function fish_greeting
    if command -sq pfetch
        pfetch
    else if command -sq neofetch
        neofetch
    else
        printf $fish_greeting
    end
end
