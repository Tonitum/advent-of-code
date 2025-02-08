use std::fs;

#[derive(Debug, PartialEq)]
enum GuardDirection {
    NORTH,
    EAST,
    SOUTH,
    WEST,
}

struct Guard {
    position: (i32, i32),
    direction: GuardDirection,
    on_map: bool,
}

impl Guard {
    pub fn new(x: i32, y: i32, direction: GuardDirection) -> Guard {
        Guard {
            position: (x, y),
            direction,
            on_map: true,
        }
    }

    pub fn turn_guard(&mut self) {
        match self.direction {
            GuardDirection::EAST => self.direction = GuardDirection::SOUTH,
            GuardDirection::SOUTH => self.direction = GuardDirection::WEST,
            GuardDirection::WEST => self.direction = GuardDirection::NORTH,
            GuardDirection::NORTH => self.direction = GuardDirection::EAST,
        }
    }

    fn move_north(&mut self) {
        self.position = (self.position.0, self.position.1 - 1);
    }

    fn move_east(&mut self) {
        self.position = (self.position.0 + 1, self.position.1);
    }

    fn move_south(&mut self) {
        self.position = (self.position.0, self.position.1 + 1);
    }

    fn move_west(&mut self) {
        self.position = (self.position.0 - 1, self.position.1);
    }

    fn move_guard(&mut self) {
        match self.direction {
            GuardDirection::EAST => self.move_east(),
            GuardDirection::SOUTH => self.move_south(),
            GuardDirection::WEST => self.move_west(),
            GuardDirection::NORTH => self.move_north(),
        }
    }

    pub fn patrol(
        &mut self,
        current_line: &String,
        line_above: Option<&String>,
        line_below: Option<&String>,
    ) {
        match self.direction {
            GuardDirection::EAST => {
                if self.position.0 + 1 >= current_line.len().try_into().unwrap() {
                    // we'll move past the map with this move
                    self.on_map = false;
                    return;
                }
                // check if there is a blockage. if there is, turn and then move
                if current_line
                    .chars()
                    .nth((self.position.0 + 1).try_into().unwrap())
                    .unwrap()
                    == '#'
                {
                    self.turn_guard();
                }
                self.move_guard();
            }
            GuardDirection::SOUTH => {
                if line_below.is_none() {
                    // we'll move past the map with this move
                    self.on_map = false;
                    return;
                }
                if line_below
                    .unwrap()
                    .chars()
                    .nth((self.position.0).try_into().unwrap())
                    .unwrap()
                    == '#'
                {
                    self.turn_guard();
                }
                self.move_guard();
            }
            GuardDirection::WEST => {
                if self.position.0 == 0 {
                    // we'll move past the map with this move
                    self.on_map = false;
                    return;
                }
                // check if there is a blockage. if there is, turn and then move
                if current_line
                    .chars()
                    .nth((self.position.0 - 1).try_into().unwrap())
                    .unwrap()
                    == '#'
                {
                    self.turn_guard();
                }
                self.move_guard();
            }
            GuardDirection::NORTH => {
                if line_above.is_none() {
                    // we'll move past the map with this move
                    self.on_map = false;
                    return;
                }
                if line_above
                    .unwrap()
                    .chars()
                    .nth((self.position.0).try_into().unwrap())
                    .unwrap()
                    == '#'
                {
                    self.turn_guard();
                }
                self.move_guard();
            }
        }
    }
}

fn load_input(filepath: &String) -> Vec<String> {
    let contents = fs::read_to_string(filepath).expect("Could not read file");
    let contents_split: Vec<String> = contents.split("\n").map(|line| line.to_string()).collect();
    return contents_split;
}

fn find_guard(lines: &Vec<String>) -> Option<Guard> {
    // iterate through the lines to find the starting position
    for y in 0..lines.len() {
        let line = lines.get(y).unwrap();
        for x in 0..line.len() {
            if line.chars().nth(x).unwrap() == '^' {
                return Some(Guard::new(
                    x.try_into().unwrap(),
                    y.try_into().unwrap(),
                    GuardDirection::NORTH,
                ));
            }
            if line.chars().nth(x).unwrap() == '>' {
                return Some(Guard::new(
                    x.try_into().unwrap(),
                    y.try_into().unwrap(),
                    GuardDirection::EAST,
                ));
            }
            if line.chars().nth(x).unwrap() == 'V' {
                return Some(Guard::new(
                    x.try_into().unwrap(),
                    y.try_into().unwrap(),
                    GuardDirection::SOUTH,
                ));
            }
            if line.chars().nth(x).unwrap() == '<' {
                return Some(Guard::new(
                    x.try_into().unwrap(),
                    y.try_into().unwrap(),
                    GuardDirection::WEST,
                ));
            }
        }
    }
    None
}

