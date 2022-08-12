pub mod ming {
    table! {
        ming.record (record_id) {
            record_id -> Int8,
            user_id -> Int8,
        }
    }

    table! {
        ming.record_activity (record_activity_id) {
            record_activity_id -> Int8,
            name -> Text,
            description -> Nullable<Text>,
            happiness -> Nullable<Int2>,
            productivity -> Nullable<Int2>,
            start_time -> Timestamptz,
            end_time -> Nullable<Timestamptz>,
        }
    }

    table! {
        ming.record_has_tag (tag_id, record_id) {
            tag_id -> Int8,
            record_id -> Int8,
        }
    }

    table! {
        ming.record_image (record_image_id) {
            record_image_id -> Int8,
            path -> Text,
        }
    }

    table! {
        ming.record_link (record_link_id) {
            record_link_id -> Int8,
            name -> Nullable<Text>,
            url -> Text,
        }
    }

    table! {
        ming.record_story (record_story_id) {
            record_story_id -> Int8,
            content -> Text,
        }
    }

    table! {
        ming.tag (tag_id) {
            tag_id -> Int8,
            name -> Text,
        }
    }

    table! {
        ming.user (user_id) {
            user_id -> Int8,
            name -> Text,
        }
    }

    joinable!(record -> user (user_id));
    joinable!(record_activity -> record (record_activity_id));
    joinable!(record_has_tag -> record (record_id));
    joinable!(record_has_tag -> tag (tag_id));
    joinable!(record_image -> record (record_image_id));
    joinable!(record_link -> record (record_link_id));
    joinable!(record_story -> record (record_story_id));

    allow_tables_to_appear_in_same_query!(
        record,
        record_activity,
        record_has_tag,
        record_image,
        record_link,
        record_story,
        tag,
        user,
    );
}
