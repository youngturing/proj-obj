<?php
require_once 'ProductController.php';

$controller = new ProductController();

// wyświetl listę produktów
echo "<h2>Lista produktów</h2>";
$products = $controller->index();
foreach ($products as $product) {
    echo "<p> ID: " . $product->getId() . ", Nazwa: " . $product->getName() . ", Opis: " . $product->getDescription() . ", Cena: " . $product->getPrice() . "</p>";
}

// dodaj nowy produkt
echo "<h2>Dodaj produkt</h2>";
$newProduct = $controller->create('Nowy produkt', 'Opis nowego produktu', 39.99);
echo "<p>Nowy produkt dodany. ID: " . $newProduct->getId() . ", Nazwa: " . $newProduct->getName() . ", Opis: " . $newProduct->getDescription() . ", Cena: " . $newProduct->getPrice() . "</p>";

// wyświetl pojedynczy produkt po ID
echo "<h2>Pojedynczy produkt</h2>";
$product = $controller->show(2);
if ($product) {
    echo "<p>ID: " . $product->getId() . ", Nazwa: " . $product->getName() . ", Opis: " . $product->getDescription() . ", Cena: " . $product->getPrice() . "</p>";
} else {
    echo "<p>Produkt nie istnieje.</p>";
}

// aktualizuj produkt po ID
echo "<h2>Aktualizuj produkt</h2>";
$updatedProduct = $controller->update(2, 'Zaktualizowana nazwa', 'Zaktualizowany opis', 49.99);
if ($updatedProduct) {
    echo "<p>Produkt zaktualizowany. ID: " . $updatedProduct->getId() . ", Nazwa: " . $updatedProduct->getName() . ", Opis: " . $updatedProduct->getDescription() . ", Cena: " . $updatedProduct->getPrice() . "</p>";
} else {
    echo "<p>Produkt nie istnieje.</p>";
}

// usuń produkt po ID
echo "<h2>Usuń produkt</h2>";
$deleted = $controller->delete(3);
if ($deleted) {
    echo "<p>Produkt usunięty.</p>";
} else {
    echo "<p>Produkt nie istnieje lub nie może być usunięty.</p>";
}
?>