fn trace_guard_path(guard: Guard, lines: &Vec<String>) -> i32 {
    return 0;
}

fn find_guard_path(lines: &Vec<String>) -> i32 {
    return 0;
}

fn main() {
    // load the input
    // split the lines into arrays
    // find where the guard starting position is
    // move the guard, adding spaces to a vector
    //      move guard forward
    //      when encouter edge of map, end movement
    //      when encounter obstacle, turn direction right
    //      repeat
    // find count of unique spaces in list
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_turn_guard() {
        let mut guard = Guard::new(0, 0, GuardDirection::NORTH);
        guard.turn_guard();
        assert_eq!(guard.direction, GuardDirection::EAST);
        guard.turn_guard();
        assert_eq!(guard.direction, GuardDirection::SOUTH);
        guard.turn_guard();
        assert_eq!(guard.direction, GuardDirection::WEST);
        guard.turn_guard();
        assert_eq!(guard.direction, GuardDirection::NORTH);
    }

    #[test]
    fn test_find_guard_north() {
        let lines: Vec<String> = Vec::from([
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "....^.....".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
        ]);
        let guard = find_guard(&lines).unwrap();
        assert_eq!(guard.direction, GuardDirection::NORTH);
        assert_eq!(guard.position, (4, 6));
    }

    #[test]
    fn test_find_guard_east() {
        let lines: Vec<String> = Vec::from([
            "..........".to_string(),
            "..........".to_string(),
            "......>...".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
        ]);
        let guard = find_guard(&lines).unwrap();
        assert_eq!(guard.direction, GuardDirection::EAST);
        assert_eq!(guard.position, (6, 2));
    }

    #[test]
    fn test_find_guard_south() {
        let lines: Vec<String> = Vec::from([
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            ".V........".to_string(),
            "..........".to_string(),
        ]);
        let guard = find_guard(&lines).unwrap();
        assert_eq!(guard.direction, GuardDirection::SOUTH);
        assert_eq!(guard.position, (1, 8));
    }

    #[test]
    fn test_find_guard_west() {
        let lines: Vec<String> = Vec::from([
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            ".........<".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
        ]);
        let guard = find_guard(&lines).unwrap();
        assert_eq!(guard.direction, GuardDirection::WEST);
        assert_eq!(guard.position, (9, 5));
    }

    #[test]
    fn test_find_guard_none() {
        let lines: Vec<String> = Vec::from([
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
        ]);
        let guard = find_guard(&lines);
        assert_eq!(true, guard.is_none());
    }

    #[test]
    fn test_move_guard_north() {
        let lines: Vec<String> = Vec::from([
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            "..........".to_string(),
            ".....^....".to_string(),
        ]);
        let mut guard = find_guard(&lines).unwrap();
        guard.patrol(
            &lines.get(guard.position.1 as usize).unwrap(),
            Some(lines.get((guard.position.1 - 1) as usize).unwrap()),
            None,
        );
        assert_eq!(guard.position, (5, 8));

        while guard.on_map {
            guard.patrol(
                &lines.get(guard.position.1 as usize).unwrap(),
                lines.get((guard.position.1 - 1) as usize),
                lines.get((guard.position.1 + 1) as usize),
            );
        }
        assert_eq!(guard.position, (5, 0));
    }

    #[test]
    fn test_move_guard_east() {
        let lines: Vec<String> = Vec::from([
            "..........".to_string(),
            ">.........".to_string(),
            "..........".to_string(),
        ]);
        let mut guard = find_guard(&lines).unwrap();
        guard.patrol(
            &lines.get(guard.position.1 as usize).unwrap(),
            Some(lines.get((guard.position.1 - 1) as usize).unwrap()),
            None,
        );
        assert_eq!(guard.position, (1, 1));

        while guard.on_map {
            guard.patrol(
                &lines.get(guard.position.1 as usize).unwrap(),
                lines.get((guard.position.1 - 1) as usize),
                lines.get((guard.position.1 + 1) as usize),
            );
        }
        assert_eq!(guard.position, (9, 1));
    }
}
