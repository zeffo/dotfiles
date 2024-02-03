function fish_prompt
    set_color $fish_color_lavender
    echo -n "┌── "
    set_color -o $fish_color_pink # f5c2e7
    if set -q SSH_TTY
        set_color -o $fish_color_sky # 89dceb
    end
    echo -n $USER 
    set_color normal
    set_color $fish_color_mauve 
    echo -n "   " #      
    set_color $fish_color_teal 
    echo (prompt_pwd)
    set_color $fish_color_lavender
    echo -n '╰─ '
    # set_color f5c2e7
end


