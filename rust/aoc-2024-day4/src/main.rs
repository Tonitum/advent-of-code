use std::fs;

fn load_input(filepath: &String) -> Vec<String> {
    let contents = fs::read_to_string(filepath).expect("Could not read file");
    let contents_split: Vec<String> = contents.split("\n").map(|line| line.to_string()).collect();
    return contents_split;
}

fn get_x_mas_count(lines: &Vec<String>, x: &usize, y: &usize) -> i32 {
    // looking for x-mas
    // M . S
    // . A .
    // M . S
    // M . M
    // . A .
    // S . S
    // S . M
    // . A .
    // S . M
    // S . S
    // . A .
    // M . M
    let line_length = &lines[*x].len();
    let mut match_count = 0;
    println!("Checking {}, {}", &x,&y);
    if !(0 < *y && *y < line_length - 1) {
        println!("Skipping, in first or last column");
        return 0;
    }
    if !(0 < *x && *x < lines.len()) {
        println!("Skipping, in first or last row");
        return 0;
    }
    println!("Position is safe to check");

    let top_chars = [
        lines[x - 1].chars().nth(y - 1).unwrap(),
        lines[x - 1].chars().nth(y + 1).unwrap(),
    ];
    let bottom_chars = [
        lines[x + 1].chars().nth(y - 1).unwrap(),
        lines[x + 1].chars().nth(y + 1).unwrap(),
    ];
    if top_chars == ['M', 'S'] && bottom_chars == ['M', 'S'] {
        match_count += 1;
        return match_count;
    }
    if top_chars == ['M', 'M'] && bottom_chars == ['S', 'S'] {
        match_count += 1;
        return match_count;
    }
    if top_chars == ['S', 'M'] && bottom_chars == ['S', 'M'] {
        match_count += 1;
        return match_count;
    }
    if top_chars == ['S', 'S'] && bottom_chars == ['M', 'M'] {
        match_count += 1;
        return match_count;
    }
    return match_count;
}

