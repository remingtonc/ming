#[derive(Queryable)]
pub struct User {
    pub user_id: uint64,
    pub name: String,
}

#[derive(Queryable)]
pub struct Record {
    pub record_id: uint64,
    pub user_id: uint64,
    pub name: String,
}
