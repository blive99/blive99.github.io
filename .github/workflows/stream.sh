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
    -f hls \
-hls_time 5 \
-hls_list_size 10 \
-hls_flags delete_segments+append_list \
output.m3u8

    echo "Stream disconnected! Reconnecting in 5 seconds..."
    sleep 5
done
