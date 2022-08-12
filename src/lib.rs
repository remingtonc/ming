pub mod models;
pub mod schema;

#[macro_use]
extern crate diesel;
extern crate dotenv;

use diesel::pg::PgConnection;
use diesel::prelude::*;
use dotenv::dotenv;
use std::env;

pub fn establish_connection() -> PgConnection {
    dotenv().ok();

    let database_url = env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    PgConnection::establish(&database_url).expect(&format!("Error connecting to {}", database_url))
}

use self::models::{NewRecord, NewRecordStory, NewUser, Record, RecordStory, User};

pub fn create_user<'r>(conn: &PgConnection, name: &'r str) -> User {
    use schema::ming::user;
    let new_user: NewUser = NewUser { name: name };
    diesel::insert_into(user::table)
        .values(&new_user)
        .get_result(conn)
        .expect("Error creating new user!")
}

pub fn create_record<'r>(conn: &PgConnection, user_id: &'r i64) -> Record {
    use schema::ming::record;
    let new_record: NewRecord = NewRecord { user_id: user_id };
    diesel::insert_into(record::table)
        .values(&new_record)
        .get_result(conn)
        .expect("Error creating new record!")
}

pub fn create_story<'r>(conn: &PgConnection, user_id: &'r i64, content: &'r str) -> RecordStory {
    use schema::ming::record_story;
    let new_record: Record = create_record(conn, user_id);
    let new_story = NewRecordStory {
        record_story_id: &new_record.record_id,
        content: content,
    };
    diesel::insert_into(record_story::table)
        .values(&new_story)
        .get_result(conn)
        .expect("Error creating new Story!")
}
