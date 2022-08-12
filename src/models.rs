#[derive(Queryable)]
pub struct User {
    pub user_id: i64,
    pub name: String,
}

#[derive(Queryable)]
pub struct Record {
    pub record_id: i64,
    pub user_id: i64,
}

#[derive(Queryable)]
pub struct RecordStory {
    pub record_story_id: i64,
    pub content: String,
}

#[derive(Queryable)]
pub struct RecordImage {
    pub record_image_id: i64,
    pub path: String,
}

#[derive(Queryable)]
pub struct RecordActivity {
    pub record_activity_id: i64,
    pub name: String,
    pub description: String,
    pub happiness: i16,
    pub productivity: i16,
    pub start_time: std::time::SystemTime,
    pub end_time: std::time::SystemTime,
}

#[derive(Queryable)]
pub struct RecordLink {
    pub record_link_id: i64,
    pub name: String,
    pub url: String,
}

#[derive(Queryable)]
pub struct Tag {
    pub tag_id: i64,
    pub record_id: i64,
}

use super::schema::ming::{record, record_story, user};

#[derive(Insertable)]
#[table_name = "user"]
pub struct NewUser<'r> {
    pub name: &'r str,
}

#[derive(Insertable)]
#[table_name = "record"]
pub struct NewRecord<'r> {
    pub user_id: &'r i64,
}

#[derive(Insertable)]
#[table_name = "record_story"]
pub struct NewRecordStory<'r> {
    pub record_story_id: &'r i64,
    pub content: &'r str,
}
