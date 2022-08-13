use actix_web::{web, App, HttpResponse, HttpServer};
use ming::settings::load_settings_file;

fn config_static(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::resource("/")
            .route(web::get().to(|| async { HttpResponse::Ok().body("this is a static file") })),
    );
}

fn config_api(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::resource("/")
            .route(web::get().to(|| async { HttpResponse::Ok().body("\"this is javascript\"") })),
    );
}

fn config_ui(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::resource("/")
            .route(web::get().to(|| async { HttpResponse::Ok().body("this is html") })),
    );
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let loaded_settings = load_settings_file("config.json");
    HttpServer::new(|| {
        App::new()
            .configure(config_ui)
            .service(web::scope("/api").configure(config_api))
            .service(web::scope("/static").configure(config_static))
    })
    .bind((loaded_settings.domain, loaded_settings.port))?
    .run()
    .await
}
