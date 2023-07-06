import React from 'react';
import { View, Text, FlatList, Button } from 'react-native';

const ProductList = ({ products, addToCart }) => {
  const renderProductItem = ({ item }) => (
    <View>
      <Text>{item.name}</Text>
      <Text>{item.price}</Text>
      <Button title="Add to Cart" onPress={() => addToCart(item)} />
    </View>
  );

  return (
    <View>
      <Text>Product List</Text>
      <FlatList
        data={products}
        renderItem={renderProductItem}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

export default ProductList;
