fuck() {
    # reinvoke the last command and save both the command and stderr output
    fc -s -- -1 2>~/.last_stderr.log
    guessed_command=$(python <insert_path_to>thefuck.py ~/.last_stderr.log)
    if [ "$(echo $ZSH_VERSION)" ]; then
        print -z $@
    else
        # assume bash or sh
        bind "\"\e[0n\": \"$guessed_command\""
        printf '\e[5n'
    fi
}
