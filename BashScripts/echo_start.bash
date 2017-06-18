#!/bin/bash

# IDE completion

echo "hi." || echo "This won't happen"
$(ls nonexistentfile) || "This will happen"
echo $(pwd) && echo "This ALSO will happen"
