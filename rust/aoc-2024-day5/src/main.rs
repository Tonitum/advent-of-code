use std::{collections::HashMap, fs, net::SocketAddr};

const _EXAMPLE_FILE_NAME: &str = "./src/example_input_1.txt";
const _INPUT_FILE_NAME: &str = "./src/input.txt";

fn load_input(filepath: &str) -> (Vec<String>, Vec<String>) {
    let contents = fs::read_to_string(filepath).expect("Could not read file");
    let contents_split: Vec<String> = contents.split("\n").map(|line| line.to_string()).collect();
    let mut rules_lines: Vec<String> = Vec::new();
    let mut pages_lines: Vec<String> = Vec::new();

    let mut setting_rules: bool = true;
    for line in contents_split {
        if line == "" {
            setting_rules = false;
        }
        if setting_rules {
            rules_lines.push(line);
            continue;
        }
        pages_lines.push(line);
    }

    return (rules_lines, pages_lines);
}

fn create_rules(rules_lines: &Vec<String>) -> HashMap<u32, Vec<u32>> {
    let mut rules_set: HashMap<u32, Vec<u32>> = HashMap::new();
    for line in rules_lines {
        // split the rules by the |
        let parts: Vec<u32> = line
            .split("|")
            .map(|c| c.parse::<u32>().expect("failed to parse int in rules"))
            .collect();
        if !rules_set.contains_key(&parts[0]) {
            rules_set.insert(parts[0], [parts[1]].to_vec());
            continue;
        }
        rules_set.get_mut(&parts[0]).unwrap().push(parts[1]);
    }
    return rules_set;
}

fn create_page_sets(pages_lines: &Vec<String>) -> Vec<Vec<u32>> {
    let mut page_sets: Vec<Vec<u32>> = Vec::new();
    for page_set in pages_lines {
        if page_set == "" {
            continue;
        }
        let pages: Vec<u32> = page_set
            .split(",")
            .map(|page| page.parse::<u32>().expect("faile to parse int in pages"))
            .collect();
        page_sets.push(pages);
    }
    return page_sets;
}

fn is_page_set_ordered(pages: &Vec<u32>, rules: &HashMap<u32, Vec<u32>>) -> bool {
    for i in 0..pages.len() {
        if !rules.contains_key(&pages[i]) {
            // if the page in the pageset doesn't have rules, it doesn't matter what order it's in
            continue;
        }
        let page_order_rules = rules.get(&pages[i]).expect("failed to load page rules");
        for j in 0..i {
            if page_order_rules.contains(&pages[j]) {
                return false;
            }
        }
    }
    return true;
}

fn check_page_sets(pages: &Vec<Vec<u32>>, rules: &HashMap<u32, Vec<u32>>) -> u32 {
    let mut mid_value_sum = 0;
    for page_set in pages {
        if is_page_set_ordered(page_set, rules) {
            mid_value_sum += page_set.get(page_set.len() / 2).unwrap();
        }
    }
    return mid_value_sum;
}

fn find_candidate(page_set: &Vec<u32>, rules: &HashMap<u32, Vec<u32>>) -> Option<usize> {
    for i in 0..page_set.len() {
        let candidate = *page_set.get(i).unwrap();
        let mut has_pointers = false;
        // println!("\t\tCandidate: {}", candidate);
        for ruleset in rules.keys() {
            if candidate == *ruleset {
                continue;
            }
            // println!("\t\tRules: {:?}", rules.get(ruleset));
            if rules.get(ruleset).unwrap().contains(&candidate) {
                has_pointers = true;
            }
        }
        if !has_pointers {
            return Some(i);
        }
    }
    None
}

fn order_page_set(page_set: &Vec<u32>, rules: &HashMap<u32, Vec<u32>>) -> u32 {
    // we only care about some of the rules
    let mut applicable_rules: HashMap<u32, Vec<u32>> = HashMap::new();
    for page in page_set {
        let ruleset = rules.get(page);
        if !ruleset.is_some() {
            continue;
        }
        applicable_rules.insert(*page, ruleset.unwrap().to_vec());
    }
    let mut pages = page_set.clone();
    let mut sorted_pages: Vec<u32> = Vec::new();
    while sorted_pages.len() < page_set.len() {
        let candidate = find_candidate(&pages, &applicable_rules);
        if candidate.is_none() {
            break;
        }
        sorted_pages.push(*pages.get(candidate.unwrap()).unwrap());
        applicable_rules.remove(pages.get(candidate.unwrap()).unwrap());
        pages.remove(candidate.unwrap());
    }
    return *sorted_pages
        .get(sorted_pages.len() / 2)
        .unwrap();
}

fn sort_and_check_page_sets(pages: &Vec<Vec<u32>>, rules: &HashMap<u32, Vec<u32>>) -> u32 {
    let mut mid_value_sum = 0;
    for page_set in pages {
        if is_page_set_ordered(&page_set, rules) {
            continue;
        }
        mid_value_sum += order_page_set(page_set, rules);
    }
    return mid_value_sum;
}

fn _print_rules(rules: &HashMap<u32, Vec<u32>>) {
    for (key, value) in rules {
        println!("----------");
        print!("{}: ", key);
        for page in value {
            print!("{}, ", page);
        }
        println!("");
    }
}

fn main() {
    let (rule_lines, pages_lines) = load_input(_INPUT_FILE_NAME);
    let rules = create_rules(&rule_lines);
    let pages = create_page_sets(&pages_lines);
    println!("{}", check_page_sets(&pages, &rules));
    println!("{}", sort_and_check_page_sets(&pages, &rules));
}
