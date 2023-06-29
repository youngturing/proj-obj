import NIOSSL
import Fluent
import FluentSQLiteDriver
import Leaf
import Vapor

// configures your application
public func configure(_ app: Application) async throws {
    // uncomment to serve files from /Public folder
    // app.middleware.use(FileMiddleware(publicDirectory: app.directory.publicDirectory))

    try app.redis.configuration()

    app.redis.configuration = try RedisConfiguration(hostname: "redis", port: 6379)
    app.redis.configuration.password = "password"
    app.redis.use(.default, as: .redis)

    app.databases.use(.sqlite(.file("db.sqlite")), as: .sqlite)

    app.migrations.add(CreateTodo())

    app.views.use(.leaf)

    

    // register routes
    try routes(app)
}

func routes(_ app: Application) throws {
    app.get { req in
        return req.view.render("index")
    }

    try app.register(collection: ProductController())
    try app.register(collection: CategoryController())
}
