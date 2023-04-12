<?php

require_once 'Product.php';

class ProductController {
    private $products = array();

    // konstruktor, tworzy przykładowe produkty
    public function __construct() {
        $this->products[] = new Product(1, 'Produkt 1', 'Opis produktu 1', 9.99);
        $this->products[] = new Product(2, 'Produkt 2', 'Opis produktu 2', 19.99);
        $this->products[] = new Product(3, 'Produkt 3', 'Opis produktu 3', 29.99);
    }

    // metoda pobierająca listę produktów
    public function index() {
        return $this->products;
    }

    // metoda dodająca nowy produkt
    public function create($name, $description, $price) {
        $id = count($this->products) + 1;
        $product = new Product($id, $name, $description, $price);
        $this->products[] = $product;
        return $product;
    }

    // metoda pobierająca pojedynczy produkt po ID
    public function show($id) {
        foreach ($this->products as $product) {
            if ($product->getId() == $id) {
                return $product;
            }
        }
        return null;
    }

    // metoda aktualizująca produkt
    public function update($id, $name, $description, $price) {
        foreach ($this->products as $product) {
            if ($product->getId() == $id) {
                $product->setName($name);
                $product->setDescription($description);
                $product->setPrice($price);
                return $product;
            }
        }
        return null;
    }

    // metoda usuwająca produkt
    public function delete($id) {
        foreach ($this->products as $key => $product) {
            if ($product->getId() == $id) {
                unset($this->products[$key]);
                return true;
            }
        }
        return false;
    }
}
