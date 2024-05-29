#!/bin/bash

socat TCP-LISTEN:8892,reuseaddr,fork EXEC:./request_handler.sh