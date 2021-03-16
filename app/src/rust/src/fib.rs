pub fn fib(n: u64) -> u64 {
  if n <= 1 {
    return 1;
  }
  fib(n - 1) + fib(n - 2)
}

fn main() {
  println!("Rust says the 40th Fibonacci number is {}", fib(40));
}
