const express = require('express')
const cors = require('cors')

const app = express()
app.use(cors())
app.use(express.json())

app.get('/api/products', (req, res) => {

  const categories = [
      { id: 1, name: 'Electronics' },
      { id: 2, name: 'Sport' },
      { id: 3, name: 'Work' },
   ]
   res.json(categories)

  const products = [
    { id: 3, name: 'Pendrive', price: 30, categoryId: 1 },
    { id: 2, name: 'Ball', price: 20, categoryId: 2 },
    { id: 1, name: 'Pen', price: 10, categoryId: 3 },
  ]
  res.json(products)
})

app.post('/api/payments', (req, res) => {
  console.log('Received payement data:', req.body)
  res.sendStatus(200)
})

const port = 3001
app.listen(port, () => {
  console.log(`Servers' port ${port}`)
})
