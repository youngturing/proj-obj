import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import CategoryList from './CategoryList';
import ProductList from './ProductList';
import React, { useState } from 'react';
import Cart from './Cart';

const categories = [
  { id: 1, name: 'Electronics' },
  { id: 2, name: 'Clothing' },
  { id: 3, name: 'Books' },
];

const products = [
  { id: 1, name: 'Laptop', price: 999.99, categoryId: 1 },
  { id: 2, name: 'T-Shirt', price: 19.99, categoryId: 2 },
  { id: 3, name: 'Book', price: 9.99, categoryId: 3 },
];

export default function App() {
  const [cartItems, setCartItems] = useState([]);

  const addToCart = (product) => {
    setCartItems((prevItems) => [...prevItems, product]);
  };

  return (
    <View style={styles.container}>
      <CategoryList categories={categories} />
      <ProductList products={products} addToCart={addToCart} />
      <Cart cartItems={cartItems} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
