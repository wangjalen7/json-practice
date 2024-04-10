#!/bin/bash

METAR_DATA=$(curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40,-90,45,-85")

echo "$METAR_DATA" | jq -r '.[].receiptTime' | head -n 6
