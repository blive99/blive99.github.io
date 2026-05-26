#!/bin/bash

while true
do
    echo "Starting stream..."

    ffmpeg \
    -loglevel error \
    -reconnect 1 \
    -reconnect_streamed 1 \
    -reconnect_at_eof 1 \
    -reconnect_delay_max 10 \
    -rw_timeout 15000000 \
    -user_agent "Mozilla/5.0" \
    -i "https://dkl-1.shop/dookeela/truefilm2/chunks.m3u8" \
    -c copy \
    -f flv \
    "rtmp://YOUR_SERVER/live/streamkey"

    echo "Stream disconnected! Reconnecting in 5 seconds..."
    sleep 5
done