fn get_matching_count(lines: &Vec<String>, x: &usize, y: &usize) -> i32 {
    let line_length = &lines[*x].len();
    let mut match_count = 0;
    // Left: [0,1], [0,2], [0,3]
    // Diagonal Down Left: [1,1], [2,2], [3,3]
    // Diagonal Up Left: [-1,1], [-2,2], [-3,3]
    if *y < (line_length - 3) {
        // println!("\tCan Check Left");
        // if there are at least 3 lines below, we can check them
        if *x < lines.len() - 4 {
            let chars = [
                lines[x + 1].chars().nth(y + 1).unwrap(),
                lines[x + 2].chars().nth(y + 2).unwrap(),
                lines[x + 3].chars().nth(y + 3).unwrap(),
            ];

            if chars == ['M', 'A', 'S'] {
                println!("\tFound Match Diagonal Down Right");
                println!("\tMatch at: {},{}", x, y);
                match_count += 1;
            }
        }
        // if 3 lines above, check left diagonal
        if *x >= 3 {
            let chars = [
                lines[x - 1].chars().nth(y + 1).unwrap(),
                lines[x - 2].chars().nth(y + 2).unwrap(),
                lines[x - 3].chars().nth(y + 3).unwrap(),
            ];

            if chars == ['M', 'A', 'S'] {
                println!("\tFound Match Diagonal Up Right");
                println!("\tMatch at: {},{}", x, y);
                match_count += 1;
            }
        }
        // check straight right
        let chars = [
            lines[*x].chars().nth(y + 1).unwrap(),
            lines[*x].chars().nth(y + 2).unwrap(),
            lines[*x].chars().nth(y + 3).unwrap(),
        ];

        if chars == ['M', 'A', 'S'] {
            println!("\tFound Match Straight Right");
            println!("\tMatch at: {},{}", x, y);
            match_count += 1;
        }
    }
    // Diagonal Down Right: [1,-1], [2,-2], [3,-3]
    // Diagonal Up Right: [-1,-1], [-2,-2], [-3,-3]
    // Right: [0,-1], [0,-2], [0,-3]
    if *y >= 3 {
        if *x < lines.len() - 4 {
            let chars = [
                lines[x + 1].chars().nth(y - 1).unwrap(),
                lines[x + 2].chars().nth(y - 2).unwrap(),
                lines[x + 3].chars().nth(y - 3).unwrap(),
            ];

            if chars == ['M', 'A', 'S'] {
                println!("\tFound Match Diagonal Down Left");
                println!("\tMatch at: {},{}", x, y);
                match_count += 1;
            }
        }
        // if 3 lines above, check left diagonal
        if *x >= 3 {
            let chars = [
                lines[x - 1].chars().nth(y - 1).unwrap(),
                lines[x - 2].chars().nth(y - 2).unwrap(),
                lines[x - 3].chars().nth(y - 3).unwrap(),
            ];

            if chars == ['M', 'A', 'S'] {
                println!("\tFound Match Diagonal Up Left");
                println!("\tMatch at: {},{}", x, y);
                match_count += 1;
            }
        }
        // check straight left
        // if 3 lines below, check left diagonal
        let chars = [
            lines[*x].chars().nth(y - 1).unwrap(),
            lines[*x].chars().nth(y - 2).unwrap(),
            lines[*x].chars().nth(y - 3).unwrap(),
        ];

        if chars == ['M', 'A', 'S'] {
            println!("\tFound Match Straight Left");
            println!("\tMatch at: {},{}", x, y);
            match_count += 1;
        }
    }
    // Down: [1,0], [2,0], [3,0]
    if *x < lines.len() - 4 {
        let chars = [
            lines[x + 1].chars().nth(*y).unwrap(),
            lines[x + 2].chars().nth(*y).unwrap(),
            lines[x + 3].chars().nth(*y).unwrap(),
        ];

        if chars == ['M', 'A', 'S'] {
            println!("\tFound Match Straight Down");
            println!("\tMatch at: {},{}", x, y);
            match_count += 1;
        }
    }
    // Up: [-1,0], [-2,0], [-3,0]
    if *x >= 3 {
        let chars = [
            lines[x - 1].chars().nth(*y).unwrap(),
            lines[x - 2].chars().nth(*y).unwrap(),
            lines[x - 3].chars().nth(*y).unwrap(),
        ];

        if chars == ['M', 'A', 'S'] {
            println!("\tFound Match Straight Up");
            println!("\tMatch at: {},{}", x, y);
            match_count += 1;
        }
    }
    return match_count;
}

fn find_all_xmas_pt1(input: &Vec<String>) -> i32 {
    let x_dimension = input.len() - 1;
    // assumes all lines are the same length
    let y_dimension = input[0].len();
    let mut xmas_count = 0;
    for x in 0..x_dimension {
        for y in 0..y_dimension {
            let line = &input[x];
            if line.chars().nth(y).unwrap() == 'X' {
                xmas_count += get_matching_count(&input, &x, &y);
                println!("-----------");
            }
        }
    }
    return xmas_count;
}

fn find_all_xmas_pt2(input: &Vec<String>) -> i32 {
    let x_dimension = input.len() - 2;
    // assumes all lines are the same length
    let y_dimension = input[0].len();
    let mut xmas_count = 0;
    for x in 1..x_dimension {
        for y in 0..y_dimension {
            let line = &input[x];
            if line.chars().nth(y).unwrap() == 'A' {
                xmas_count += get_x_mas_count(&input, &x, &y);
            }
        }
    }
    return xmas_count;
}

fn main() {
    let input = load_input(&"./src/input.txt".to_string());
    let res = find_all_xmas_pt2(&input);
    println!("Result: {}", res);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_xmas_simple1() {
        let input = load_input(&"./src/example_input_1.txt".to_string());
        let res = find_all_xmas_pt1(&input);
        assert_eq!(res, 4);
    }
    #[test]
    fn test_find_xmas_simple2() {
        let input = load_input(&"./src/example_input_2.txt".to_string());
        let res = find_all_xmas_pt1(&input);
        assert_eq!(res, 18);
    }
    #[test]
    fn test_find_x_mas_1() {
        let input = load_input(&"./src/example_input_2.txt".to_string());
        let res = find_all_xmas_pt2(&input);
        assert_eq!(res, 9);
    }
}
