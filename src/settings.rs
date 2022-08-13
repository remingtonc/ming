use serde::{Deserialize, Serialize};
use std::fs::File;

#[derive(Serialize, Deserialize)]
pub struct Settings {
    pub scheme: String,
    pub domain: String,
    pub port: u16,
    pub database_url: String,
}

pub fn load_settings_file(filename: &str) -> Settings {
    let settings_fd = File::open(filename).expect("Error opening settings file!");
    serde_json::from_reader(settings_fd).unwrap()
}
