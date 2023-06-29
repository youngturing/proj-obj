import Vapor

struct ProductController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let productsRoute = routes.grouped("products")
        productsRoute.get(use: getAllHandler)
        productsRoute.post(use: createHandler)
        productsRoute.group(":productID") { productRoute in
            productRoute.get(use: getHandler)
            productRoute.put(use: updateHandler)
            productRoute.delete(use: deleteHandler)
        }
    }

    func getAllHandler(req: Request) throws -> EventLoopFuture<[Product]> {
        return Product.query(on: req.db).all()
    }

    func createHandler(req: Request) throws -> EventLoopFuture<Product> {
        let product = try req.content.decode(Product.self)
        return product.save(on: req.db).map { product }
    }

    func getHandler(req: Request) throws -> EventLoopFuture<Product> {
        guard let productID = req.parameters.get("productID", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        return Product.find(productID, on: req.db)
            .unwrap(or: Abort(.notFound))
    }

    func updateHandler(req: Request) throws -> EventLoopFuture<Product> {
        guard let productID = req.parameters.get("productID", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        let updatedProduct = try req.content.decode(Product.self)
        return Product.find(productID, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                product.name = updatedProduct.name
                return product.save(on: req.db).map { product }
            }
    }

    func deleteHandler(req: Request) throws -> EventLoopFuture<HTTPStatus> {
        guard let productID = req.parameters.get("productID", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        return Product.find(productID, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                product.delete(on: req.db)
                    .transform(to: .noContent)
            }
    }
}

struct CategoryController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let categoriesRoute = routes.grouped("categories")
        categoriesRoute.get(use: getAllHandler)
        categoriesRoute.post(use: createHandler)
        categoriesRoute.group(":categoryID") { categoryRoute in
            categoryRoute.get(use: getHandler)
            categoryRoute.put(use: updateHandler)
            categoryRoute.delete(use: deleteHandler)
        }
    }

    func getAllHandler(req: Request) throws -> EventLoopFuture<[Category]> {
        return Category.query(on: req.db).all()
    }

    func createHandler(req: Request) throws -> EventLoopFuture<Category> {
        let category = try req.content.decode(Category.self)
        return category.save(on: req.db).map { category }
    }

    func getHandler(req: Request) throws -> EventLoopFuture<Category> {
        guard let categoryID = req.parameters.get("categoryID", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        return Category.find(categoryID, on: req.db)
            .unwrap(or: Abort(.notFound))
    }

    func updateHandler(req: Request) throws -> EventLoopFuture<Category> {
        guard let categoryID = req.parameters.get("categoryID", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        let updatedCategory = try req.content.decode(Category.self)
        return Category.find(categoryID, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { category in
                category.name = updatedCategory.name
                return category.save(on: req.db).map { category }
            }
    }

    func deleteHandler(req: Request) throws -> EventLoopFuture<HTTPStatus> {
        guard let categoryID = req.parameters.get("categoryID", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        return Category.find(categoryID, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { category in
                category.delete(on: req.db)
                    .transform(to: .noContent)
            }
    }
}
