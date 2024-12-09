struct Rules {
    set: Vec<u32>,
}

impl Rules {
    fn new(set: Vec<u32>) -> Self {
        Self { set }
    }
}

struct Change {
    rules: &Rules,
    changes: Vec<u32>
}

impl Change {
    fn new(rules: &Rules, change_string: String) -> Self {
        let changes: Vec<u32> = change_string.split(",").map(|c| { c.parse::<u32>().unwrap()}).collect();

        Self {rules: rules, changes }
    }

    fn is_sorted(&self) -> bool {
        return false;
    }

    fn sort(&mut self) {
        self.changes.sort();
    }

    fn middle(&self) -> u32 {
        return *self.changes.get(self.changes.len() / 2).unwrap();
    }
}

fn load_lines(filepath: &String) -> (Vec<u32>, Vec<String>) {
}

fn load_changes(filepath: &String) -> Vec<Change> {
    let changes: Vec<Change> = Vec::new();
    let (rules_line, change_lines) = load_lines(filepath);
    let rules = Rules::new(rules_line);
    for change_line in change_lines {
        changes.push(Change::new(&rules, change_line));
    }
    return changes;
}

fn main() {
    // load the input
    let changes = load_changes();
    let mut valid_middle_item_sum = 0;
    for change in changes {
        if change.is_sorted() {
            valid_middle_item_sum += change.middle();
        }
    }
    println!("{}", valid_middle_item_sum);
}
