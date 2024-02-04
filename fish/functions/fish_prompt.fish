function fish_prompt
    # set_color $fish_color_lavender
    # echo -n "┌──"
    # # set_color $fish_color_lavender
    # echo -n ""
    # set_color -o --background $fish_color_lavender # f5c2e7
    # set_color $fish_color_crust
    # if set -q SSH_TTY
    #     set_color -o $fish_color_sky # 89dceb
    # end
    # echo -n  $USER 
    # set_color normal
    # set_color $fish_color_lavender
    # echo -n ""
    # set_color $fish_color_mauve 
    # echo -n "─ ─" #      
    # set_color $fish_color_teal 
    # echo (prompt_pwd)
    # set_color $fish_color_lavender
    # # echo "│"
    # echo -n '╰─ '
    # # set_color f5c2e7
    set_color $fish_color_mauve
    echo -n "╭─"
    set_color $fish_color_pink
    echo -n ""
    set_color -o --background $fish_color_pink
    set_color $fish_color_crust
    echo -n $USER
    set_color normal
    set_color --background $fish_color_mauve
    set_color $fish_color_pink
    echo -n " " 
    set_color $fish_color_base
    echo -n (string replace $HOME '~' (pwd)) 
    set_color $fish_color_mauve
    set_color --background $fish_color_red
    echo -n  "" 
    set_color $fish_color_red
    set_color --background $fish_color_peach
    echo -n  "" 
    set_color $fish_color_peach
    set_color --background $fish_color_yellow
    echo -n  "" 
    set_color $fish_color_yellow
    set_color --background $fish_color_green
    echo -n  ""
    set_color $fish_color_green
    set_color --background $fish_color_blue
    echo -n ""
    set_color normal
    set_color $fish_color_blue
    echo ""
    set_color $fish_color_base
    set_color $fish_color_mauve
    echo -n "╰─"
    set_color $fish_color_pink
    echo -n "  "

end


