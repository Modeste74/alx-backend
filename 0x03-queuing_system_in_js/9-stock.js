const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
	{id: 1, name: 'Suitcase 250', price: 50, stock: 4},
	{id: 2, name: 'Suitcase 450', price: 100, stock: 10},
	{id: 3, name: 'Suitcase 650', price: 350, stock: 2},
	{id: 4, name: 'Suitcase 450', price: 550, stock: 5},
	];

function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

async function reserveStockById(id, stock) {
  await setAsync(`item.${id}`, stock);
}

async function getCurrentReservedStockById(id) {
  const reservedStock = await getAsync(`item.${id}`);
  return reservedStock ? parseInt(reservedStock) : 0;
}

app.use(express.json());

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  console.log(`Got the itemId: ${itemId}`)
  const item = getItemById(itemId);

  if (!item) {
  	return res.json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  const productDetails = {
  	itemId: item.id,
  	itemName: item.name,
  	price: item.price,
  	initialAvailableQuantity: item.stock,
  	currentQuantity
  };
  res.json(productDetails);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.query.id);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity === item.stock) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, currentQuantity + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});