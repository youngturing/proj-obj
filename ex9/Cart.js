import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);

  const addToCart = (product) => {
    setCartItems((prevItems) => [...prevItems, product]);
  };

  const removeFromCart = (product) => {
    setCartItems((prevItems) => prevItems.filter((item) => item.id !== product.id));
  };

  const renderCartItem = (item) => (
    <View key={item.id}>
      <Text>{item.name}</Text>
      <Button title="Remove" onPress={() => removeFromCart(item)} />
    </View>
  );

  return (
    <View>
      <Text>Cart</Text>
      {cartItems.length === 0 ? (
        <Text>Your cart is empty.</Text>
      ) : (
        cartItems.map(renderCartItem)
      )}
    </View>
  );
};

export default Cart;
