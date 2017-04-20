#!/bin/sh

#REMOTE_HOST='web2.sniperoj.cn'
#REMOTE_PORT='10005'
#X_FORWARDED_FOR='127.0.0.1'
#LOCAL_PORT='23333'
#USER_AGENT='SniperOJ-Web-Broswer'

#echo curl http://${REMOTE_HOST}:${REMOTE_PORT}/ --header "'X-Forwarded-For:${X_FORWARDED_FOR}'" --header "'User-Agent:${USER_AGENT}'" --local-port ${LOCAL_PORT}

#curl http://${REMOTE_HOST}:${REMOTE_PORT}/ --header "'X-Forwarded-For:${X_FORWARDED_FOR}'" --header "'User-Agent:${USER_AGENT}'" --local-port ${LOCAL_PORT}

curl http://web2.sniperoj.cn:10005/ --header 'X-Forwarded-For:127.0.0.1' --header 'User-Agent:SniperOJ-Web-Broswer' --local-port 23333
