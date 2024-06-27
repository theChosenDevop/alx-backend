import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
const asyncGet = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});


async function displaySchoolValue(schoolName) {
  try {
    const value = await asyncGet(schoolName);
    console.log(value);
  } catch (err) {
    console.log(`Error retrieving value for ${schoolName}: ${err.message}`);
  };
};

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting ${schoolName}: ${err}`);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

  client.quit()
}

main();
