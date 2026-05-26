#!/bin/bash

while true
do
  echo "Starting FFmpeg..."

  ffmpeg \
  -headers $'Referer: https://dookeela.live/\r\nUser-Agent: Mozilla/5.0\r\n' \
  -reconnect 1 \
  -reconnect_streamed 1 \
  -reconnect_at_eof 1 \
  -reconnect_delay_max 10 \
  -rw_timeout 30000000 \
  -timeout 30000000 \
  -i "https://dkl-1.shop/dookeela/truefilm2/chunks.m3u8" \
  -c copy \
  -f null -

  echo "FFmpeg crashed. Restarting in 5 seconds..."
  sleep 5
done
