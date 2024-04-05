#path for  mysql
PATH=$PATH:/usr/local/mysql/bin
export PATH
export TCL_LIBRARY=/usr/local/opt/tcl-tk/lib/tcl8.6
export TK_LIBRARY=/usr/local/opt/tcl-tk/lib/tk8.6

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/muhammedsafuvan/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/muhammedsafuvan/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

