#/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

SOURCE_DIR="dist"
OUTPUT_FILE="${HOME}/rpmbuild/SOURCES/dist.tar.gz"

cd "$SCRIPT_DIR" || exit 1

if [ -d "$SOURCE_DIR" ]; then
    tar -czf "$OUTPUT_FILE" "$SOURCE_DIR"
    echo "tar: $SCRIPT_DIR/$OUTPUT_FILE"
else
    echo "error: $SOURCE_DIR not found in $SCRIPT_DIR"
    exit 1
fi

spectool -g -R v2ray-plugin.spec

rpmbuild -bs v2ray-plugin.spec
