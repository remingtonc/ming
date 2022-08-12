extern crate diesel;
extern crate ming;

use self::diesel::prelude::*;
use self::ming::{create_story, establish_connection};
use std::io::{stdin, Read};

fn main() {
    use self::ming::schema::ming::user::dsl::*;
    let connection = establish_connection();

    println!("What is your username?");
    let mut username = String::new();
    stdin().read_line(&mut username).unwrap();
    let username = &username[..(username.len() - 1)]; // Drop the newline character
    let user_id_int: i64 = user
        .filter(name.eq(username))
        .select(user_id)
        .first(&connection)
        .expect("Could not load user!");
    println!("\nOk! Let's write! (Press {} when finished)\n", EOF);
    let mut content = String::new();
    stdin().read_to_string(&mut content).unwrap();
    let story = create_story(&connection, &user_id_int, &content);
    println!("Created story with ID {}", story.record_story_id)
}

#[cfg(not(windows))]
const EOF: &'static str = "CTRL+D";

#[cfg(windows)]
const EOF: &'static str = "CTRL+Z";
