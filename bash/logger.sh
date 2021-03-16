# Start logging for every session:
test "$(ps -ocommand= -p $PPID | awk '{print $1}')" == 'script' || (script -f /media/sf_virtualbox_transfer/terminator_$(date +"%Y%m%d_%H%M%S").log)
