#!/bin/sh

root_dir=$(git rev-parse --show-toplevel)

new_day_number=${1:?"ENTER DAY NUMBER"}

if [ -d "$root_dir/day${new_day_number}" ]; then
  echo "day $new_day_number already exists"
  exit 1
fi

mkdir -p "$root_dir/day${new_day_number}/test"
touch "$root_dir/day${new_day_number}/test/test_day${new_day_number}.py" 
touch "$root_dir/day${new_day_number}/test/real_input.txt" 
touch "$root_dir/day${new_day_number}/test/example_input.txt" 
touch "$root_dir/day${new_day_number}/day${new_day_number}.py" 
