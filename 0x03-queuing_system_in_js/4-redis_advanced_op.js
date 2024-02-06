import redis from 'redis';
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

const hashData = [
	{ field: 'Portland', value: 50 },
	{ field: 'Seattle', value: 80 },
	{ field: 'New York', value: 20 },
	{ field: 'Bogota', value: 20 },
	{ field: 'Cali', value: 40 },
	{ field: 'Paris', value: 2 },
	];

hashData.forEach(({ field, value }) => {
  client.hset('HolbertonSchools', field, value, redis.print);
});

client.hgetall('HolbertonSchools', (err, reply) => {
  console.log(reply);
});