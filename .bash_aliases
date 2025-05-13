alias ..="cd .."
alias ...="cd ../.."
alias lsa="ls -a"

alias venv="source .venv/bin/activate"
alias .venv="source ../.venv/bin/activate"
alias mkvenv="python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"

alias gpull="git pull"
alias gs="git fetch && git status -bs"
alias glog="git log --oneline --graph --decorate --all"

alias py="python3"

alias editautostart="sudo nano /etc/xdg/lxsession/LXDE-pi/autostart"
alias karusell="python3 ~/Desktop/infoskjerm-karusell/infoskjerm_karusell.py"
