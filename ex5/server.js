const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Endpoint do pobierania danych o produktach
app.get('/api/products', (req, res) => {
  const products = [
    { id: 1, name: 'Pen', price: 10 },
    { id: 2, name: 'Ball', price: 20 },
    { id: 3, name: 'Pendrive', price: 30 },
  ];
  res.json(products);
});

// Endpoint do obsługi płatności
app.post('/api/payments', (req, res) => {
  console.log('Received payement data:', req.body);
  res.sendStatus(200);
});

const port = 3001; // Wybierz odpowiedni numer portu
app.listen(port, () => {
  console.log(`Servers' port ${port}`);
});
