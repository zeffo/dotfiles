# DRY programmers should look away!


function fish_prompt
    set_color $fish_color_mauve
    echo -n "╭─"
    set_color $fish_color_pink
    echo -n ""
    set_color -o --background $fish_color_pink
    set_color $fish_color_crust
    echo -n $USER 
    set_color normal

    set_color --background $fish_color_red
    set_color $fish_color_pink
    echo -n "" 

    set_color --background $fish_color_peach
    set_color $fish_color_red
    echo -n "" 

    set_color --background $fish_color_yellow
    set_color $fish_color_peach
    echo -n "" 

    set_color --background $fish_color_green
    set_color $fish_color_yellow
    echo -n ""

    set_color --background $fish_color_blue
    set_color $fish_color_green
    echo -n ""

    set_color $fish_color_mauve
    set_color --background $fish_color_blue
    echo -n ""

    set_color --background $fish_color_mauve
    set_color $fish_color_base
    echo -n (string replace $HOME '~' (pwd)) 
    set_color normal
    set_color $fish_color_mauve
    echo ""
    set_color $fish_color_base
    set_color $fish_color_mauve
    echo -n "╰─"
    set_color $fish_color_pink
    echo -n "  "

end


