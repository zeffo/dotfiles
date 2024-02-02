function fish_prompt
    set_color -o f5c2e7
    if set -q SSH_TTY
        set_color -o 89dceb
    end
    echo -n $USER 
    set_color normal
    set_color cba6f7
    echo -n ' @ '
    set_color 94e2d5
    echo (prompt_pwd)
    set_color f5c2e7
    echo '  '
end
