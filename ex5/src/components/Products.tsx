import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Product {
    id: number,
    name: string,
    price: number,
}

const Products: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
        const response = await axios.get('http://localhost:3001/api/products');
        setProducts(response.data);
    } catch(error) {
        console.log(error);
    }
  };

  return (
    <div>
        <h2>Products</h2>
        <ul>
            {products.map((product) => (
                <li key={product.id}>
                    Product: {product.name} - price: {product.price}
                </li>
            ))}
        </ul>
    </div>
  );
};


export default Products;
 