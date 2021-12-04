use std::fs;

enum Cmd {
  Forward(usize),
  Down(usize),
  Up(usize)
}

fn read_input() -> Vec<Cmd> {
    let file = fs::read_to_string("input/2.in").expect("couldn't read file");
    file.lines()
        .map(|s| {
          let cmd_str = s.split(" ");
          let step = cmd_str[1];
          match cmd_str.   {
              "forward" => Cmd::Forward()
          }
        })
}
