extern crate diesel;
extern crate ming;

use self::ming::{create_user, establish_connection};
use std::io::stdin;

fn main() {
    let connection = establish_connection();

    println!("What would you like your username to be?");
    let mut username = String::new();
    stdin().read_line(&mut username).unwrap();
    let username = &username[..(username.len() - 1)]; // Drop the newline character
    let new_user = create_user(&connection, username);
    println!(
        "New user {} created with ID {}",
        new_user.name, new_user.user_id
    );
}
