import React from 'react';
import { View, Text, FlatList } from 'react-native';

const CategoryList = ({ categories }) => {
  const renderCategoryItem = ({ item }) => (
    <View>
      <Text>{item.name}</Text>
    </View>
  );

  return (
    <View>
      <Text>Category List</Text>
      <FlatList
        data={categories}
        renderItem={renderCategoryItem}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

export default CategoryList;