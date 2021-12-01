use std::fs;

pub fn solution_a()  -> usize {
  let values = read_data();
  let offset = 1;
  
  let mut counter = 0;
  for index in 0..values.len() - offset {
    if values[index + offset] > values[index] { counter += 1; }
  }

  counter
}

pub fn solution_b()  -> usize {
  let values = read_data();
  let offset = 3;
  
  let mut counter = 0;
  for index in 0..values.len() - offset {
    if values[index + offset] > values[index] { counter += 1; }
  }

  counter
}

fn read_data() -> Vec<usize> {
  let values = fs::read_to_string("../input/1.in").expect("Couldn't read the file :(");
  values
    .split("\n")
    .filter_map(|s| s.parse::<usize>().ok())
    .collect()
}
